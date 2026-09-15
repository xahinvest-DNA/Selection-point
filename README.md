# Selection Point

**Selection Point** — самостоятельная система восстановления способности выбора.

## Project system

Selection Point рассматривается как **один проект с несколькими уровнями и repository nodes**, а не как набор независимых проектов.

Управляющий контур: `docs/PROJECT_SYSTEM/PROJECT_SYSTEM_STATE.yaml` и `docs/PROJECT_SYSTEM/PROJECT_CONTROL_PLANE.md`.

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

## Текущее состояние

Авторитетный статус архитектуры: `docs/FOUNDATION/PROJECT_STATE.yaml`.

Авторитетная топология проекта: `docs/PROJECT_SYSTEM/PROJECT_SYSTEM_STATE.yaml`.

На 15 сентября 2026 года:

- Фаза 3 — точная архитектура пяти ступеней;
- SP-HCM-01–SP-HCM-09 утверждены;
- Ступени 1–3 завершены;
- **Ступень 4 завершена полностью: SP-S4-P01–SP-S4-P13**, P07 = `zero-delta`, P09 = `amended zero-delta`;
- последний утверждённый параметр: **SP-S4-P13 «Ловушка четвёртой ступени»**;
- утверждена сквозная boundary **RC-018 — choice → realized continuation → feedback**;
- создан `SP-PSYS-001` — Project Control Plane для синхронизации уровней/репозиториев;
- `SP-HLAB-001` зарегистрирован как private evidence node owner self-pilot;
- открытого архитектурного параметра нет;
- SP-S5-P01 — следующий кандидат, **не открыт**;
- внешний пользовательский пилот — **не открыт**.

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

Для проекта в целом:

1. `docs/PROJECT_SYSTEM/PROJECT_SYSTEM_STATE.yaml`;
2. `docs/PROJECT_SYSTEM/PROJECT_CONTROL_PLANE.md`;
3. `docs/PROJECT_SYSTEM/CROSS_REPO_SYNC_PROTOCOL.md`;
4. `docs/PROJECT_SYSTEM/HEALTH_LAB_NODE_CONTRACT.md`.

Для архитектуры метода:

1. `docs/FOUNDATION/PROJECT_OPERATING_PROTOCOL.md`;
2. `docs/FOUNDATION/PROJECT_STATE.yaml`;
3. `docs/FOUNDATION/CURRENT_PROJECT_STATE.md`;
4. `docs/FOUNDATION/CORE_CHOICE_ACTION_FEEDBACK_BOUNDARY.md`;
5. `docs/FOUNDATION/CANONICAL/01B_CORE_CHOICE_ACTION_FEEDBACK_BOUNDARY_CANONICAL.md`.

Для Product Lab:

1. `docs/PRODUCT_LAB/LAB_STATE.yaml`;
2. `docs/PRODUCT_LAB/00_LAB_INDEX.md`;
3. `docs/PRODUCT_LAB/REALITY_EVENT_MODEL_V0_2.md`;
4. `docs/PRODUCT_LAB/PILOT_METRICS_SPEC_V0_1.md`.

**Ступень 4 завершена. RC-018 утверждён. SP-PSYS-001 активен. SP-S5-P01 и внешний пилот не открыты.**
