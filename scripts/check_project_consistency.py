#!/usr/bin/env python3
"""Validate current authority, recovery and execution boundaries, not historical phrases."""
import argparse
from pathlib import Path
import re
import yaml
from project_state import ROOT,SYSTEM,FOUNDATION,LAB,load,metadata,managed_views,replace_block

def validate(root=ROOT):
    errors=[]
    def require(condition,message):
        if not condition:errors.append(message)
    def paths(value,trail,external=False):
        if isinstance(value,dict):
            external=external or value.get('repository')=='xahinvest-DNA/Selection-point-health-lab'
            for k,v in value.items():paths(v,f'{trail}.{k}',external)
        elif isinstance(value,list):
            for i,v in enumerate(value):paths(v,f'{trail}[{i}]',external)
        elif isinstance(value,str) and value.startswith('docs/') and value.endswith(('.md','.yaml')) and not external:
            target=(root/value).resolve()
            require(target.is_relative_to(root.resolve()) and target.is_file(),f'{trail}: missing local file {value}')
    try:
        s,f,lab=(load(root,p) for p in (SYSTEM,FOUNDATION,LAB))
        for name,doc in ((SYSTEM,s),(FOUNDATION,f),(LAB,lab)):paths(doc,name)
        w=s['current_work'];r=s['course_first_reset'];c=r['stage_1_course'];t=s['training_state'];b=s['new_chat_bootstrap']['read_first']
        require(len(b)==len(set(b)),'bootstrap: duplicate documents')
        require(b[:2]==[SYSTEM,s['recovery']['current_checkpoint']],'bootstrap: current checkpoint must be second')
        required=[r['decision'],c['course_structure_decision'],c['course_structure'],w['artifact']]+[x['document'] for x in s['active_working_inputs']]
        require(all(p in b for p in required),'bootstrap: current course/decision/working input missing')
        require(len(b)<=10,'bootstrap: more than ten mandatory documents; route additional reading by task')
        require(w['route']==s['operating_model']['current_authorization'],'active route differs from operating authorization')
        require(w['objective']==r['active_objective'],'current objective differs from course-first objective')
        require(w['next_step']==r['next_step'],'two different next steps in system state')
        if w['artifact']==c['lesson_template']:
            require(w['artifact_status']==c['lesson_template_status'],'current artifact status differs from template status')
        for path,field,expected,label in [
            (w['artifact'],'Status',w['artifact_status'],'current artifact document status'),
            (c['lesson_template'],'ID',c['lesson_template_id'],'template ID'),
            (c['course_structure'],'ID',c['course_structure_id'],'course structure ID'),
            (c['course_structure'],'Status',c['course_structure_status'],'course structure status'),
            (t['stage_1_capability']['document'],'ID',t['stage_1_capability']['id'],'capability ID'),
            (t['stage_1_research_packet']['deliverable'],'Status',t['stage_1_research_packet']['status'],'research packet status')]:
            require(metadata(root,path,field)==expected,f'{label} differs from SSOT')
        if w['artifact']==c['lesson_template'] and w['artifact_status']=='draft_for_owner_review':
            require(w['owner_decision_required'] is True and w['execution_authorized'] is False,'unapproved template must not authorize full lesson execution')
        if r['status']=='approved' and not r['gate_pipeline_active']:
            require(r['v0_validation_execution_active'] is False,'course-first reset conflicts with V0 execution')
            require(t['stage_1_post_protocol_validation']['v0_execution_authorized'] is False,'suspended V0 is authorized')
            require(t['stage_1_post_protocol_validation']['operational_role']=='execution_suspended','V0 role is not suspended')
            for k,v in t.items():
                if isinstance(v,dict) and k.startswith('stage_1_'):
                    require('next_step' not in v,f'{k}: historical next step leaks into active state')
                    require(v.get('operational_role') in ('research_reference_only','execution_suspended'),f'{k}: missing operational role')
                    require(not any(re.fullmatch(r'gate_[a-h]_opened',x) for x in v),f'{k}: undated historical gate authorization')
        for p in [t['stage_1_post_protocol_validation']['design'],t['stage_1_post_protocol_validation']['approval_decision']]:
            require('<!-- SP:SUSPENDED -->' in (root/p).read_text(),f'{p}: suspended permission lacks successor notice')
        for p in (root/'docs/TRAINING').glob('STAGE_1_*.md'):
            require('<!-- SP:REFERENCE -->' in p.read_text(),f'{p.name}: historical training artifact lacks role notice')
        for path in [r['active_brief'],c['course_structure'],c['lesson_template']]:
            content=(root/path).read_text()
            for item in s['active_working_inputs']:require(item['document'] in content,f'{path}: active working input missing')
        for path,name,body in managed_views(root):
            text=(root/path).read_text()
            require(text==replace_block(text,name,body),f'{path}: generated {name} view stale')
        for k in ('id','status','document'):
            require(lab['daily_trajectory_questionnaire'][k]==r['trajectory_questionnaire'][k],f'questionnaire {k} differs between manifests')
        q=lab['daily_trajectory_questionnaire']
        require(metadata(root,q['document'],'Status')==q['status'],'questionnaire document status differs')
        require(metadata(root,q['document'],'ID')==q['id'],'questionnaire document ID differs')
        require(lab['project_route_authority']==SYSTEM,'Lab has no current project-route authority')
        require(s['current_gates']['external_user_pilot']==lab['status']['external_user_pilot_status'],'external pilot status differs')
        if f['constraints']['stage_5_not_opened']:
            require(s['current_gates']['stage_5']=='unopened' and f['status']['next_status']=='unopened','Foundation S5 boundary differs')
        require(s['current_gates']['product_lab_002']==lab['sp_lab_002_gate']['status'],'SP-LAB-002 status differs')
        require(s['promotion_rule']['raw_data_to_public_repo']=='forbidden' and lab['measurement_foundation']['raw_participant_data_in_public_repo_allowed'] is False,'raw-data publication boundary weakened')
        require(s['current_shared_contract']['selected_not_realized'] is True and lab['constraints']['selected_continuation_not_equal_realized_continuation'] is True,'selected/realized boundary weakened')
        require(f['constraints']['rc018_approved'] is True, 'RC-018 approval boundary missing')
        require(lab['measurement_foundation']['composite_selection_score_allowed'] is False, 'unvalidated composite score authorized')
        require(lab['measurement_foundation']['measurement_adherence_is_domain_outcome'] is False, 'measurement adherence confused with domain outcome')
        require(lab['measurement_foundation']['prompt_exposure_must_be_recorded'] is True, 'prompt exposure contract missing')
        require(lab['constraints']['legacy_raw_records_must_not_be_rewritten'] is True, 'legacy raw immutability weakened')
        require(s['current_shared_contract']['conscious_non_action_may_be_realized'] is True, 'conscious non-action boundary missing')
        for path in ['docs/PROJECT_SYSTEM/SP_CHAT_OPERATING_MODEL.md', 'docs/PROJECT_SYSTEM/PROJECT_CONTROL_PLANE.md']:
            current_text=(root/path).read_text()
            require('PROJECT_SYSTEM_STATE.yaml.current_work' in current_text, f'{path}: missing active-route pointer')
            require('Current authorization is Gate B' not in current_text and 'The currently authorized training cycle is:' not in current_text, f'{path}: obsolete Gate authorization')
        tech=s['technical_work']
        require((metadata(root,tech['task'],'Status') or '').startswith(tech['status']),'technical task status differs from SSOT')
        if tech['status']=='completed':require(bool(tech['implementation_repository'] and tech['completion_commit']),'technical completion lacks provenance')
        d=load(root,s['operations_contract'])
        require(lab['reminder_delivery_state']==s['operations_contract'],'reminder contract differs between manifests')
        if q['status']=='draft_for_owner_review':
            require(d['full_questionnaire_v0_2_approved'] is False and d['full_questionnaire_v0_2_deployed'] is False,'draft questionnaire marked deployed/approved')
        require(d['evening']['q9']=='С какими 1–3 фактами ты входишь в завтра?','deployed Q9 reintroduces inferred availability')
        require(d['timezone']=='Europe/Moscow','reminder timezone differs from owner timezone')
        for name in ('morning','midday'):require(d[name]['data_entry_required'] is False,f'{name}: violates once-daily data entry')
        wf=yaml.load((root/'.github/workflows/selection-point-consistency.yml').read_text(),Loader=yaml.BaseLoader)
        require('pull_request' in wf['on'] and 'push' in wf['on'],'CI must cover pushes and pull requests')
        for event in ('push','pull_request'):
            config=wf['on'].get(event) or {}
            require(not any(k in config for k in ('paths','paths-ignore')),f'CI {event}: path filter leaves drift blind spots')
    except (KeyError,ValueError,TypeError,AttributeError,OSError,yaml.YAMLError) as e:
        errors.append(f'State/schema error: {e}')
    return errors
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',type=Path,default=ROOT);a=p.parse_args()
    errors=validate(a.root)
    print('Selection Point consistency check FAILED:\n'+'\n'.join('- '+e for e in errors) if errors else 'Selection Point consistency check passed: current route, recovery, roles, generated views, contracts and CI agree.')
    raise SystemExit(bool(errors))
