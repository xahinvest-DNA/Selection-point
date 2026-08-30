# Reality Check Register

**Статус:** действующий реестр проверок  
**Дата обновления:** 30 августа 2026 года

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
| RC-014 | SP-S4-P10 | активен | reality-check-complete; red-team-complete; externally-compatible; externally-limited; pilot-observability-pending; falsifier-defined; owner-decision-pending | Stage-specific life-scale delta сохранена: устойчивость траектории ≠ неизменность её формы. |

## RC-014 — активный итог

Рабочий центральный тезис:

> **Жизненные проявления четвёртой ступени состоят в том, что устойчивость собственной линии всё меньше зависит от сохранения её прежней формы. Под значимой нагрузкой могут измениться план, темп, масштаб, распределение ресурсов, роли, обязательства и отдельные цели; могут сохраняться последствия срыва или кризиса. Однако человек способен снова организовывать последующие ходы из изменившейся фактической позиции относительно релевантного направления и обратной связи, не требуя сначала вернуть прежнее устройство жизни и не превращая сохранение направления в обязанность сохранять любой прежний план или цель.**

Коротко:

> **Устойчивость траектории ≠ неизменность её формы.**

### Что поддерживает внешний слой

Исследования regulatory/coping flexibility и dynamic resilience совместимы с тем, что адаптивность зависит от контекста, доступного ответа и коррекции по feedback, а не от применения одной стратегии во всех условиях. Исследования goal adjustment также ограничивают идею persistence: своевременное disengagement/reengagement может быть частью успешной саморегуляции.

Внешний слой **не доказывает** пятиступенчатую архитектуру.

### Red Team boundaries

```text
сохранение траектории
≠ persistence конкретной цели любой ценой

изменение формы
≠ адаптивность само по себе

благоприятный исход
≠ критерий P10

скорость восстановления
≠ критерий P10

объективно тяжёлая позиция
≠ потеря выбора
```

### Prospective observability

Чтобы избежать рассказа задним числом, до знания результата должно быть возможно увидеть:

1. признание изменившейся фактической позиции;
2. отсутствие автоматического приоритета прежнего плана;
3. различимый релевантный приоритет / осознанный его пересмотр;
4. practically available следующий ход;
5. открытость дальнейшей корректировке по feedback.

### Falsifier

Дельту следует пересмотреть, если life-scale pattern нельзя наблюдать отдельно от P04/P08, если он существует только как ретроспективная история, или если в пилоте невозможно отличить reality-based reorganization от avoidance / обычной смены планов.

## Текущая граница

**RC-014 завершён до owner decision. SP-S4-P10 остаётся активным; internal-approved отсутствует. SP-S4-P11 не открыт.**
