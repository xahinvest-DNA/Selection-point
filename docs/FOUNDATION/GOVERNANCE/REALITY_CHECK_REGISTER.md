# Reality Check Register

**Статус:** действующий реестр проверок  
**Дата обновления:** 15 сентября 2026 года

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
| RC-017 | SP-S4-P13 | утверждено | owner-approved; revised; externally-compatible; externally-limited; pilot-observability-pending; falsifier-defined | Moment-level recovery не должен обнулять trajectory-level feedback. |
| RC-018 | Core boundary: choice → realized continuation → feedback | **утверждено** | owner-approved; externally-compatible; externally-limited; pilot-observability-pending; falsifier-defined | Выбранное продолжение ≠ фактически реализованное; feedback относится к реально произошедшему. |

## RC-017 — закрытый итог

5 сентября 2026 года после temporal-scale refinement, повторного Architect pass, revised Reality Check и revised Red Team Андрей явно утвердил SP-S4-P13.

> **Выбор совершается в моменте. Траектория обнаруживается во времени.**

> **Прошлое не должно определять следующий выбор, но релевантная история должна иметь право изменить описание текущей позиции.**

Approval addendum: `RC-017_SP-S4-P13_APPROVAL_ADDENDUM.md`.

## RC-018 — закрытый итог

15 сентября 2026 года после Architect pass, RC-018 Reality Check и Red Team Андрей явно утвердил сквозную boundary решением:

> **«Утверждаем».**

### Центральный тезис

> **Selection Point должен различать внутренне выбранное и фактически реализованное продолжение. Несовпадение между ними — данные о процессе исполнения, а не моральный провал. Обратную связь о последствиях конкретного действия нельзя приписывать этому действию, если оно не произошло; при этом реальность может дать другие данные — о неисполнении, частичном исполнении, сознательной паузе или пересмотре решения.**

Коротко:

> **Выбрать ≠ сделать. Сделать ≠ получить желаемое. Последствия ≠ автоматически использованная обратная связь.**

### External compatibility

- intention–behavior literature подтверждает устойчивый gap между намерением и поведением;
- Rubicon Model функционально разводит decision / planning / actional phases;
- implementation intentions работают именно как мост от намерения к запуску поведения;
- feedback research связывает коррекцию с данными о фактическом поведении и его последствиях;
- sequential decision research ограничивает сильный вывод: реализованный ход не гарантирует однозначного causal feedback при delayed/noisy outcomes.

### Red Team boundaries

```text
internal choice = real event
≠ proof of execution

selected ≠ realized
≠ автоматически sabotage / weak will

conscious pause / non-action
может быть realized continuation

partial execution
→ only partial test

action
≠ guaranteed clear causal feedback
```

### Архитектурный итог

RC-018 утверждён как **cross-cutting clarification / boundary**, не как новый SP-HCM-10.

Утверждённые слои:
- `../CORE_CHOICE_ACTION_FEEDBACK_BOUNDARY.md`;
- `../CANONICAL/01B_CORE_CHOICE_ACTION_FEEDBACK_BOUNDARY_CANONICAL.md`;
- `../LIBRARIES/CORE_CHOICE_ACTION_FEEDBACK_BOUNDARY_DELTA.md`;
- `RC-018_CORE_CHOICE_ACTION_FEEDBACK_APPROVAL_ADDENDUM.md`.

Approval addendum: `RC-018_CORE_CHOICE_ACTION_FEEDBACK_APPROVAL_ADDENDUM.md`.

## Текущая граница

**RC-018 закрыт как owner-approved. Ступень 4 завершена. SP-S5-P01 остаётся unopened.**
