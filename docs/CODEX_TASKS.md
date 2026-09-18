# CODEX_TASKS

**Статус:** активна одна ограниченная follow-up задача Codex.

## Авторитетный статус

Перед любой задачей Codex обязан читать актуальный SSOT проекта.

Codex не должен самостоятельно открывать Stage 5, SP-LAB-002 или изменять канон/методологию Selection Point.

## Завершённая задача

### Local Participant Storage v0.1

**Статус:** COMPLETED по отчёту Codex от 2026-09-18.

Task-файл:

`docs/CODEX_TASKS/TASK_LOCAL_PARTICIPANT_STORAGE_V0_1.md`

Реализованы local-first storage, CLI, schema validation, duplicate protection, privacy guardrails, tests и operator guide.

## Активная задача

### Local Participant Storage v0.2 — Time Provenance

**Статус:** ACTIVE  
**Причина:** участники могут отправлять D1 вовремя, а владелец переносит отчёт в локальное хранилище позже. Эти два времени нельзя смешивать.

Task-файл:

`docs/CODEX_TASKS/TASK_LOCAL_PARTICIPANT_STORAGE_V0_2_TIME_PROVENANCE.md`

Граница:

- сохранить `date` как дату отчёта/событий;
- добавить optional participant submission timestamp;
- автоматически фиксировать local-store ingestion timestamp;
- не считать задержку владельца задержкой участника;
- сохранить provenance при revision/overwrite;
- обновить tests/operator guide;
- не менять методологию, канон или продуктовый scope.

## Общие ограничения Codex

Codex не должен самостоятельно:

- открывать следующий архитектурный параметр;
- открывать Stage 5;
- открывать SP-LAB-002;
- дописывать метод;
- менять канон;
- создавать новый product scope;
- помещать реальные participant raw-data в Git/GitHub.

## Правило активации

Codex получает новую задачу только после явного решения владельца и появления ограниченного task-файла с измеримым результатом.

**Сейчас активна только `TASK_LOCAL_PARTICIPANT_STORAGE_V0_2_TIME_PROVENANCE.md`.**
