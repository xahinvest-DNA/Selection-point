# Reality Check Register

**Статус:** действующий реестр проверок  
**Дата обновления:** 5 сентября 2026 года

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
| RC-013 | SP-S4-P09 | утверждено: amended zero-delta | owner-approved; amended-zero-delta; externally-compatible; externally-limited; pilot-observability-pending; falsifier-defined | Body-state bidirectionality — сквозное свойство. |
| RC-014 | SP-S4-P10 | утверждено | owner-approved; externally-compatible; externally-limited; pilot-observability-pending; falsifier-defined | Устойчивость траектории ≠ неизменность её формы. |
| RC-015 | SP-S4-P11 | утверждено | owner-approved; externally-compatible; externally-limited; pilot-observability-pending; falsifier-defined | Тренировать доступность / re-entry reality-coupled выбора под нагрузкой. |
| RC-016 | SP-S4-P12 | утверждено | owner-approved; externally-compatible; externally-limited; pilot-observability-pending; falsifier-defined | Контекстно-релевантное сохранение + functional re-entry. |
| RC-017 | SP-S4-P13 | **утверждено** | owner-approved; revised; externally-compatible; externally-limited; pilot-observability-pending; falsifier-defined | Moment-level recovery не должен обнулять trajectory-level feedback. |

## RC-017 — закрытый итог

5 сентября 2026 года после temporal-scale refinement, повторного Architect pass, revised Reality Check и revised Red Team Андрей явно утвердил SP-S4-P13 решением:

> **«Утверждаем».**

### Центральный тезис

> **Выбор совершается в моменте. Траектория обнаруживается во времени.**

Ловушка:

> **Полезная способность возвращаться к выбору в каждом отдельном моменте становится ловушкой, если moment-level view превращается в почти единственный масштаб оценки и серия функционально сходных эпизодов не получает достаточного веса как новая фактическая позиция.**

Корректирующая формула:

> **Прошлое не должно определять следующий выбор, но релевантная история должна иметь право изменить описание текущей позиции.**

### External compatibility

- behaviour-maintenance literature различает lapse и relapse / sequence of lapses;
- EMA literature различает fast local processes и slower unfolding/background processes;
- maintenance models требуют учитывать поведение во времени и контекстах;
- context-dependent relapse literature поддерживает возможность влияния устойчивых условий, но не доказывает одну скрытую причину.

### Red Team boundaries

```text
present moment ≠ trap
history = data ≠ verdict / identity / destiny
single lapse ≠ trajectory
series ≠ proof of one cause
aggregation ≠ guilt score
negative outcomes alone ≠ negative trajectory
macro-awareness ≠ total self-monitoring
```

### Falsifier

P13 пересматривается, если temporal aggregation не добавляет practically useful distinction к P12, если временной масштаб неизбежно выбирается post hoc, если macro-review создаёт преимущественно guilt / hyper-control либо если local recovery и trajectory-level feedback практически неразличимы как отдельные функции.

Approval addendum: `RC-017_SP-S4-P13_APPROVAL_ADDENDUM.md`.

## Текущая граница

**RC-017 закрыт как owner-approved. Ступень 4 завершена полностью. SP-S5-P01 не открыт.**
