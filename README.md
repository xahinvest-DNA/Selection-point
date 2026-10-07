# Selection Point

**Selection Point** — самостоятельная система восстановления способности выбора.

## Project system

Selection Point рассматривается как **один проект с несколькими уровнями и repository nodes**, а не как набор независимых проектов.

Управляющий контур: `docs/PROJECT_SYSTEM/PROJECT_SYSTEM_STATE.yaml` и `docs/PROJECT_SYSTEM/PROJECT_CONTROL_PLANE.md`.

Активная операционная модель: `docs/PROJECT_SYSTEM/SP_CHAT_OPERATING_MODEL.md` (`SP-OPS-002`).

Текущая топология:

```text
Selection-point (public)
├─ Foundation / Canon
├─ Product Lab
└─ Project Control Plane
       ↓ contracts
Selection-point-health-lab (private)
└─ SP-HLAB-001 / owner self-pilot evidence node
       ↑ de-identified findings / falsification signals only
```

`Selection-point-health-lab` хранит приватные longitudinal raw-data, локальные reviews и рабочие гипотезы. Он не имеет права автоматически менять Product Lab или канон. Raw personal data обратно в публичный репозиторий не переносятся.

Рабочий контур проекта:

```text
Owner — направление и окончательное решение
Chat — методология + research + synthesis + audits + bounded artifacts + evidence review + Red Team
Codex — только утверждённая техническая реализация, когда она действительно нужна
Pilot / Reality — эмпирическая проверка и право опровергнуть модель
```

Отдельный режим ChatGPT Work **не является частью активной системы и не требуется ни для одного шага проекта**. Устойчивость проекта важнее зависимости от отдельного режима или его лимитов.

## Текущее состояние

<!-- SP:CURRENT:BEGIN -->
Дата синхронизации: **2026-10-07**.

Направление: **Системно выбирать и фактически совершать действия, которые сохраняют здоровье, повышают физическую эффективность и расширяют возможности тела в будущем.**.

Маршрут: `stage_1_course_first_development`; цель: `build_effective_stage_1_course`.

**Следующий шаг: Рассмотреть и утвердить либо доработать шаблон урока первой ступени.**

Артефакт: `docs/COURSE/STAGE_1_LESSON_TEMPLATE.md` — `draft_for_owner_review`.

Структура: `SP-COURSE-S1-STRUCT-003` — `approved`; 5 уроков, ориентация и интеграция отдельно.

Foundation: последний утверждённый параметр `SP-S4-P13`; следующий кандидат `SP-S5-P01` — `unopened`.

Capability: `SP-TR-S1-CAP-002`.

Опросник: `SP-DTQ-002` — `draft_for_owner_review`; отдельная телеметрия.

Checkpoint: `docs/PROJECT_SYSTEM/RECOVERY_CHECKPOINT_2026-10-07_SYNC_REPAIR.md`.

Активные рабочие уточнения: `docs/FOUNDATION/PROJECT_OPERATING_PROTOCOL_ADDENDUM_2026-10-05_DIRECTION_ROUTE_ACTION.md`.

Gate-маршрут активен: `false`; V0 execution: `false`.

Закрытые области: `stage_5: unopened`; `product_lab_002: unopened`; `external_user_pilot: unopened`; `trainer_implementation: unopened`.

Источники: `docs/PROJECT_SYSTEM/PROJECT_SYSTEM_STATE.yaml`; `docs/FOUNDATION/PROJECT_STATE.yaml`; `docs/PRODUCT_LAB/LAB_STATE.yaml`.
<!-- SP:CURRENT:END -->

## Центральная идея

> **Контроль предполагает возможность заранее получить желаемый результат. Создание происходит независимо от контроля.**

Уточнённый core cycle:

```text
увидеть фактическую текущую позицию
→ различить / выбрать направление
→ выбрать доступное продолжение
→ фактически реализовать продолжение
→ получить последствия / ответ реальности
→ извлечь обратную связь
→ оказаться в новой фактической позиции
→ снова увидеть
→ повторить цикл
```

## Сквозные границы

> **Модель остаётся рабочей только пока реальность сохраняет возможность её изменить.**

```text
влияние ≠ контроль
участие в причинности ≠ единственная причина
создание траектории ≠ предопределение результата
```

RC-018 добавляет:

> **Внутренне выбранное продолжение не равно фактически реализованному продолжению.**

```text
выбрать ≠ сделать
сделать ≠ получить желаемое
последствия ≠ автоматически использованная обратная связь
```

Неисполненный выбор остаётся реальным внутренним фактом, но не получает внешней проверки как неслучившееся действие.

## Утверждённый SP-S4-P13

> **Выбор совершается в моменте. Траектория обнаруживается во времени.**

Ловушка:

> **Ошибка — считать момент достаточным масштабом для оценки траектории.**

Корректирующая формула:

> **Прошлое не должно определять следующий выбор, но релевантная история должна иметь право изменить описание текущей позиции.**

RC-018 уточняет:

> **Внутренние выборы показывают направление намерения; фактически реализованные продолжения участвуют в построении фактической траектории.**

## Граница следующего уровня

```text
S4:
выбор / recovery в фактической позиции
+
trajectory-level feedback

S5 candidate:
система условий, формирующая вероятные будущие позиции
```

Полная архитектура S5 ещё не открыта.

## Точки входа

Начните с `docs/PROJECT_SYSTEM/PROJECT_SYSTEM_STATE.yaml` → `new_chat_bootstrap.read_first`.
Это единственный список обязательного восстановления активной работы.

По задаче:
- архитектура: `docs/FOUNDATION/PROJECT_STATE.yaml` и `PROJECT_OPERATING_PROTOCOL.md`;
- управление: `docs/PROJECT_SYSTEM/PROJECT_CONTROL_PLANE.md` и `SP_CHAT_OPERATING_MODEL.md`;
- курс: `docs/COURSE/STAGE_1_EFFECTIVE_BODY_COURSE_STRUCTURE.md` и `STAGE_1_LESSON_TEMPLATE.md`;
- Lab: `docs/PRODUCT_LAB/LAB_STATE.yaml`;
- техника: `docs/CODEX_TASKS.md`;
- напоминания: `docs/PROJECT_SYSTEM/REMINDER_DELIVERY_STATE.yaml`;
- межрепозиторный контракт: `docs/PROJECT_SYSTEM/CROSS_REPO_SYNC_PROTOCOL.md` и `HEALTH_LAB_NODE_CONTRACT.md`.

Текущий блок выше генерируется командой `python scripts/render_project_status.py`.
