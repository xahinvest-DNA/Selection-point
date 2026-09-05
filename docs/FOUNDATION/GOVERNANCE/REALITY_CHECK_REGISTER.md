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
| RC-017 | SP-S4-P13 | на обсуждении | revised; externally-compatible; externally-limited; pilot-observability-pending; falsifier-defined; owner-decision-pending | Moment-level recovery может недоучитывать trajectory-level feedback. |

## RC-017 — revised open result

5 сентября 2026 года после первого Architect / RC-017 / Red Team Андрей уточнил P13 через временной масштаб. На этом основании Architect pass, Reality Check и Red Team пересобраны.

### Surviving candidate

> **Ловушка S4 возникает, когда полезная способность возвращаться к доступному выбору в каждом отдельном моменте непреднамеренно превращает moment-level view в основной и почти единственный масштаб оценки. Тогда серия функционально сходных эпизодов может не получить достаточного веса как новая фактическая позиция, и человек локально остаётся в выборе, одновременно недооценивая устойчивое изменение собственной траектории во времени.**

Короткая формула:

> **Выбор совершается в моменте. Ошибка — считать момент достаточным масштабом для оценки траектории.**

Корректирующая:

> **Прошлое не определяет следующий выбор, но релевантная история должна иметь право изменить описание текущей позиции.**

### External compatibility

- behaviour-maintenance literature различает lapse и relapse / sequence of lapses;
- EMA literature различает fast local processes и slower unfolding/background processes;
- maintenance models требуют учитывать поведение во времени и контекстах;
- context-dependent relapse literature показывает, что повторение может зависеть от устойчивых условий, но не доказывает одну скрытую причину.

### Red Team boundaries

```text
present moment ≠ problem
past = data ≠ verdict / identity / destiny
single lapse ≠ trajectory
series ≠ proof of one cause
aggregation ≠ guilt score
negative outcomes alone ≠ negative trajectory
macro-awareness ≠ total self-monitoring
```

### Zero-delta / falsification condition

P13 должен быть пересмотрен или признан `zero-delta`, если temporal aggregation не добавляет practically useful distinction к P12, если временное окно неизбежно выбирается post hoc, если macro-review создаёт в основном guilt / hyper-control либо если невозможно наблюдаемо показать случай, где local recovery работает, но trajectory-level feedback систематически недоучитывается.

Связанные файлы:
- `SP-S4-P13_ARCHITECT_PASS_NOTES.md`;
- `RC-017_SP-S4-P13.md`;
- `SP-S4-P13_RED_TEAM_NOTES.md`;
- `../SOURCE_MATERIALS/25_2026-09-05_P13_TEMPORAL_SCALE_AND_TRAJECTORY.md`;
- `../SOURCE_MATERIALS/24_2026-09-05_P13_COMPENSATION_THINKING_AND_REALITY_CONTACT.md`.

## Текущая граница

**SP-S4-P13 повторно прошёл Architect pass, RC-017 и Red Team после temporal-scale refinement; ожидается явное решение владельца.**
