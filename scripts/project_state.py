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


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping
)


def load(root, path):
    result = yaml.load(
        (root / path).read_text(encoding='utf-8'), Loader=UniqueKeyLoader
    )
    if not isinstance(result, dict):
        raise ValueError(f'Expected mapping: {path}')
    return result


def metadata(root, path, field):
    m = re.search(
        rf'^\*\*{re.escape(field)}:\*\*\s*(.+?)\s*$',
        (root / path).read_text(encoding='utf-8'),
        re.M,
    )
    return m.group(1).strip().strip('`') if m else None


def managed_views(root):
    s = load(root, SYSTEM)
    lab = load(root, LAB)
    w = s['current_work']
    env = s['environment_first_reset']
    v0 = env['v0']
    checkpoint = env['recovery_checkpoint']

    lines = [
        f"Дата синхронизации: **{s['updated_at']}**.",
        f"Направление: **{w['direction']}**.",
        f"Продуктовое направление: **{w['product_direction']}**.",
        f"Маршрут: `{w['route']}`; цель: `{w['objective']}`.",
        f"**Следующий шаг: {w['next_step_label']}**",
        f"Активная архитектура: `{w['artifact']}` — `{w['artifact_status']}`.",
        (
            "V0: одна способность; "
            f"{v0['scenario_count_min']}–{v0['scenario_count_max']} сценариев; "
            f"{v0['real_world_transfer_experiments']} эксперимент переноса в реальность; "
            "ручная подача допустима."
        ),
        f"Product thesis: `{env['product_thesis']}`.",
        (
            f"Foundation: последний утверждённый параметр "
            f"`{s['foundation_state']['last_approved_point']}`; "
            f"Stage 5 — `{s['foundation_state']['stage_5_status']}`."
        ),
        f"Capability reference: `{s['training_state']['stage_1_capability']['id']}`.",
        (
            f"Опросник: `{lab['daily_trajectory_questionnaire']['id']}` — "
            f"`{lab['daily_trajectory_questionnaire']['status']}`; телеметрия, не механизм продукта."
        ),
        (
            f"Курс: `{s['course_first_reset']['status']}`; роль — "
            f"`{s['course_first_reset']['artifacts_role']}`."
        ),
        (
            "Реализация ПО: "
            f"`{str(w['software_implementation_authorized']).lower()}`; "
            "внешний пилот: "
            f"`{str(w['external_pilot_authorized']).lower()}`."
        ),
        f"Checkpoint: `{checkpoint}`.",
        'Активные рабочие уточнения: '
        + '; '.join(f"`{v['document']}`" for v in s['active_working_inputs'])
        + '.',
        (
            "Научная граница: успех в симуляции не доказывает перенос; "
            "реальный перенос фиксируется отдельно."
        ),
        f'Источники: `{SYSTEM}`; `{FOUNDATION}`; `{LAB}`.',
    ]
    current = '\n\n'.join(lines)
    return [
        ('README.md', 'CURRENT', current),
        ('docs/CURRENT_STATE.md', 'CURRENT', current),
    ]


def replace_block(text, name, body):
    start, end = f'<!-- SP:{name}:BEGIN -->', f'<!-- SP:{name}:END -->'
    if text.count(start) != 1 or text.count(end) != 1:
        raise ValueError(f'Expected exactly one {name} block')
    before, rest = text.split(start)
    _, after = rest.split(end)
    return before + start + '\n' + body + '\n' + end + after
