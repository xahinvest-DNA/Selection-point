# SP-LAB-D004 — Reality Engine measurement foundation

**Дата:** 15 сентября 2026 года  
**Статус:** owner-approved remediation decision  
**Источник решения:** после диагностики проекта владелец согласился выполнить доступные исправления до отдельного детального обсуждения пилота.

## Что утверждено этим решением

1. Product Lab синхронизируется с утверждённой RC-018 boundary.
2. В исследовательских данных отдельно хранятся:
   - selected continuation;
   - realized continuation;
   - consequence;
   - observed feedback;
   - model update.
3. Conscious non-action может быть realized continuation.
4. Partial execution считается partial test, а не автоматически успехом или провалом.
5. Selected → realized gap рассматривается сначала как данные, а не как моральная оценка.
6. Для owner self-pilot создаётся рабочая спецификация event model и метрик.
7. Prompt/scaffold exposure должен быть видимым, чтобы не приписывать системе развитие навыка там, где наблюдается только эффект напоминания.
8. Для будущих внешних участников вводится data-governance boundary: raw participant data не хранится в публичном репозитории.
9. В репозиторий добавляется автоматическая consistency check для известных status/documentation drift.

## Что этим решением НЕ открывается

- SP-S5-P01;
- SP-LAB-002;
- внешний пользовательский пилот;
- готовое приложение;
- универсальный Trajectory Score;
- Selection Capacity Score;
- доказанная эффективность;
- причинный эффект напоминаний;
- новая каноническая архитектура Selection Point.

## Рабочие документы

- `REALITY_EVENT_MODEL_V0_2.md`;
- `PILOT_METRICS_SPEC_V0_1.md`;
- `PARTICIPANT_DATA_POLICY_V0_1.md`;
- обновлённый `PERSONAL_TRAJECTORY_PILOT_V0.md`;
- обновлённый `CANONICAL_TO_PRODUCT_MAP.md`;
- обновлённый `RESEARCH_PLAN.md`;
- автоматическая проверка `scripts/check_project_consistency.py`.

## Следующая точка

После завершения этой remediation-задачи следующий содержательный шаг — **отдельно обсудить дизайн пилота**, не открывая его автоматически только на основании текущей документации.
