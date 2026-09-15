#!/usr/bin/env python3
"""Fail fast on known Selection Point status/documentation drift.

Stdlib-only by design: this check must run in GitHub Actions without project dependencies.
It does not validate the truth of the method; it validates repository/project-system invariants.
"""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def read(rel: str) -> str:
    path = ROOT / rel
    if not path.exists():
        fail(f"missing required file: {rel}")
        return ""
    return path.read_text(encoding="utf-8")


def require(text: str, needle: str, where: str) -> None:
    if needle not in text:
        fail(f"{where}: expected marker not found: {needle!r}")


def forbid(text: str, needle: str, where: str) -> None:
    if needle in text:
        fail(f"{where}: stale/conflicting marker still present: {needle!r}")


PROJECT_STATE = "docs/FOUNDATION/PROJECT_STATE.yaml"
SYSTEM_STATE = "docs/PROJECT_SYSTEM/PROJECT_SYSTEM_STATE.yaml"
CONTROL_PLANE = "docs/PROJECT_SYSTEM/PROJECT_CONTROL_PLANE.md"
SYNC_PROTOCOL = "docs/PROJECT_SYSTEM/CROSS_REPO_SYNC_PROTOCOL.md"
HEALTH_CONTRACT = "docs/PROJECT_SYSTEM/HEALTH_LAB_NODE_CONTRACT.md"
SYSTEM_DECISION = "docs/PROJECT_SYSTEM/DECISION_PSYS_001_2026-09-15.md"
LAB_STATE = "docs/PRODUCT_LAB/LAB_STATE.yaml"
RESEARCH_PLAN = "docs/PRODUCT_LAB/RESEARCH_PLAN.md"
LAB_INDEX = "docs/PRODUCT_LAB/00_LAB_INDEX.md"
EVENT_MODEL = "docs/PRODUCT_LAB/REALITY_EVENT_MODEL_V0_2.md"
METRICS = "docs/PRODUCT_LAB/PILOT_METRICS_SPEC_V0_1.md"
DATA_POLICY = "docs/PRODUCT_LAB/PARTICIPANT_DATA_POLICY_V0_1.md"
PILOT = "docs/PRODUCT_LAB/PERSONAL_TRAJECTORY_PILOT_V0.md"
README = "README.md"

project = read(PROJECT_STATE)
system = read(SYSTEM_STATE)
control = read(CONTROL_PLANE)
sync = read(SYNC_PROTOCOL)
health_contract = read(HEALTH_CONTRACT)
_ = read(SYSTEM_DECISION)
lab = read(LAB_STATE)
research = read(RESEARCH_PLAN)
index = read(LAB_INDEX)
event_model = read(EVENT_MODEL)
metrics = read(METRICS)
data_policy = read(DATA_POLICY)
pilot = read(PILOT)
readme = read(README)

# Foundation remains paused before S5 unless owner explicitly changes it.
require(project, "active_stage: 4", PROJECT_STATE)
require(project, "active_parameter: null", PROJECT_STATE)
require(project, "next_candidate: SP-S5-P01", PROJECT_STATE)
require(project, "next_status: unopened", PROJECT_STATE)
require(project, "stage_5_not_opened: true", PROJECT_STATE)
require(project, "rc018_approved: true", PROJECT_STATE)

