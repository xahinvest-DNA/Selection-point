# Карта доказательного статуса Selection Point

**Статус:** консолидированный evidence index  
**Дата обновления:** 5 сентября 2026 года  
**Режим:** internal approval ≠ external evidence

## Назначение

Selection Point является самостоятельной авторской системой. Внутренняя логическая утверждённость положения не означает автоматически его научную, клиническую или универсальную доказанность.

Подробные проверки и falsification хранятся в `../GOVERNANCE/REALITY_CHECK_REGISTER.md` и отдельных RC-файлах.

## Статусы

- `internal-approved` — утверждено внутри архитектуры Selection Point;
- `external-review-pending` — требуется внешний обзор;
- `externally-compatible` — найдены совместимые внешние данные по отдельным компонентам;
- `externally-limited` — есть существенные ограничения переноса;
- `pilot-observability-pending` — требуется проверка различимости на реальных эпизодах;
- `falsifier-defined` — определено условие существенного опровержения;
- `clinical-boundary` — нельзя превращать claim в медицинскую рекомендацию без профильной проверки.

## Консолидированная карта

| Объект | Внутренний статус | Внешний статус | Главная область проверки |
|---|---|---|---|
| SP-HCM-01–SP-HCM-08 | internal-approved | external-review-pending | perception, appraisal, state effects, habits, self-schema, learning, feedback |
| SP-HCM-09 | internal-approved | external-review-pending; falsifier-defined | agency, reciprocal causation, path dependence, perceived control |
| SP-S1-P01–SP-S1-P13 | internal-approved | external-review-pending; pilot-observability-pending | functional analysis, perception, self-regulation, transfer |
| SP-S2-P01–SP-S2-P13 | internal-approved | external-review-pending; pilot-observability-pending | pattern recognition, narrative identity, expectancy, scenario generalization |
| SP-S3-P01–SP-S3-P12 | internal-approved | external-review-pending; pilot-observability-pending | goal systems, psychological flexibility, skill acquisition, transfer |
| SP-S3-P13 | internal-approved | pilot-observability-pending; falsifier-defined | реальная пересматриваемость модели vs риторическая гибкость |
| SP-S4-P01 | internal-approved | external-review-pending; pilot-observability-pending; falsifier-defined | stress performance, state-dependent skill access |
| SP-S4-P02 | internal-approved | external-review-pending; pilot-observability-pending; falsifier-defined | attentional narrowing, threat bias, belief updating |
| SP-S4-P03 | internal-approved | initial-external-review; pilot-observability-pending; falsifier-defined | self-distancing, identity threat, self-model under load |
| SP-S4-P04 | internal-approved | initial-external-review; pilot-observability-pending; falsifier-defined | goal adjustment, competing goals, reality-driven revision |
| SP-S4-P05 | internal-approved | externally-compatible; externally-limited; pilot-observability-pending; falsifier-defined | stress-related narrowing, executive flexibility, objective vs subjective option narrowing |
| SP-S4-P06 | internal-approved | externally-compatible; externally-limited; pilot-observability-pending; falsifier-defined | state-dependent performance, metacognitive overgeneralization, mastery vs availability |
| SP-S4-P07 | internal-approved: zero-delta | externally-compatible; falsifier-defined | grief / regret / loss are real but not shown to be S4-specific structural pain |
| SP-S4-P08 | internal-approved | externally-compatible; externally-limited; pilot-observability-pending; falsifier-defined | psychological flexibility, recovery, graded participation, self-regulation |
| SP-S4-P09 | internal-approved: amended zero-delta | externally-compatible; externally-limited; pilot-observability-pending; falsifier-defined | facial feedback, posture, respiration, interoception; body-state bidirectionality |
| SP-S4-P10 | internal-approved | externally-compatible; externally-limited; pilot-observability-pending; falsifier-defined | regulatory flexibility, coping flexibility, dynamic resilience, goal adjustment, prospective observability |
| SP-S4-P11 | internal-approved | externally-compatible; externally-limited; pilot-observability-pending; falsifier-defined | stress inoculation, graduated simulation, situation awareness, feedback, limits of imagery |
| SP-S4-P12 | internal-approved | externally-compatible; externally-limited; pilot-observability-pending; falsifier-defined | recovery after lapse, dynamic resilience, regulatory flexibility, transfer limits, context dependence |
| SP-S4-P13 | internal-approved | externally-compatible; externally-limited; pilot-observability-pending; falsifier-defined | lapse vs relapse, EMA temporal aggregation, behaviour maintenance over time, context-dependent recurrence |
| SP-VM-01–SP-VM-02 | internal-approved as visual models | not evidence | риск ложного контроля, равной доступности и буквального чтения метафор |

## SP-S4-P05 — evidence boundary

Внешние данные совместимы с тем, что острый стресс способен в некоторых условиях ухудшать executive functioning, flexibility и использование периферической информации.

Из этого не следует универсальный телесный маркер или правило «больше вариантов = больше свободы».

Основные источники зафиксированы в RC-009.

## SP-S4-P08 — evidence boundary

P08 соседствует с psychological flexibility, self-regulation и recovery research, но не объявляется новым универсальным психологическим механизмом.

```text
восстановление участия
≠ доказанная отдельная психологическая сущность
```

## SP-S4-P09 — evidence boundary

Повторный обзор поддержал ограниченную двусторонность:

