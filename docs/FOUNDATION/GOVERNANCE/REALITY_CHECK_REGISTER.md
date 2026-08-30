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
| RC-013 | SP-S4-P09 | активен | reanalysis-complete; amended-zero-delta-recommended; externally-compatible; externally-limited; pilot-observability-pending; falsifier-defined; owner-decision-pending | Body-state bidirectionality подтверждена как сквозное свойство, но не как уникальная S4-дельта; вынести владельцу amended zero-delta recommendation. |

## Закрытые / текущие полные записи

- `RC-009_SP-S4-P05.md` — P05, owner-approved.
- `RC-010_SP-S4-P06.md` — P06, owner-approved.
- `RC-011_SP-S4-P07_ZERO_DELTA.md` — P07, owner-approved zero-delta.
- `RC-012_SP-S4-P08.md` + `RC-012_SP-S4-P08_APPROVAL_ADDENDUM.md` — P08, owner-approved.
- `RC-013_SP-S4-P09.md` — первый Reality Check P09.
- `RC-013_SP-S4-P09_REANALYSIS_ADDENDUM.md` — повторный Reality Check после контрпримера владельца о двусторонности body-state; active; owner-decision-pending.

## RC-011 — краткий итог

> **На четвёртой ступени может присутствовать сильная человеческая боль, но отдельная новая структурная «главная боль», специфичная именно для этой ступени, не подтверждена.**

```text
боль утраты значимого будущего
≠
самостоятельная структурная боль S4
```

## RC-012 — краткий итог

> **Восстанавливать участие из фактической доступности.**

```text
восстановить участие
≠
сначала полностью восстановить прежнее состояние
```

P08 не заявляется как новый универсальный психологический механизм; pilot-observability и falsifier остаются действующими.

## RC-013 — итог после повторного анализа

Первый Reality Check установил:

```text
напряжение ≠ потеря выбора
спокойствие ≠ наличие выбора
```

После этого владелец привёл контрпример:

```text
внутреннее состояние
→ мимика / поза / движения
```

и:

```text
намеренное изменение мимики / телесной организации
или внутреннего образа
→ может изменить внутреннее состояние
```

Повторный внешний обзор поддержал причинную двусторонность для ряда каналов:

- facial feedback: эффект существует, но в среднем мал / heterogeneous; preregistered Many Smiles поддержал voluntary facial action и mimicry;
- posture: отдельные randomized studies показывают effects on affect/stress response, но effects контекстны и могут зависеть от individual embodiment;
- respiration: breathing ↔ emotion/cognition имеет reciprocal neural/physiological links;
- mental imagery: может причинно менять affect, но является не чисто телесным, а внутренне-перцептивным входом.

Это исправляет слишком пассивную формулу:

```text
тело = только индикатор
```

Корректнее:

```text
тело
= часть текущей позиции
+
один из причинных участников дальнейшей динамики
```

Однако stage-specificity attack сохраняется:

```text
body-state bidirectionality
≠ уникальный механизм S4
```

Она является сквозным свойством системы и частично уже содержится в HCM-02 / S1-P09 / S3-P09.

Intentional bodily leverage:

```text
изменить телесный компонент
→ попытаться изменить состояние / доступность
```

является кандидатом функционального класса для P11, а не новым «телесным проявлением» P09.

Текущая рекомендация:

> **SP-S4-P09 — amended `zero-delta`: отдельная новая телесная структура S4 не подтверждена, но обязательной сквозной границей становится признание тела активным участником, а не только отражением внутренней позиции.**

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

До явного решения владельца `internal-approved` отсутствует.

## Правила

- внутренняя утверждённость не равна внешней научной доказанности;
- внешнее сходство не означает тождества;
- контрпример проверяется против области применимости и центрального тезиса;
- `zero-delta` является допустимым результатом;
- реестр обновляется при каждом meaningful Reality Check;
- следующий параметр не открывается до завершения текущего governance cycle.
