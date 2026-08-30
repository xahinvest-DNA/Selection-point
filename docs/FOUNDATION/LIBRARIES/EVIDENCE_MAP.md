# Карта доказательного статуса Selection Point

**Статус:** консолидированный evidence index  
**Дата обновления:** 30 августа 2026 года  
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

Из внешней литературы **не следует**:

- существование ступени S4;
- доказанность «жизненной траектории» как отдельной научной конструкции Selection Point;
- что изменение планов автоматически является зрелостью;
- что хороший outcome подтверждает правильность выбора;
- что быстрое восстановление означает более высокий уровень.

Поэтому P10 имеет статус `externally-compatible; externally-limited; pilot-observability-pending; falsifier-defined`.

## Приоритетные Reality Check

- RC-001 — SP-HCM-09;
- RC-002 — SP-S3-P13;
- RC-003–RC-014 — соответствующие параметры S4;
- RC-014 — SP-S4-P10: `owner-approved; externally-compatible; externally-limited; pilot-observability-pending; falsifier-defined`.

## Клиническая и предметная граница

Selection Point не заменяет медицинскую диагностику, психотерапию, психиатрию, лечение зависимости, кризисную помощь или предметную экспертизу.

Телесный сигнал, субъективная ясность, внутреннее ощущение правильности или внешний успех не являются самостоятельным доказательством истинности модели.

## Консолидация

- после P05 — выполнена 29 августа 2026 года;
- после P10 — **выполнена 30 августа 2026 года**;
- следующая — P13 / граница ступени.

## Текущая остановка

**SP-S4-P10 утверждён. SP-S4-P11 не открыт.**
