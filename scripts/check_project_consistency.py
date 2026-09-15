#!/usr/bin/env python3
"""Fail fast on known Selection Point status/documentation drift.

Stdlib-only by design: this check must run in GitHub Actions without project dependencies.
It does not validate the truth of the method; it validates a small set of repository invariants.
"""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]


def read(rel: str) -> str:
    path = ROOT / rel
    if not path.exists():
        fail(f"missing required file: {rel}")
        return ""
    return path.read_text(encoding="utf-8")


errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def require(text: str, needle: str, where: str) -> None:
    if needle not in text:
        fail(f"{where}: expected marker not found: {needle!r}")


def forbid(text: str, needle: str, where: str) -> None:
    if needle in text:
        fail(f"{where}: stale/conflicting marker still present: {needle!r}")


PROJECT_STATE = "docs/FOUNDATION/PROJECT_STATE.yaml"
LAB_STATE = "docs/PRODUCT_LAB/LAB_STATE.yaml"
RESEARCH_PLAN = "docs/PRODUCT_LAB/RESEARCH_PLAN.md"
LAB_INDEX = "docs/PRODUCT_LAB/00_LAB_INDEX.md"
EVENT_MODEL = "docs/PRODUCT_LAB/REALITY_EVENT_MODEL_V0_2.md"
METRICS = "docs/PRODUCT_LAB/PILOT_METRICS_SPEC_V0_1.md"
DATA_POLICY = "docs/PRODUCT_LAB/PARTICIPANT_DATA_POLICY_V0_1.md"
PILOT = "docs/PRODUCT_LAB/PERSONAL_TRAJECTORY_PILOT_V0.md"

project = read(PROJECT_STATE)
lab = read(LAB_STATE)
research = read(RESEARCH_PLAN)
index = read(LAB_INDEX)
event_model = read(EVENT_MODEL)
metrics = read(METRICS)
data_policy = read(DATA_POLICY)
pilot = read(PILOT)

# Foundation must remain paused before S5 unless the owner explicitly changes it.
require(project, "active_stage: 4", PROJECT_STATE)
require(project, "active_parameter: null", PROJECT_STATE)
require(project, "next_candidate: SP-S5-P01", PROJECT_STATE)
require(project, "next_status: unopened", PROJECT_STATE)
require(project, "stage_5_not_opened: true", PROJECT_STATE)
require(project, "rc018_approved: true", PROJECT_STATE)

# Product Lab current task and gates.
require(lab, "current_task: SP-LAB-PILOT-001", LAB_STATE)
require(lab, "current_task_status: active", LAB_STATE)
require(lab, 'foundation_sync: "RC-018"', LAB_STATE)
require(lab, "no_external_user_pilot_in_lab_0: true", LAB_STATE)
require(lab, "do_not_open_SP_LAB_002_without_explicit_owner_direction: true", LAB_STATE)
require(lab, "external_user_pilot_status: unopened", LAB_STATE)

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

# New Lab artifacts must be discoverable from the index.
for rel in (EVENT_MODEL, METRICS, DATA_POLICY):
    filename = Path(rel).name
    require(index, filename, LAB_INDEX)

# LAB_STATE must point at the measurement foundation.
for filename in (Path(EVENT_MODEL).name, Path(METRICS).name, Path(DATA_POLICY).name):
    require(lab, filename, LAB_STATE)

if errors:
    print("Selection Point consistency check FAILED:\n")
    for item in errors:
        print(f"- {item}")
    sys.exit(1)

print("Selection Point consistency check passed.")
print("- Foundation: S4 complete, S5 unopened, RC-018 approved")
print("- Product Lab: self-pilot active, external pilot unopened")
print("- RC-018 event/metrics/data boundaries present")
