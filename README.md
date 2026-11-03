# Selection Point

Selection Point — проект о восстановлении и развитии практически доступной способности выбирать продолжение в реальной ситуации и превращать выбранное продолжение в действие с обратной связью.

С 3 ноября 2026 года активная продуктовая гипотеза — **environment-first**: не курс как основной механизм, а ограниченная адаптивная среда / симулятор, в которой человек многократно сталкивается с репрезентативными ситуациями, делает выбор, видит последствия и затем проверяет перенос различения в реальность.

Это изменение не переписывает утверждённый Foundation canon. Старые course/training artifacts сохраняются как история и исследовательское сырьё.

## Current state

<!-- SP:CURRENT:BEGIN -->
Дата синхронизации: **2026-11-03**.

Направление: **Системно выбирать и фактически совершать действия, которые сохраняют здоровье, повышают физическую эффективность и расширяют возможности тела в будущем.**.

Продуктовое направление: **Создать среду, в которой способность выбора становится практически доступнее через повторяющиеся репрезентативные ситуации, последствия, обратную связь и проверяемый перенос в реальность.**.

Маршрут: `stage_1_environment_first_development`; цель: `define_and_build_minimal_adaptive_selection_environment`.

**Следующий шаг: Зафиксировать одну тренируемую способность V0, сценарную грамматику 10–15 репрезентативных ситуаций и минимальные признаки переноса из симуляции в реальность.**

Активная архитектура: `docs/PRODUCT_LAB/ADAPTIVE_ENVIRONMENT_ARCHITECTURE_V0.md` — `approved_direction_working_architecture`.

V0: одна способность; 10–15 сценариев; 1 эксперимент переноса в реальность; ручная подача допустима.

Product thesis: `docs/PRODUCT_LAB/PRODUCT_THESIS.md`.

Foundation: последний утверждённый параметр `SP-S4-P13`; Stage 5 — `unopened`.

Capability reference: `SP-TR-S1-CAP-002`.

Опросник: `SP-DTQ-002` — `withdrawn_for_redesign`; телеметрия, не механизм продукта.

Курс: `superseded_as_active_route`; роль — `historical_reference_and_scenario_source`.

Реализация ПО: `false`; внешний пилот: `false`.

Checkpoint: `docs/PROJECT_SYSTEM/RECOVERY_CHECKPOINT_2026-11-03_ENVIRONMENT_FIRST_RESET.md`.

Активные рабочие уточнения: `docs/FOUNDATION/PROJECT_OPERATING_PROTOCOL_ADDENDUM_2026-10-05_DIRECTION_ROUTE_ACTION.md`; `docs/FOUNDATION/SOURCE_MATERIALS/29_2026-11-03_ADAPTATION_ENVIRONMENT_AND_TRANSFER.md`.

Научная граница: успех в симуляции не доказывает перенос; реальный перенос фиксируется отдельно.

Источники: `docs/PROJECT_SYSTEM/PROJECT_SYSTEM_STATE.yaml`; `docs/FOUNDATION/PROJECT_STATE.yaml`; `docs/PRODUCT_LAB/LAB_STATE.yaml`.
<!-- SP:CURRENT:END -->

## Active product loop

```text
representative situation
→ perceived position and constraints
→ Selection Point
→ available continuations
→ selected continuation
→ realized / non-realized continuation
→ consequences
→ feedback
→ varied next situation
```

Validation requires a second loop:

```text
simulation
→ bounded real-world experiment
→ factual realization / non-realization
→ real consequence
→ review
→ next simulation
```

## V0 anti-expansion boundary

V0 is deliberately limited to one target capability, 10–15 manually authorable scenarios and one real-world transfer experiment. VR, AI, a platform, gamification and a full curriculum are not prerequisites.

## Project authority

Read in this order for the active route:

1. `docs/PROJECT_SYSTEM/PROJECT_SYSTEM_STATE.yaml`
2. `docs/PROJECT_SYSTEM/RECOVERY_CHECKPOINT_2026-11-03_ENVIRONMENT_FIRST_RESET.md`
3. `docs/PROJECT_SYSTEM/DECISION_ENVIRONMENT_FIRST_RESET_2026-11-03.md`
4. `docs/PRODUCT_LAB/ADAPTIVE_ENVIRONMENT_ARCHITECTURE_V0.md`
5. `docs/PRODUCT_LAB/PRODUCT_THESIS.md`
6. `docs/PROJECT_SYSTEM/PROJECT_CONTROL_PLANE.md`

Foundation authority remains under `docs/FOUNDATION/` and is not silently changed by Product Lab decisions.

## Historical/reference layers

- `docs/COURSE/` — previous course-first route; scenario/content source only unless explicitly reactivated.
- `docs/TRAINING/` — capability, progression, practice and measurement research; reference input, not active Gate progression.
- `docs/CONTENT/` and older prototype material — legacy unless another current manifest explicitly promotes it.

## Consistency

The repository uses strict manifests and generated current-state views. Run:

```bash
python scripts/check_project_consistency.py
python -m unittest discover -s tests
```

The checker must fail if the course-first route silently regains execution authority, if implementation/pilot gates open without an owner decision, if V0 expands past its approved boundary, or if simulator performance is treated as proof of real-world transfer.