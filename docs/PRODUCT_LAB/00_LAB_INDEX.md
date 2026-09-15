# Selection Point Product Lab

**Статус:** активный исследовательский workstream / owner self-pilot active  
**Обновлено:** 15 сентября 2026 года  
**Контур:** параллельный Фазе 3, без открытия Фаз 4–8  
**SSOT лаборатории:** `LAB_STATE.yaml`

## Назначение

Product Lab проверяет, может ли утверждённая методология Selection Point быть передана людям как **тренажёр способности выбирать** и привести к наблюдаемому обучению.

На текущем owner self-pilot проверяется более сильная продуктовая рамка: Selection Point как система, которая **связывает локальный выбор с траекторией во времени и проверяет внутренний выбор через фактически реализованное продолжение и последствия**.

Формулировки Product Lab остаются продуктовыми гипотезами, а не новым каноническим определением метода.

## Product Lab внутри единого проекта

С 15 сентября 2026 года репозитории Selection Point рассматриваются как узлы **одного проекта**, а не как независимые проекты.

Управляющий контур проекта:

- `../PROJECT_SYSTEM/PROJECT_SYSTEM_STATE.yaml` — topology / authority SSOT;
- `../PROJECT_SYSTEM/PROJECT_CONTROL_PLANE.md` — роли уровней и поток решений/данных;
- `../PROJECT_SYSTEM/CROSS_REPO_SYNC_PROTOCOL.md` — правила синхронизации;
- `../PROJECT_SYSTEM/HEALTH_LAB_NODE_CONTRACT.md` — контракт первого private evidence-node.

Текущая структура:

```text
Foundation / Canon
        ↓
Product Lab
        ↓ contract
SP-HLAB-001 — Selection-point-health-lab (private evidence node)
        ↑
de-identified findings / contradictions / falsification signals
```

`SP-HLAB-001` хранит owner self-pilot raw-data, локальные reviews и локальные H-xxx hypotheses. Эти данные и гипотезы не имеют автоматического права изменять Product Lab или канон.

## Граница с основным проектом

```text
канон Selection Point
        ↓
CANONICAL_TO_PRODUCT_MAP
        ↓
продуктовые гипотезы
        ↓
research contracts
        ↓
evidence nodes / experiments
        ↓
reviewed de-identified findings
        ↓
решение лаборатории
```

Product Lab не имеет права напрямую изменять канонический смысл. Если данные требуют пересмотра метода, создаётся отдельное предложение в основной архитектурный контур и применяется действующий `PROJECT_OPERATING_PROTOCOL.md`.

## RC-018 как обязательная граница Lab

С 15 сентября 2026 года Product Lab синхронизирован с утверждённой boundary RC-018:

```text
selected continuation
≠ realized continuation
≠ consequence
≠ used feedback
```

Следствия:

- внутренний выбор остаётся реальным событием, но не является доказательством исполнения;
- conscious non-action может быть фактически реализованным продолжением;
- partial execution означает partial test;
- selected → realized gap является данными, а не моральной оценкой;
- последствия не считаются использованным feedback автоматически;
- measurement adherence не считается автоматически domain success или доказательством Selection Capacity.

## Документы

### Управление проектом

- `../PROJECT_SYSTEM/PROJECT_SYSTEM_STATE.yaml` — система уровней и зарегистрированные repository nodes;
- `../PROJECT_SYSTEM/PROJECT_CONTROL_PLANE.md` — Project Control Plane;
- `../PROJECT_SYSTEM/CROSS_REPO_SYNC_PROTOCOL.md` — downward/upward sync;
- `../PROJECT_SYSTEM/HEALTH_LAB_NODE_CONTRACT.md` — контракт `SP-HLAB-001`.

### Product Lab

