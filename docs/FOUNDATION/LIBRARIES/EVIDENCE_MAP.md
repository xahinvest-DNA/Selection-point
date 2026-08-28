# Карта доказательного статуса Selection Point

**Статус:** консолидированный evidence index  
**Дата обновления:** 28 августа 2026 года  
**Режим:** internal approval ≠ external evidence

## Назначение

Selection Point является самостоятельной авторской системой. Внутренняя логическая утверждённость положения не означает автоматически его научную, клиническую или универсальную доказанность.

С 28 августа 2026 года подробная активная очередь внешней проверки и falsification хранится в:

`../GOVERNANCE/REALITY_CHECK_REGISTER.md`.

---

## Статусы

- `internal-approved` — утверждено внутри архитектуры Selection Point;
- `external-review-pending` — требуется внешний обзор;
- `externally-compatible` — найдены содержательно совместимые внешние данные по отдельным компонентам;
- `externally-limited` — найдены важные ограничения применимости;
- `externally-challenged` — данные требуют содержательного пересмотра;
- `pilot-observability-pending` — нужно проверить различимость на реальных эпизодах;
- `falsifier-defined` — определено условие существенного опровержения;
- `revisit-required` — параметр должен быть содержательно открыт повторно;
- `clinical-boundary` — нельзя превращать claim в медицинскую/клиническую рекомендацию без профильной проверки.

---

## Консолидированная карта

| Объект | Внутренний статус | Внешний статус | Главная область проверки |
|---|---|---|---|
| SP-HCM-01–SP-HCM-08 | internal-approved | external-review-pending | perception, appraisal, state effects, habits, self-schema, learning, feedback, recovery points |
| SP-HCM-09 | internal-approved | external-review-pending; falsifier-defined | agency, reciprocal causation, path dependence, perceived control, риск смешения участия и контроля результата |
| SP-S1-P01–SP-S1-P13 | internal-approved | external-review-pending; pilot-observability-pending | functional analysis, perception, self-schema, interoception, self-regulation, transfer |
| SP-S2-P01–SP-S2-P13 | internal-approved | external-review-pending; pilot-observability-pending | pattern recognition, narrative identity, expectancy, scenario generalization, uncertainty tolerance |
| SP-S3-P01–SP-S3-P12 | internal-approved | external-review-pending; pilot-observability-pending | decentering, goal systems, psychological flexibility, intention–behavior gap, skill acquisition, transfer |
| SP-S3-P13 | internal-approved | pilot-observability-pending; falsifier-defined | различие реальной пересматриваемости модели и риторического признания ошибки/хронического сомнения |
| SP-S4-P01 | internal-approved | external-review-pending; pilot-observability-pending | stress performance, state-dependent skill access, automaticity, recovery |
| SP-S4-P02 | internal-approved | external-review-pending; pilot-observability-pending | attentional narrowing, threat bias, premature closure, expert recognition, belief updating |
| SP-VM-01–SP-VM-02 | internal-approved as visual models | not evidence | проверка риска ложного контроля, равной доступности и буквального чтения метафор |

---

## Приоритетная очередь Reality Check

### RC-001 — SP-HCM-09

Проверить, не смешивает ли язык «создание собственной реальности»:

- человеческую агентность;
- причинное участие;
- воспринимаемый контроль;
- реальный внешний результат.

Внутренний канон не изменяется автоматически; public-language review обязателен до Фазы 4.

### RC-002 — SP-S3-P13

Проверить наблюдаемое различие:

```text
модель действительно корректируется фактами
≠ человек только говорит, что готов пересмотреть модель
≠ человек хронически сомневается во всём
```

### RC-003 — SP-S4-P01

Проверить различие:

```text
способность сформирована, но временно недоступна под нагрузкой
≠ способность ещё не сформирована
```

### RC-004 — SP-S4-P02

Проверить различие:

```text
функциональное сужение внимания
≠ искажённое сужение
```

Особенно важно исключить ретроспективный критерий «если исход плохой, значит сужение было искажённым».

### RC-005 — матрица 5 × 13

Проверка ведётся на каждом следующем параметре: существует ли самостоятельная дельта или ячейка является `zero-delta`.

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

Поиск только подтверждений запрещён. Обзор обязан включать критику, ограничения и противоположные эффекты.

---

## Клиническая и предметная граница

Selection Point не заменяет медицинскую диагностику, психотерапию, психиатрию, лечение зависимости, помощь при РПП, кризисную помощь или предметную экспертизу.

Телесный сигнал, субъективная ясность, внутреннее ощущение правильности или внешняя успешность не считаются самостоятельным доказательством истинности модели.

---

## Delta-first

Новые evidence questions после следующего параметра сначала фиксируются в parameter delta и Reality Check Register.

Этот файл консолидируется после P05, P10, P13, на границе ступени или по отдельному решению Андрея.

---

## Текущая остановка

Согласно `../PROJECT_STATE.yaml`:

**SP-S4-P02 утверждён. SP-S4-P03 не открыт.**
