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
8. `S4_P01_STATE_DELTA.md`.
9. `S4_P02_REALITY_PERCEPTION_DELTA.md`.
10. `S4_P03_SELF_PERCEPTION_DELTA.md`.
11. `S4_P04_DECISION_DRIVERS_DELTA.md`.
12. `S4_P05_AVAILABLE_POINT_OF_CHOICE_DELTA.md`.
13. `S4_P06_MAIN_ILLUSION_DELTA.md`.
14. `S4_P07_MAIN_PAIN_ZERO_DELTA.md` — утверждённый zero-delta P07.
15. `S4_P08_NEXT_SKILL_DELTA.md` — утверждённая дельта P08.
16. `S4_P09_BODY_MANIFESTATIONS_ZERO_DELTA.md` — утверждённый amended zero-delta P09.

## Reality Check links

- `../GOVERNANCE/RC-009_SP-S4-P05.md`;
- `../GOVERNANCE/RC-010_SP-S4-P06.md`;
- `../GOVERNANCE/RC-011_SP-S4-P07_ZERO_DELTA.md`;
- `../GOVERNANCE/RC-012_SP-S4-P08.md`;
- `../GOVERNANCE/RC-012_SP-S4-P08_APPROVAL_ADDENDUM.md`;
- `../GOVERNANCE/RC-013_SP-S4-P09.md`;
- `../GOVERNANCE/RC-013_SP-S4-P09_REANALYSIS_ADDENDUM.md`;
- `../GOVERNANCE/RC-013_SP-S4-P09_APPROVAL_ADDENDUM.md`.

---

## Delta-first

После каждого утверждённого параметра создаётся local parameter delta record. Для `zero-delta` record фиксирует отсутствие новой сущности и обязательные границы.

Плановая консолидация больших реестров выполняется:

- после P05;
- после P10;
- после P13;
- на границе ступени;
- либо по отдельному решению владельца.

29 августа 2026 года после P05 выполнена плановая консолидация `CLAIMS_REGISTRY.md`, `EVIDENCE_MAP.md` и `CROSS_REFERENCE_MAP.md`.

P06–P09 добавлены delta-first без внеплановой большой консолидации. P07 и P09 утверждены как `zero-delta` и не создают новый самостоятельный canonical claim.

Следующая плановая консолидация — после P10.

---

## Текущий охват утверждённого слоя

Библиотеки и approved delta-records покрывают:

- SP-HCM-01–SP-HCM-09;
- SP-S1-P01–SP-S1-P13;
- SP-S2-P01–SP-S2-P13;
- SP-S3-P01–SP-S3-P13;
- SP-S4-P01–SP-S4-P09, где P07 и P09 = `zero-delta`;
- SP-VM-01–SP-VM-02.

---

## Последний завершённый approved delta record — SP-S4-P09

Тип:

> **amended `zero-delta`.**

Утверждённый смысл:

> **На четвёртой ступени тело остаётся значимой частью фактической текущей позиции и может участвовать в изменении состояния и доступности действия, но отдельный новый класс телесных проявлений S4 не подтверждён.**

Коротко:

> **Тело не только показывает позицию — оно участвует в её изменении. Но это не отдельная S4-дельта.**

Ключевые границы:

```text
телесный сигнал = данные
≠ только данные

изменение тела может влиять на состояние
≠ гарантирует изменение состояния

улучшение состояния
≠ восстановление выбора

body-state bidirectionality
≠ unique S4 mechanism
```

Intentional bodily leverage сохранён как кандидат функционального класса для P11.

Full approved record: `../FIVE_STAGES_THEORY/48_STAGE_4_BODY_MANIFESTATIONS_ZERO_DELTA.md`.

Reality Check: `../GOVERNANCE/RC-013_SP-S4-P09.md`.

Owner approval: `../GOVERNANCE/RC-013_SP-S4-P09_APPROVAL_ADDENDUM.md`.

---

## Матрица 5 × 13

Библиотечная инфраструктура не требует искусственного claim для каждой ячейки. Если самостоятельной practically useful дельты нет, допустим `zero-delta`.

---

## Авторитетный текущий статус

Источник: `../PROJECT_STATE.yaml`.

**SP-S4-P09 утверждён. SP-S4-P10 не открыт.**
