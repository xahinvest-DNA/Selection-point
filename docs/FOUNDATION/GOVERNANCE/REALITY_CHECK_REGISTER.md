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
| RC-013 | SP-S4-P09 | утверждено: amended zero-delta | owner-approved; amended-zero-delta; externally-compatible; externally-limited; pilot-observability-pending; falsifier-defined | Body-state bidirectionality — сквозное свойство, не S4-specific delta. |
| RC-014 | SP-S4-P10 | утверждено | owner-approved; externally-compatible; externally-limited; pilot-observability-pending; falsifier-defined | Устойчивость траектории ≠ неизменность её формы. |
| RC-015 | SP-S4-P11 | утверждено | owner-approved; externally-compatible; externally-limited; pilot-observability-pending; falsifier-defined | Тренировать доступность / re-entry reality-coupled выбора под нагрузкой. |
| RC-016 | SP-S4-P12 | утверждено | owner-approved; externally-compatible; externally-limited; pilot-observability-pending; falsifier-defined | Контекстно-релевантное сохранение + functional re-entry. |
| RC-017 | SP-S4-P13 | на обсуждении | externally-compatible; externally-limited; pilot-observability-pending; falsifier-defined; owner-decision-pending | Возможная ошибка масштаба: успешная episodic self-regulation маскирует repeated generating conditions. |

## RC-016 — закрытый итог

4 сентября 2026 года SP-S4-P12 утверждён владельцем после Architect pass / Reality Check / Red Team.

> **Не непрерывный контроль, а достаточно надёжное сохранение и функциональное возвращение выбора под релевантной нагрузкой.**

Approval addendum: `RC-016_SP-S4-P12_APPROVAL_ADDENDUM.md`.

## RC-017 — открытый итог

5 сентября 2026 года для SP-S4-P13 завершены Architect pass, Reality Check и Red Team. Параметр ещё не утверждён владельцем.

### Surviving candidate

> **Ловушка S4 возникает не от самого recovery, reflection или усилия, а когда доказанная локальная компетентность систематически удерживает прежний масштаб вмешательства: человек продолжает успешно восстанавливать участие в повторяющихся эпизодах и именно поэтому недооценивает данные о том, что practically relevant объектом стала повторяющаяся конфигурация условий.**

Короткие формулы:

> **Компетентность на уровне эпизода может маскировать ошибку масштаба.**

> **«Я справляюсь» может скрыть вопрос «почему мне снова приходится справляться с тем же типом позиции?»**

### External compatibility

- intention–behavior literature: сильное намерение / понимание не гарантирует действие;
- implementation intentions: точная cue→action организация может уменьшать разрыв между намерением и действием;
- behaviour-maintenance literature: привычки, ресурсы и среда влияют на объём требуемой активной саморегуляции;
- behavioral activation: некоторые формы rumination могут функционально поддерживать avoidance, но это не универсальный вывод о мышлении;
- deliberate-reflection research: рефлексия может улучшать решение сложных задач, поэтому `thinking = trap` отвергается;
- habit/context research: generating conditions могут участвовать в вероятности повторяющегося поведения.

### Red Team boundaries

```text
thinking ≠ trap
recovery ≠ trap
effort ≠ bad structure
repetition ≠ proof of hidden structure
systemic view ≠ externalization of responsibility
local action may itself accumulate into system change
```

### Zero-delta / falsification condition

P13 должен быть пересмотрен или признан `zero-delta`, если его нельзя отличить от S1/procrastination, от уже утверждённого P12 transition failure, от нормального repeated recovery в объективно трудной среде либо если generating conditions нельзя описывать prospectively без post hoc storytelling.

Связанные файлы:
- `SP-S4-P13_ARCHITECT_PASS_NOTES.md`;
- `RC-017_SP-S4-P13.md`;
- `SP-S4-P13_RED_TEAM_NOTES.md`;
- `../SOURCE_MATERIALS/24_2026-09-05_P13_COMPENSATION_THINKING_AND_REALITY_CONTACT.md`.

## Текущая граница

**SP-S4-P13 прошёл Architect pass, RC-017 и Red Team; ожидается явное решение владельца.**
