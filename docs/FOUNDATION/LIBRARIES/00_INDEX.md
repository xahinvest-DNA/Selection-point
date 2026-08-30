# Общие библиотеки Selection Point

**Статус:** действующая инфраструктура канонического слоя  
**Дата введения:** 4 июля 2026 года  
**Дата обновления:** 30 августа 2026 года

## Состав

1. `TERMS_REGISTRY.md` — единые определения терминов со стабильными ID.
2. `CLAIMS_REGISTRY.md` — консолидированный индекс утверждённых claims.
3. `EXAMPLE_LIBRARY.md` — переиспользуемые примеры.
4. `RISKS_AND_BOUNDARIES.md` — централизованные риски и ограничения.
5. `EVIDENCE_MAP.md` — консолидированная карта доказательного статуса.
6. `CROSS_REFERENCE_MAP.md` — консолидированная карта связей.
7. `P13_STAGE_TRAP_DELTA.md` — историческая дельта SP-S3-P13.
8. `S4_P01_STATE_DELTA.md` — дельта SP-S4-P01.
9. `S4_P02_REALITY_PERCEPTION_DELTA.md` — дельта SP-S4-P02.
10. `S4_P03_SELF_PERCEPTION_DELTA.md` — дельта SP-S4-P03.
11. `S4_P04_DECISION_DRIVERS_DELTA.md` — дельта SP-S4-P04.
12. `S4_P05_AVAILABLE_POINT_OF_CHOICE_DELTA.md` — дельта SP-S4-P05.
13. `S4_P06_MAIN_ILLUSION_DELTA.md` — дельта SP-S4-P06.
14. `S4_P07_MAIN_PAIN_ZERO_DELTA.md` — утверждённый zero-delta record SP-S4-P07.
15. `S4_P08_NEXT_SKILL_DELTA.md` — утверждённая дельта SP-S4-P08.

Внешняя и falsification-проверка вынесена в:

- `../GOVERNANCE/REALITY_CHECK_PROTOCOL.md`;
- `../GOVERNANCE/REALITY_CHECK_REGISTER.md`;
- `../GOVERNANCE/RC-009_SP-S4-P05.md`;
- `../GOVERNANCE/RC-010_SP-S4-P06.md`;
- `../GOVERNANCE/RC-011_SP-S4-P07_ZERO_DELTA.md`;
- `../GOVERNANCE/RC-012_SP-S4-P08.md`;
- `../GOVERNANCE/RC-012_SP-S4-P08_APPROVAL_ADDENDUM.md`.

---

## Delta-first

После каждого утверждённого параметра создаётся local parameter delta record.

Плановая консолидация больших реестров выполняется:

- после P05;
- после P10;
- после P13;
- на границе ступени;
- либо по отдельному решению владельца.

29 августа 2026 года после утверждения SP-S4-P05 выполнена плановая консолидация `CLAIMS_REGISTRY.md`, `EVIDENCE_MAP.md` и `CROSS_REFERENCE_MAP.md`.

SP-S4-P06, P07 и P08 добавлены delta-first без внеплановой большой консолидации. Для P07 новый claim не создавался, потому что параметр утверждён как `zero-delta`.

Следующая плановая консолидация — после P10, если отдельное решение владельца не потребует её раньше.

---

## Текущий охват утверждённого слоя

Библиотеки и approved delta-records покрывают:

- SP-HCM-01–SP-HCM-09;
- SP-S1-P01–SP-S1-P13;
- SP-S2-P01–SP-S2-P13;
- SP-S3-P01–SP-S3-P13;
- SP-S4-P01–SP-S4-P08, где P07 = `zero-delta`;
- SP-VM-01–SP-VM-02.

---

## Последний завершённый approved delta record — SP-S4-P08

> **Следующий навык четвёртой ступени — способность восстанавливать функциональное участие из фактической степени текущей доступности после того, как под нагрузкой уменьшился доступ к уже сформированной способности выбора.**

Коротко:

> **Восстанавливать участие из фактической доступности.**

Ключевые границы:

```text
восстановить участие
≠
сначала полностью восстановить прежнее состояние

полное прежнее состояние не всегда нужно
≠
состояние никогда не нужно восстанавливать

больше вариантов
≠
больше зрелости
```

Approved full record: `../FIVE_STAGES_THEORY/47_STAGE_4_NEXT_SKILL.md`.

Canonical: `../CANONICAL/38_STAGE_4_P08_CANONICAL.md`.

Reality Check: `../GOVERNANCE/RC-012_SP-S4-P08.md`.

Owner approval: `../GOVERNANCE/RC-012_SP-S4-P08_APPROVAL_ADDENDUM.md`.

---

## Матрица 5 × 13

Библиотечная инфраструктура не требует искусственного claim для каждой ячейки. Если самостоятельной practically useful дельты нет, допустим `zero-delta`.

---

## Авторитетный текущий статус

Источник: `../PROJECT_STATE.yaml`.

**SP-S4-P08 утверждён. SP-S4-P09 не открыт.**