- `LAB_CHARTER.md` — полномочия, границы и lifecycle;
- `LAB_STATE.yaml` — единственный источник текущего состояния Lab;
- `PERSONAL_TRAJECTORY_PILOT_V0.md` — текущий активный owner self-pilot;
- `REALITY_EVENT_MODEL_V0_2.md` — минимальная RC-018-aligned схема событий Reality Loop;
- `PILOT_METRICS_SPEC_V0_1.md` — рабочая спецификация измерений без общего score;
- `PARTICIPANT_DATA_POLICY_V0_1.md` — обязательная граница для данных будущих внешних участников;
- `PRODUCT_THESIS.md` — рабочая продуктовая гипотеза;
- `SELECTION_CAPACITY_V0.md` — рабочая декомпозиция предполагаемой тренируемой способности и Red Team;
- `SP_LAB_001_SYNTHESIS.md` — утверждённый итог SP-LAB-001;
- `MINIMAL_RECOVERY_LOOP.md` — гипотеза минимального цикла восстановления участия;
- `TRAINING_ARCHITECTURE_V0.md` — предварительная гипотеза архитектуры обучения;
- `COMPARATIVE_POSITIONING_RESEARCH_01.md` — сравнительная проверка относительно близких подходов;
- `HYPOTHESES.md` — реестр проверяемых гипотез;
- `CANONICAL_TO_PRODUCT_MAP.md` — мост «канон → тренируемая способность → наблюдаемое изменение»;
- `RESEARCH_PLAN.md` — порядок исследовательских фаз;
- `DECISION_LOG.md` — история явных продуктовых решений.

## Утверждённая база

`SP-LAB-001` утверждён 1 сентября 2026 года как рабочая продуктовая модель для последующей внешней проверки.

Ключевая формулировка:

> **Selection Capacity — способность сохранять или восстанавливать участие в собственном действии так, чтобы релевантная реальность продолжала иметь возможность изменить модель, следующий ход и, при необходимости, само направление.**

Краткая внутренняя формула:

> **Реальность всё ещё может тебя поправить.**

## Текущая точка — SP-LAB-PILOT-001

12 сентября 2026 года владелец возобновил Product Lab через личный self-pilot, не открывая SP-LAB-002.

15 сентября после диагностики владелец утвердил устранение рассинхронизации Product Lab с RC-018 и создание измерительной инфраструктуры.

15 сентября затем утверждено системное решение `SP-PSYS-001`: `Selection-point` и `Selection-point-health-lab` — единый проект с разными authority/evidence уровнями. Health Lab зарегистрирован как `SP-HLAB-001`.

Первый домен: **тело / здоровье / физическая эффективность**.

Текущий приоритет:

```text
Trajectory Engine
+ Selected → Realized Evidence
+ episode → day → week → month → quarter
```

Рабочее ядро Reality Loop:

```text
fact
→ trajectory
→ forecast
→ selection point
→ selected continuation
→ realized continuation
→ consequence
→ observed feedback
→ model update
```

Принят режим напоминаний **B**:

- `21:30` — Review + Plan;
- утром — Plan Recall;
- в середине дня — Trajectory Check.

`prompt_exposure` должен фиксироваться отдельно, чтобы не спутать самостоятельный навык с поведением под scaffold.

Исторические raw-записи Health Lab за 12–14 сентября сохраняются как были получены и не переписываются под новую схему. При необходимости они нормализуются только в derived layer с явной ссылкой на источник и `unknown/not_observed` для отсутствующих наблюдений.

## Что остаётся закрытым

- `SP-LAB-002 — Problem Discovery Research Design` остаётся `unopened`;
- внешний пользовательский пилот в LAB-0 не открыт;
- S5 не открывается из Product Lab;
- доказанная эффективность не заявляется;
- Body pilot не превращает SP в медицинское или фитнес-приложение;
- единый Selection Capacity / Trajectory Score не вводится;
- Simulator / serious game остаётся вторым контуром после проверки Reality Loop.

## Bootstrap для нового чата

Новый чат, работающий с проектом в целом, сначала читает:

1. `../PROJECT_SYSTEM/PROJECT_SYSTEM_STATE.yaml`;
2. `LAB_STATE.yaml`;
3. `PERSONAL_TRAJECTORY_PILOT_V0.md`;
4. `REALITY_EVENT_MODEL_V0_2.md`;
5. `PILOT_METRICS_SPEC_V0_1.md`;
6. `SP_LAB_001_SYNTHESIS.md`;
7. `DECISION_LOG.md`.

При работе с фактическими pilot data затем читать `xahinvest-DNA/Selection-point-health-lab::docs/NODE_STATE.yaml` и локальные данные Health Lab.

`SP-LAB-002`, S5 и внешний пилот автоматически не открывать.
