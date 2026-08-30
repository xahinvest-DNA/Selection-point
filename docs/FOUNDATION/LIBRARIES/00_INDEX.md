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

Внешняя и falsification-проверка вынесена в:

- `../GOVERNANCE/REALITY_CHECK_PROTOCOL.md`;
- `../GOVERNANCE/REALITY_CHECK_REGISTER.md`;
- `../GOVERNANCE/RC-009_SP-S4-P05.md`;
- `../GOVERNANCE/RC-010_SP-S4-P06.md`;
- `../GOVERNANCE/RC-011_SP-S4-P07_ZERO_DELTA.md`;
- `../GOVERNANCE/RC-012_SP-S4-P08.md` — active, owner-decision-pending.

---

## Delta-first

После каждого **утверждённого** параметра создаётся local parameter delta record.

Для обычного параметра он фиксирует новую дельту. Для `zero-delta` он фиксирует проверенный результат отсутствия самостоятельной новой дельты.

Активный, но ещё не утверждённый параметр не получает approved delta заранее.

Плановая консолидация больших реестров выполняется:

- после P05;
- после P10;
- после P13;
- на границе ступени;
- либо по отдельному решению владельца.

29 августа 2026 года после утверждения SP-S4-P05 выполнена плановая консолидация:

- `CLAIMS_REGISTRY.md` — SP-S4-P03–P05;
- `EVIDENCE_MAP.md` — SP-S4-P03–P05;
- `CROSS_REFERENCE_MAP.md` — SP-S4-P03–P05.

SP-S4-P06 добавлен delta-first без внеплановой большой консолидации.

SP-S4-P07 завершён как `zero-delta`; новый claim в большие реестры не добавляется, потому что самостоятельной сущности не введено.

SP-S4-P08 сейчас активен, но не утверждён. Его рабочая гипотеза хранится в Architect / Reality Check слоях, а не в approved libraries.

Следующая плановая консолидация — после P10, если отдельное решение владельца не потребует её раньше.

---

## Текущий охват утверждённого слоя

Библиотеки и approved delta-records покрывают:

- SP-HCM-01–SP-HCM-09;
- SP-S1-P01–SP-S1-P13;
- SP-S2-P01–SP-S2-P13;
- SP-S3-P01–SP-S3-P13;
- SP-S4-P01–SP-S4-P07, где P07 = `zero-delta`;
- SP-VM-01–SP-VM-02.

SP-S4-P08 в этот список **не входит до утверждения**.

---

## Последний завершённый approved delta record

SP-S4-P07:

> **Самостоятельная новая архитектурная дельта «главной боли» S4 не подтверждена.**

Ключевые границы:

```text
zero-delta
≠ отсутствие боли

боль утраты важного будущего
≠ самостоятельная структурная боль S4

принятие реальности
≠ отсутствие чувств
```

Approved full record: `../FIVE_STAGES_THEORY/46_STAGE_4_MAIN_PAIN_ZERO_DELTA.md`.

Canonical-card: не создаётся, потому что нового самостоятельного claim нет.

Reality Check: `../GOVERNANCE/RC-011_SP-S4-P07_ZERO_DELTA.md`.

---

## Active working parameter — SP-S4-P08

Рабочий кандидат находится вне approved library:

- `../SOURCE_MATERIALS/15_2026-08-30_WILLIAMS_MILLMAN_FRITZ_P08_REFLECTION.md`;
- `../GOVERNANCE/SP-S4-P08_ARCHITECT_PASS_NOTES.md`;
- `../GOVERNANCE/RC-012_SP-S4-P08.md`.

До решения владельца:

```text
working P08 delta candidate
≠
approved parameter delta
```

---

## Матрица 5 × 13

Библиотечная инфраструктура не требует искусственного claim для каждой ячейки. Если Reality Check показывает отсутствие самостоятельной дельты, допустим `zero-delta`.

---

## Авторитетный текущий статус

Источник: `../PROJECT_STATE.yaml`.

**Последний утверждённый параметр — SP-S4-P07 (`zero-delta`). SP-S4-P08 активен и ожидает решения владельца. SP-S4-P09 не открыт.**
