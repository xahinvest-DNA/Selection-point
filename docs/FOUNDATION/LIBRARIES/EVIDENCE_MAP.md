# Карта доказательного статуса Selection Point

**Статус:** консолидированный evidence index  
**Дата обновления:** 29 августа 2026 года  
**Режим:** internal approval ≠ external evidence

## Назначение

Selection Point является самостоятельной авторской системой. Внутренняя логическая утверждённость положения не означает автоматически его научную, клиническую или универсальную доказанность.

Подробные активные проверки и falsification хранятся в `../GOVERNANCE/REALITY_CHECK_REGISTER.md` и отдельных RC-файлах.

---

## Статусы

- `internal-approved` — утверждено внутри архитектуры Selection Point;
- `external-review-pending` — требуется внешний обзор;
- `externally-compatible` — найдены содержательно совместимые внешние данные по отдельным компонентам;
- `externally-limited` — найдены существенные ограничения переноса;
- `externally-challenged` — данные требуют содержательного пересмотра;
- `pilot-observability-pending` — требуется проверка различимости на реальных эпизодах;
- `falsifier-defined` — определено условие существенного опровержения;
- `revisit-required` — параметр должен быть содержательно открыт повторно;
- `clinical-boundary` — claim нельзя превращать в медицинскую/клиническую рекомендацию без профильной проверки.

---

## Консолидированная карта

| Объект | Внутренний статус | Внешний статус | Главная область проверки |
|---|---|---|---|
| SP-HCM-01–SP-HCM-08 | internal-approved | external-review-pending | perception, appraisal, state effects, habits, self-schema, learning, feedback, recovery points |
| SP-HCM-09 | internal-approved | external-review-pending; falsifier-defined | agency, reciprocal causation, path dependence, perceived control, риск смешения участия и контроля результата |
| SP-S1-P01–SP-S1-P13 | internal-approved | external-review-pending; pilot-observability-pending | functional analysis, perception, self-schema, interoception, self-regulation, transfer |
| SP-S2-P01–SP-S2-P13 | internal-approved | external-review-pending; pilot-observability-pending | pattern recognition, narrative identity, expectancy, scenario generalization, uncertainty tolerance |
| SP-S3-P01–SP-S3-P12 | internal-approved | external-review-pending; pilot-observability-pending | decentering, goal systems, psychological flexibility, intention–behavior gap, skill acquisition, transfer |
| SP-S3-P13 | internal-approved | pilot-observability-pending; falsifier-defined | различие реальной пересматриваемости модели и риторического признания ошибки / хронического сомнения |
| SP-S4-P01 | internal-approved | external-review-pending; pilot-observability-pending; falsifier-defined | stress performance, state-dependent skill access, automaticity, recovery |
| SP-S4-P02 | internal-approved | external-review-pending; pilot-observability-pending; falsifier-defined | attentional narrowing, threat bias, premature closure, expert recognition, belief updating |
| SP-S4-P03 | internal-approved | initial-external-review; pilot-observability-pending; falsifier-defined | self-distancing, identity threat, self-concept clarity; практический вес self-модели под нагрузкой |
| SP-S4-P04 | internal-approved | initial-external-review; pilot-observability-pending; falsifier-defined | goal adjustment, competing goals, psychological flexibility; reality-driven revision vs state-driven displacement |
| SP-S4-P05 | internal-approved | externally-compatible; externally-limited; pilot-observability-pending; falsifier-defined | stress-related cognitive narrowing, executive flexibility, peripheral information use; различение объективно узкого и субъективно схлопнувшегося поля ходов |
| SP-VM-01–SP-VM-02 | internal-approved as visual models | not evidence | риск ложного контроля, равной доступности и буквального чтения метафор |

---

## SP-S4-P05 — evidence boundary

Общий уровень внешней совместимости:

- острый стресс способен ухудшать рабочую память, когнитивную гибкость и исполнительные функции;
- стресс, тревога и высокая центральная нагрузка могут ухудшать использование периферической информации;
- ширина внимания является изменяемой характеристикой.

Рабочие источники RC-009:

1. Shields, Sazma & Yonelinas (2016), PMID 27371161, DOI 10.1016/j.neubiorev.2016.06.038;
2. McKlveen et al. (2018), PMID 28690203;
3. `Peripheral vision in real-world tasks: A systematic review`, PMCID PMC9568462.

Из этого **не следует**:

- что Selection Point как модель доказан;
- что напряжение мышц лба является универсальным маркером;
- что туннельное зрение обязательно означает потерю выбора;
- что периферическое зрение является универсальным переключателем выбора;
- что больше вариантов автоматически означает больше свободы.

Поэтому P05 имеет одновременно `externally-compatible` и `externally-limited` статус.

---

## Приоритетные Reality Check

- RC-001 — SP-HCM-09;
- RC-002 — SP-S3-P13;
- RC-003 — SP-S4-P01;
- RC-004 — SP-S4-P02;
- RC-005 — матрица 5 × 13;
- RC-006 — публичный термин HCM-09;
- RC-007 — SP-S4-P03;
- RC-008 — SP-S4-P04;
- RC-009 — SP-S4-P05, architect/reality/red-team завершены, owner-approved; pilot-observability-pending остаётся действующим.

---

## Правила внешнего обзора

Для каждого внешнего источника фиксируется:

1. какой точный claim проверяется;
2. что именно совпадает;
3. что не совпадает;
4. уровень и качество источника;
5. границы переноса;
6. есть ли данные против формулировки;
7. требуется ли архитектурный пересмотр.

Поиск только подтверждений запрещён.

---

## Клиническая и предметная граница

Selection Point не заменяет медицинскую диагностику, психотерапию, психиатрию, лечение зависимости, кризисную помощь или предметную экспертизу.

Телесный сигнал, субъективная ясность, внутреннее ощущение правильности или внешний успех не являются самостоятельным доказательством истинности модели.

---

## Консолидация

29 августа 2026 года после утверждения P05 выполнена плановая консолидация evidence status SP-S4-P03–SP-S4-P05.

Следующая плановая консолидация: после P10, затем P13 / граница ступени.

---

## Текущая остановка

**SP-S4-P05 утверждён. SP-S4-P06 не открыт.**
