# Reality Check Register

**Статус:** действующий реестр проверок  
**Дата обновления:** 4 сентября 2026 года

| ID | Объект | Архитектурный статус | Reality Check status | Итог / следующий шаг |
|---|---|---|---|---|
| RC-001 | SP-HCM-09 | утверждено | external-review-pending; falsifier-defined | Проверить внешний язык до Фазы 4. |
| RC-002 | SP-S3-P13 | утверждено | pilot-observability-pending; falsifier-defined | Проверять реальную пересматриваемость модели. |
| RC-003 | SP-S4-P01 | утверждено | external-review-pending; pilot-observability-pending | «Сформировано, но недоступно» vs «не сформировано». |
| RC-004 | SP-S4-P02 | утверждено | external-review-pending; pilot-observability-pending | Функциональное vs искажённое сужение. |
| RC-005 | Матрица 5×13 | рабочая архитектура | falsifier-defined | Не создавать искусственную дельту. |
| RC-006 | Публичный термин HCM-09 | внутренний канон | revisit-required-before-phase-4 | Terminology review. |
| RC-007 | SP-S4-P03 | утверждено | initial-external-review; pilot-observability-pending; falsifier-defined | Self-model: practically consequential, not essence. |
| RC-008 | SP-S4-P04 | утверждено | initial-external-review; pilot-observability-pending; falsifier-defined | Организующий приоритет ≠ оперативный приоритет. |
| RC-009 | SP-S4-P05 | утверждено | owner-approved; externally-compatible; externally-limited; pilot-observability-pending; falsifier-defined | Объективно один ход ≠ потеря выбора. |
| RC-010 | SP-S4-P06 | утверждено | owner-approved; externally-compatible; externally-limited; pilot-observability-pending; falsifier-defined | Сформированная способность ≠ гарантированная доступность. |
| RC-011 | SP-S4-P07 | утверждено: zero-delta | owner-approved; zero-delta; externally-compatible; falsifier-defined | Отдельная S4-боль не подтверждена. |
| RC-012 | SP-S4-P08 | утверждено | owner-approved; externally-compatible; externally-limited; pilot-observability-pending; falsifier-defined | Восстанавливать участие из фактической доступности. |
| RC-013 | SP-S4-P09 | утверждено: amended zero-delta | owner-approved; amended-zero-delta; externally-compatible; externally-limited; pilot-observability-pending; falsifier-defined | Body-state bidirectionality — сквозное свойство, не S4-specific delta. |
| RC-014 | SP-S4-P10 | утверждено | owner-approved; externally-compatible; externally-limited; pilot-observability-pending; falsifier-defined | Устойчивость траектории ≠ неизменность её формы. |
| RC-015 | SP-S4-P11 | утверждено | owner-approved; externally-compatible; externally-limited; pilot-observability-pending; falsifier-defined | Тренировать доступность / re-entry reality-coupled выбора под нагрузкой, а не toughness или relaxation. |
| RC-016 | SP-S4-P12 | утверждено | owner-approved; externally-compatible; externally-limited; pilot-observability-pending; falsifier-defined | Контекстно-релевантное сохранение + functional re-entry; не universal stress resilience. |

## RC-016 — закрытый итог

4 сентября 2026 года после Architect pass, Reality Check и Red Team Андрей явно утвердил SP-S4-P12 решением:

> **«Утверждаем».**

Утверждённый центральный тезис:

> **Переход от S4 становится обоснованным, когда в конкретной области способность участия качественно достаточно надёжна при некоторой вариативности релевантной нагрузки: иногда сохраняется непосредственно внутри нагрузки, а после реального снижения доступности человек способен самостоятельно изменить ещё доступное продолжение из новой фактической позиции.**

Короткая формула:

> **Не непрерывный контроль, а достаточно надёжное сохранение и функциональное возвращение выбора под релевантной нагрузкой.**

### Ключевые ограничения

```text
late understanding ≠ functional re-entry
natural recovery ≠ own recovery operation
one rehearsed stressor ≠ sufficient transfer
support scaffold ≠ external operator of choice
хороший исход ≠ P12
recovery speed ≠ maturity
S4 mastery ≠ universal stress resilience
```

### Falsifier

P12 пересматривается, если в пилоте нельзя отличить functional re-entry от natural recovery, если релевантную нагрузку невозможно определять prospectively, если критерий подтверждается любым исходом post hoc, если собственная операция неотличима от внешнего управления либо если граница S4→S5 не добавляет practically useful distinction.

Approval addendum: `RC-016_SP-S4-P12_APPROVAL_ADDENDUM.md`.

## Текущая граница

**RC-016 закрыт как owner-approved. SP-S4-P12 утверждён. SP-S4-P13 не открыт.**
