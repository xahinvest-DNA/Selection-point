# Reality Check Register

**Статус:** действующий реестр проверок  
**Дата введения:** 28 августа 2026 года  
**Дата обновления:** 30 августа 2026 года

Назначение реестра — показывать очередь, итог и дальнейший статус Reality Check. Полная аргументация хранится в отдельных `RC-*` файлах и связанных Architect pass notes.

## Реестр

| ID | Объект | Архитектурный статус | Reality Check status | Итог / следующий шаг |
|---|---|---|---|---|
| RC-001 | SP-HCM-09 | утверждено | external-review-pending; falsifier-defined | Проверить внешний язык «создание собственной реальности» до Фазы 4. |
| RC-002 | SP-S3-P13 | утверждено | pilot-observability-pending; falsifier-defined | Проверять реальную пересматриваемость модели на эпизодах. |
| RC-003 | SP-S4-P01 | утверждено | external-review-pending; pilot-observability-pending | Проверять различие «сформировано, но недоступно» vs «не сформировано». |
| RC-004 | SP-S4-P02 | утверждено | external-review-pending; pilot-observability-pending | Проверять функциональное vs искажённое сужение восприятия. |
| RC-005 | Матрица 5 × 13 | рабочая архитектура | falsifier-defined | Не создавать искусственную дельту ради заполнения ячейки. |
| RC-006 | Публичный термин HCM-09 | внутренний канон | revisit-required-before-phase-4 | Провести terminology/public-language review. |
| RC-007 | SP-S4-P03 | утверждено | initial-external-review; pilot-observability-pending; falsifier-defined | Самостоятельная дельта сохранена: важен практический вес self-model, не сам self-language. |
| RC-008 | SP-S4-P04 | утверждено | initial-external-review; pilot-observability-pending; falsifier-defined | Самостоятельная дельта сохранена: организующий приоритет ≠ оперативный приоритет. |
| RC-009 | SP-S4-P05 | утверждено | owner-approved; externally-compatible; externally-limited; pilot-observability-pending; falsifier-defined | Объективно один ход ≠ потеря выбора; не универсализировать телесные маркеры. |
| RC-010 | SP-S4-P06 | утверждено | owner-approved; externally-compatible; externally-limited; pilot-observability-pending; falsifier-defined | Сформированная способность ≠ гарантированная доступность. |
| RC-011 | SP-S4-P07 | утверждено: zero-delta | owner-approved; zero-delta; externally-compatible; falsifier-defined | Самостоятельная структурная «главная боль» S4 не подтверждена. |
| RC-012 | SP-S4-P08 | утверждено | owner-approved; externally-compatible; externally-limited; pilot-observability-pending; falsifier-defined | Утверждён stage-specific навык восстановления участия из фактической доступности. |
| RC-013 | SP-S4-P09 | утверждено: amended zero-delta | owner-approved; amended-zero-delta; externally-compatible; externally-limited; pilot-observability-pending; falsifier-defined | Body-state bidirectionality сохранена как сквозное свойство; отдельная S4-specific телесная дельта не подтверждена. |

## Закрытые / текущие полные записи

- `RC-009_SP-S4-P05.md` — P05, owner-approved.
- `RC-010_SP-S4-P06.md` — P06, owner-approved.
- `RC-011_SP-S4-P07_ZERO_DELTA.md` — P07, owner-approved zero-delta.
- `RC-012_SP-S4-P08.md` + `RC-012_SP-S4-P08_APPROVAL_ADDENDUM.md` — P08, owner-approved.
- `RC-013_SP-S4-P09.md` — первый Reality Check P09.
- `RC-013_SP-S4-P09_REANALYSIS_ADDENDUM.md` — повторный Reality Check после контрпримера владельца.
- `RC-013_SP-S4-P09_APPROVAL_ADDENDUM.md` — P09, owner-approved amended zero-delta.

## RC-013 — закрытый итог

Первый Reality Check установил:

```text
напряжение ≠ потеря выбора
спокойствие ≠ наличие выбора
```

Контрпример владельца затем показал необходимость исправить слишком пассивную трактовку тела:

```text
внутреннее состояние
→ мимика / поза / движения
```

и:

```text
намеренное изменение телесной организации
или внутреннего образа
→ может изменить внутреннее состояние
```

Повторный внешний обзор поддержал ограниченную причинную двусторонность для facial feedback, posture, respiration и mental imagery.

Утверждённая системная граница:

```text
тело
= часть текущей позиции
+
может быть причинным участником дальнейшей динамики
```

Но:

```text
body-state bidirectionality
≠ unique S4 mechanism
```

Поэтому 30 августа 2026 года после второго Red Team Андрей явно утвердил:

> **SP-S4-P09 — amended `zero-delta`.**

Короткая формула:

> **Тело не только показывает позицию — оно участвует в её изменении. Но это не отдельная S4-дельта.**

Дополнительные предохранители:

```text
body change can influence state
≠ guarantees state change
```

```text
state improvement
≠ choice restored
```

```text
body-state bidirectionality
≠ S4-specific delta
```

Intentional bodily leverage передан как кандидат функционального класса P11. Возможное явное представление body-state bidirectionality в HCM отложено до Whole-System Review.

## Правила

- внутренняя утверждённость не равна внешней научной доказанности;
- внешнее сходство не означает тождества;
- контрпример проверяется против области применимости и центрального тезиса;
- `zero-delta` является допустимым результатом;
- реестр обновляется при каждом meaningful Reality Check;
- следующий параметр не открывается до отдельного запуска по протоколу.
