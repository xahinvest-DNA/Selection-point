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
| RC-016 | SP-S4-P12 | на обсуждении | externally-compatible; externally-limited; pilot-observability-pending; falsifier-defined; owner-decision-pending | Контекстно-релевантное сохранение + функциональный re-entry; не universal stress resilience. |

## RC-015 — закрытый итог

3 сентября 2026 года после Architect pass / Reality Check / Red Team Андрей явно утвердил SP-S4-P11 решением:

> **«Утверждаем».**

Утверждённый центральный тезис:

> **Практики четвёртой ступени должны тренировать не отдельную технику успокоения или самоконтроля, а доступность reality-coupled цикла выбора под нагрузкой: распознавать сам режим нагрузки и возможное снижение доступности, возвращать достаточную рабочую ориентацию в текущей позиции, масштабировать участие по фактам, использовать подходящий доступный вход для изменения состояния или условий, совершать реально доступный ход и получать обратную связь, способную скорректировать следующий цикл. Практика должна включать не только сохранение выбора, но и повторный вход после частичного снижения доступности.**

Коротко:

> **Тренировать цикл выбора под нагрузкой, а не отдельную технику снятия нагрузки.**

### Функциональные классы

1. load recognition;
2. relevant reorientation;
3. graded / context-relevant load;
4. available entry;
5. functional move;
6. reality-coupled feedback;
7. recovery / re-entry.

### External compatibility

Stress-inoculation, graduated simulation, situation-awareness, deliberate-practice/feedback и motor-imagery literature содержательно совместимы с отдельными компонентами и одновременно ограничивают формулы «максимум стресса лучше», «тотальный мониторинг полезен» и `imagery = sufficient practice`. Они не доказывают пятиступенчатую архитектуру Selection Point.

### Red Team boundaries

```text
«вся панель» ≠ тотальный self-monitoring
выдержать больше стресса ≠ больше выбора
load-awareness ≠ доказательство фактической потери выбора
снижение возбуждения ≠ восстановление выбора
objective feedback ≠ обязательно мгновенный KPI
visualization may help ≠ sufficient reality-coupled verification
```

### Falsifier

P11 пересматривается / схлопывается в S3-P11, если load-specific training не добавляет practically useful distinction, если «панель» неизбежно создаёт hyper-control, если reality feedback нельзя сохранить без ложной объективизации, или если в пилоте нельзя отличить расширение доступности выбора от простого привыкания терпеть стресс.

Approval addendum: `RC-015_SP-S4-P11_APPROVAL_ADDENDUM.md`.

## RC-016 — открытый итог

4 сентября 2026 года для SP-S4-P12 завершены Architect pass, Reality Check и Red Team. Параметр ещё не утверждён владельцем.

### Сохранившийся центральный кандидат

> **Переход не требует непрерывного контроля или отсутствия выпадений. В конкретной области способность должна быть качественно достаточно надёжна при некоторой вариативности релевантной нагрузки: иногда сохраняться непосредственно внутри нагрузки, а после реального снижения доступности — позволять человеку самостоятельно изменить ещё продолжающуюся траекторию из новой фактической позиции.**

### External compatibility

- behaviour-maintenance literature различает lapse / relapse и отдельно описывает recovery self-efficacy;
- resilience literature поддерживает динамическое восстановление, а не отсутствие реакции как единственный образ устойчивости;
- regulatory-flexibility literature поддерживает context sensitivity и feedback responsiveness;
- training-transfer literature ограничивает генерализацию: перенос на новые условия не автоматичен;
- habit/context literature поддерживает влияние системы условий на вероятность поведения, но не доказывает отдельную S5.

### Ключевые ограничения Red Team

```text
позднее понимание ≠ functional re-entry
natural recovery ≠ собственная операция восстановления участия
один отрепетированный стрессор ≠ достаточный transfer
support scaffold ≠ внешний оператор выбора
хороший исход ≠ P12
быстрое восстановление ≠ автоматически зрелость
S5 systemic task ≠ запрет менять среду раньше
```

### Falsifier

P12 пересматривается, если в пилоте нельзя отличить re-entry от natural recovery, если релевантную нагрузку невозможно выбирать prospectively, если критерий подтверждается только post hoc storytelling, если поддержка и собственная операция не различимы либо если S4→S5 boundary не добавляет practically useful distinction.

Связанные файлы:
- `RC-016_SP-S4-P12.md`;
- `SP-S4-P12_RED_TEAM_NOTES.md`.

## Текущая граница

**SP-S4-P12 прошёл Architect pass, RC-016 и Red Team; ожидается явное решение владельца. SP-S4-P13 не открыт.**
