"""Shared strict YAML loading and generated state views; no network or mutation."""
from pathlib import Path
import re
import yaml
ROOT = Path(__file__).resolve().parents[1]
SYSTEM = 'docs/PROJECT_SYSTEM/PROJECT_SYSTEM_STATE.yaml'
FOUNDATION = 'docs/FOUNDATION/PROJECT_STATE.yaml'
LAB = 'docs/PRODUCT_LAB/LAB_STATE.yaml'
class UniqueKeyLoader(yaml.SafeLoader):
    pass
def unique_mapping(loader, node, deep=False):
    result = {}
    for kn, vn in node.value:
        key = loader.construct_object(kn, deep=deep)
        if key in result:
            raise ValueError(f'Duplicate YAML key: {key}')
        result[key] = loader.construct_object(vn, deep=deep)
    return result
UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)
def load(root, path):
    result = yaml.load((root/path).read_text(encoding='utf-8'), Loader=UniqueKeyLoader)
    if not isinstance(result, dict):
        raise ValueError(f'Expected mapping: {path}')
    return result
def metadata(root, path, field):
    m = re.search(rf'^\*\*{re.escape(field)}:\*\*\s*(.+?)\s*$', (root/path).read_text(), re.M)
    return m.group(1).strip().strip('`') if m else None
def managed_views(root):
    s, f, lab = (load(root, p) for p in (SYSTEM, FOUNDATION, LAB))
    w, c, fs = s['current_work'], s['course_first_reset']['stage_1_course'], f['status']
    lines = [
        f"Дата синхронизации: **{s['updated_at']}**.",
        f"Направление: **{w['direction']}**.",
        f"Маршрут: `{w['route']}`; цель: `{w['objective']}`.",
        f"**Следующий шаг: {w['next_step_label']}.**",
        f"Артефакт: `{w['artifact']}` — `{w['artifact_status']}`.",
        f"Структура: `{c['course_structure_id']}` — `{c['course_structure_status']}`; {c['proposed_lesson_count']} уроков, ориентация и интеграция отдельно.",
        f"Foundation: последний утверждённый параметр `{fs['last_approved']}`; следующий кандидат `{fs['next_candidate']}` — `{fs['next_status']}`.",
        f"Capability: `{s['training_state']['stage_1_capability']['id']}`.",
        f"Опросник: `{lab['daily_trajectory_questionnaire']['id']}` — `{lab['daily_trajectory_questionnaire']['status']}`; отдельная телеметрия.",
        f"Checkpoint: `{s['recovery']['current_checkpoint']}`.",
        'Активные рабочие уточнения: '+ '; '.join(f"`{v['document']}`" for v in s['active_working_inputs'])+'.',
        f"Gate-маршрут активен: `{str(s['course_first_reset']['gate_pipeline_active']).lower()}`; V0 execution: `{str(s['training_state']['stage_1_post_protocol_validation']['v0_execution_authorized']).lower()}`.",
        'Закрытые области: '+ '; '.join(f'`{k}: {v}`' for k,v in s['current_gates'].items() if v=='unopened')+'.',
        f'Источники: `{SYSTEM}`; `{FOUNDATION}`; `{LAB}`.'
    ]
    t=s['technical_work']; prev=t['previous_task']
    tech='\n\n'.join([
        f"Текущая техническая задача: `{t['task']}`.",
        f"Статус: `{t['status']}`. Завершение требует проверки реализации.",
        f"Репозиторий реализации: `{t['implementation_repository'] or 'unknown'}`; completion commit: `{t['completion_commit'] or 'unknown'}`.",
        f"Предыдущая задача: `{prev['document']}` — `{prev['status']}` по отчёту от `{prev['report_date']}`."
    ])
    current='\n\n'.join(lines)
    return [('README.md','CURRENT',current),('docs/CURRENT_STATE.md','CURRENT',current),('docs/CODEX_TASKS.md','TECHNICAL',tech)]
def replace_block(text,name,body):
    start,end=f'<!-- SP:{name}:BEGIN -->',f'<!-- SP:{name}:END -->'
    if text.count(start)!=1 or text.count(end)!=1:
        raise ValueError(f'Expected exactly one {name} block')
    before,rest=text.split(start);_,after=rest.split(end)
    return before+start+'\n'+body+'\n'+end+after