- facial feedback может влиять на affect, но эффекты малы / неоднородны;
- posture может влиять на состояние в отдельных контекстах;
- respiration ↔ emotion/cognition имеет reciprocal links;
- interoceptive / embodied effects не дают единого биомаркера выбора.

Поэтому:

```text
body-state bidirectionality
= externally compatible

но

body-state bidirectionality
≠ unique S4 mechanism
```

P09 утверждён как amended `zero-delta`.

## SP-S4-P10 — evidence boundary

Внешняя совместимость строится вокруг четырёх областей.

### Regulatory flexibility

Bonanno & Burton (2013), PMID 26173226: context sensitivity, repertoire и feedback responsiveness поддерживают идею context-sensitive adaptation.

### Coping flexibility

Cheng, Lau & Chan (2014), PMID 25222637: meta-analysis показывает связь coping flexibility с adjustment, но важен strategy–situation fit, а не простое количество стратегий.

Chen, Cheung & Cheng (2025), PMID 40411959: крупный meta-analysis COVID-контекста поддерживает association flexibility–adjustment при существенной heterogeneity.

### Resilience as process

Bonanno et al. (2024), PMID 37566760, и Bergeman & Nelson (2024), PMID 39531707, совместимы с пониманием resilience как динамического, контекстного процесса, а не invulnerability.

### Goal adjustment

Brandstätter & Bernecker (2022), PMID 34280324, и meta-analytic work по disengagement / reengagement поддерживают границу:

```text
адаптивность
≠ persistence любой ценой
```

Из внешней литературы **не следует** существование ступени S4, доказанность «жизненной траектории» как отдельной научной конструкции SP, что изменение планов автоматически является зрелостью или что хороший outcome подтверждает правильность выбора.

## SP-S4-P11 — evidence boundary

RC-015 нашёл совместимость отдельных компонентов с:

- stress-inoculation / graduated exposure to task-relevant load;
- simulation training;
- situation awareness;
- deliberate practice / feedback;
- motor imagery как вспомогательным, но недостаточным инструментом.

Ограничения:

```text
maximum stress ≠ best training
load awareness ≠ proof of choice loss
state regulation ≠ choice recovery
imagery may help ≠ sufficient reality-coupled verification
```

Внешняя литература не доказывает конкретную последовательность функциональных классов Selection Point.

## SP-S4-P12 — evidence boundary

RC-016 нашёл совместимость отдельных компонентов с:

- behaviour-maintenance distinction lapse / relapse и recovery self-efficacy;
- resilience как динамическим процессом, а не отсутствием реакции;
- regulatory flexibility: context sensitivity + feedback responsiveness;
- transfer-of-training literature, показывающей ограниченность автоматического переноса;
- habit/context literature.

Ограничения:

```text
recovery after lapse literature
≠ доказательство S4 readiness criterion

transfer is limited
→ S4 mastery ≠ universal stress resilience
```

P12 остаётся качественным внутренним transition profile; количественные thresholds относятся к Фазе 6.

## SP-S4-P13 — evidence boundary

RC-017 после temporal-scale refinement опирается на несколько совместимых направлений.

### Lapse / relapse

Behaviour-maintenance literature различает отдельный lapse и разворачивающийся relapse / sequence of lapses. Это совместимо с различением:

```text
single episode
≠ trajectory
```

Но литература не задаёт универсального числа эпизодов или временного окна, после которого SP должен объявить trajectory shift.

### Ecological Momentary Assessment

EMA literature различает быстрые локальные процессы вокруг отдельных событий и более медленные unfolding/background процессы, видимые через повторные измерения во времени.

Совместимое ограниченное положение:

> **Точный moment-level срез может быть недостаточен для вывода о динамике серии во времени.**

### Maintenance / context

Модели поддержания поведения и context-dependent relapse показывают, что вероятность поведения меняется во времени и контекстах; повторение может содержать practically useful данные о persistent conditions.

Но:

```text
series
≠ proof of one hidden cause

negative outcome series
≠ proof of bad decision process
```

### External verdict

P13 имеет статус:

`externally-compatible; externally-limited; pilot-observability-pending; falsifier-defined`.

Внешние данные не доказывают:

- пятиступенчатую архитектуру;
- что moment-level orientation сама причинно создаёт траекторную слепоту;
- универсальный temporal window;
- необходимость системного redesign после любой серии;
- валидность aggregation без проверки process/context.

## Приоритетные Reality Check

- RC-001 — SP-HCM-09;
- RC-002 — SP-S3-P13;
- RC-003–RC-017 — соответствующие параметры S4;
- RC-015 — SP-S4-P11;
- RC-016 — SP-S4-P12;
- RC-017 — SP-S4-P13.

## Клиническая и предметная граница

Selection Point не заменяет медицинскую диагностику, психотерапию, психиатрию, лечение зависимости, кризисную помощь или предметную экспертизу.

Телесный сигнал, субъективная ясность, внутреннее ощущение правильности, единичный внешний успех или серия исходов не являются самостоятельным доказательством истинности модели.

## Консолидация

- после P05 — выполнена 29 августа 2026 года;
- после P10 — выполнена 30 августа 2026 года;
- после P13 / на границе Ступени 4 — **выполнена 5 сентября 2026 года**.

## Текущая остановка

**Ступень 4 завершена полностью. SP-S5-P01 не открыт.**