# Project-level control plane and registered evidence node.
require(system, "control_plane_id: SP-PSYS-001", SYSTEM_STATE)
require(system, "node_id: SP-HLAB-001", SYSTEM_STATE)
require(system, "repository: xahinvest-DNA/Selection-point-health-lab", SYSTEM_STATE)
require(system, "role: private_evidence_node", SYSTEM_STATE)
require(system, "external_user_pilot: unopened", SYSTEM_STATE)
require(system, "raw_data_to_public_repo: forbidden", SYSTEM_STATE)
require(system, "measurement_adherence_is_not_domain_outcome: true", SYSTEM_STATE)
require(control, "measurement adherence ≠ health-domain action", CONTROL_PLANE)
require(sync, "Raw records decide what was actually recorded", SYNC_PROTOCOL)
require(health_contract, "SP-HLAB-001", HEALTH_CONTRACT)
require(health_contract, "Legacy raw records", HEALTH_CONTRACT)
require(health_contract, "prompt_exposure", HEALTH_CONTRACT)
require(health_contract, "measurement_adherence", HEALTH_CONTRACT)
require(readme, "Project Control Plane", README)
require(readme, "SP-HLAB-001", README)

# Product Lab current task and gates.
require(lab, "current_task: SP-LAB-PILOT-001", LAB_STATE)
require(lab, "current_task_status: active", LAB_STATE)
require(lab, 'foundation_sync: "RC-018"', LAB_STATE)
require(lab, 'project_system_sync: "SP-PSYS-001"', LAB_STATE)
require(lab, "evidence_node: SP-HLAB-001", LAB_STATE)
require(lab, "no_external_user_pilot_in_lab_0: true", LAB_STATE)
require(lab, "do_not_open_SP_LAB_002_without_explicit_owner_direction: true", LAB_STATE)
require(lab, "external_user_pilot_status: unopened", LAB_STATE)
require(lab, "legacy_raw_records_must_not_be_rewritten: true", LAB_STATE)
require(lab, "measurement_adherence_is_domain_outcome: false", LAB_STATE)

# Known drift fixed on 2026-09-15 must not reappear.
forbid(research, "\n- пилот;\n", RESEARCH_PLAN)
forbid(
    pilot,
    "Внутренне принятое решение не считается реализованным выбором, пока оно не проявилось в наблюдаемом действии.",
    PILOT,
)

# RC-018-aware research instrumentation.
require(event_model, "selected_continuation", EVENT_MODEL)
require(event_model, "realized_continuation", EVENT_MODEL)
require(event_model, "conscious_non_action", EVENT_MODEL)
require(metrics, "prompt_exposure", METRICS)
require(metrics, "Selected → Realized", METRICS)
require(data_policy, "сырые персональные записи участников", DATA_POLICY)

# Project-system and Lab artifacts must be discoverable.
for rel in (SYSTEM_STATE, CONTROL_PLANE, SYNC_PROTOCOL, HEALTH_CONTRACT, EVENT_MODEL, METRICS, DATA_POLICY):
    filename = Path(rel).name
    target = README if rel.startswith("docs/PROJECT_SYSTEM/") else LAB_INDEX
    target_text = readme if target == README else index
    require(target_text, filename, target)

# Product Lab index must explain the evidence-node boundary.
require(index, "SP-HLAB-001", LAB_INDEX)
require(index, "measurement adherence", LAB_INDEX)
require(index, "Исторические raw-записи Health Lab за 12–14 сентября", LAB_INDEX)

# LAB_STATE points at measurement and project-system foundations.
for filename in (
    Path(EVENT_MODEL).name,
    Path(METRICS).name,
    Path(DATA_POLICY).name,
    Path(SYSTEM_STATE).name,
    Path(CONTROL_PLANE).name,
    Path(SYNC_PROTOCOL).name,
    Path(HEALTH_CONTRACT).name,
):
    require(lab, filename, LAB_STATE)

if errors:
    print("Selection Point consistency check FAILED:\n")
    for item in errors:
        print(f"- {item}")
    sys.exit(1)

print("Selection Point consistency check passed.")
print("- Foundation: S4 complete, S5 unopened, RC-018 approved")
print("- Project system: SP-PSYS-001 active; SP-HLAB-001 registered private evidence node")
print("- Product Lab: owner self-pilot active, external pilot unopened")
print("- RC-018 event/metrics/privacy/promotion boundaries present")
print("- Legacy Health Lab raw records are governed as immutable source data")
