# Общие библиотеки Selection Point

**Статус:** действующая инфраструктура канонического слоя  
**Дата обновления:** 15 сентября 2026 года

## Approved local records

- `P13_STAGE_TRAP_DELTA.md`;
- `S4_P01_STATE_DELTA.md`;
- `S4_P02_REALITY_PERCEPTION_DELTA.md`;
- `S4_P03_SELF_PERCEPTION_DELTA.md`;
- `S4_P04_DECISION_DRIVERS_DELTA.md`;
- `S4_P05_AVAILABLE_POINT_OF_CHOICE_DELTA.md`;
- `S4_P06_MAIN_ILLUSION_DELTA.md`;
- `S4_P07_MAIN_PAIN_ZERO_DELTA.md`;
- `S4_P08_NEXT_SKILL_DELTA.md`;
- `S4_P09_BODY_MANIFESTATIONS_ZERO_DELTA.md`;
- `S4_P10_LIFE_MANIFESTATIONS_DELTA.md`;
- `S4_P11_CORRESPONDING_PRACTICES_DELTA.md`;
- `S4_P12_TRANSITION_CRITERIA_DELTA.md`;
- `S4_P13_STAGE_TRAP_DELTA.md`;
- `CORE_CHOICE_ACTION_FEEDBACK_BOUNDARY_DELTA.md` — RC-018 cross-cutting boundary.

Основные консолидированные библиотеки: `TERMS_REGISTRY.md`, `CLAIMS_REGISTRY.md`, `EXAMPLE_LIBRARY.md`, `RISKS_AND_BOUNDARIES.md`, `EVIDENCE_MAP.md`, `CROSS_REFERENCE_MAP.md`.

## Исследовательские кейсы

- `CASE_KOMASHNYA_CLOSED_MODEL_2026-09-01.md` — потенциальное замыкание мировоззренческой модели.
- `CASE_TASK_VS_DIRECTION_FLEXIBILITY_2026-09-01.md` — различие настойчивости и ригидности.

## Delta-first и консолидация

Local parameter delta создаётся только после явного утверждения параметра. Cross-cutting boundary получает отдельную delta после явного owner approval, если добавляет practically useful distinction без создания искусственного нового механизма.

Плановая консолидация на границе P13 / Ступени 4 **выполнена 5 сентября 2026 года**:

- `CLAIMS_REGISTRY.md` — SP-S4-P13 + завершение S4;
- `CROSS_REFERENCE_MAP.md` — связи P11–P13 и граница S4→S5;
- `EVIDENCE_MAP.md` — RC-015–RC-017 и evidence boundaries;
- `RISKS_AND_BOUNDARIES.md` — добавлен SP-RISK-030.

15 сентября 2026 года дополнительно утверждена cross-cutting boundary RC-018. До следующей большой консолидации её действующий reusable meaning хранится в `CORE_CHOICE_ACTION_FEEDBACK_BOUNDARY_DELTA.md` и canonical-card.

## RC-018 — choice / realization / feedback

> **Внутренне выбранное продолжение не равно фактически реализованному продолжению.**

```text
выбрать ≠ сделать
сделать ≠ получить желаемое
последствия ≠ автоматически использованная обратная связь
```

Практическая дельта:

```text
Что выбрано?
≠
Что фактически произошло?
```

Несовпадение между ними сначала является данными о процессе исполнения, а не доказательством слабости, саботажа или морального провала.

Full foundation: `../CORE_CHOICE_ACTION_FEEDBACK_BOUNDARY.md`.  
Canonical: `../CANONICAL/01B_CORE_CHOICE_ACTION_FEEDBACK_BOUNDARY_CANONICAL.md`.  
Reality Check: `../GOVERNANCE/RC-018_CORE_CHOICE_ACTION_FEEDBACK.md`.  
Approval: `../GOVERNANCE/RC-018_CORE_CHOICE_ACTION_FEEDBACK_APPROVAL_ADDENDUM.md`.

## SP-S4-P13

> **Выбор совершается в моменте. Траектория обнаруживается во времени.**

Утверждённая trap-delta:

> **Полезная способность нового выбора в моменте может стать ловушкой, если moment-level view превращается в почти единственный масштаб оценки и accumulated series-level feedback перестаёт менять current position.**

RC-018 добавляет:

> **Внутренние выборы показывают направление намерения; фактически реализованные продолжения участвуют в построении фактической траектории.**

```text
history = data ≠ verdict
single lapse ≠ trajectory
series ≠ proof of one cause
macro review ≠ total self-monitoring
aggregation ≠ guilt scoreboard
selected ≠ automatically realized
```

Full theory: `../FIVE_STAGES_THEORY/52_STAGE_4_STAGE_TRAP.md`.  
Canonical: `../CANONICAL/42_STAGE_4_P13_CANONICAL.md`.  
Reality Check: `../GOVERNANCE/RC-017_SP-S4-P13.md`.

## Текущий approved scope

- SP-HCM-01–SP-HCM-09;
- RC-018 cross-cutting choice/action/feedback boundary;
- SP-S1-P01–P13;
- SP-S2-P01–P13;
- SP-S3-P01–P13;
- SP-S4-P01–P13, где P07 = `zero-delta`, P09 = `amended zero-delta`;
- SP-VM-01–SP-VM-02.

**Ступень 4 завершена. RC-018 утверждён. SP-S5-P01 не открыт.**
