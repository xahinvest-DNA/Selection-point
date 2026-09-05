# Governance Selection Point

**Статус:** действующий индекс управления проектом  
**Дата обновления:** 5 сентября 2026 года

## Действующие документы

1. `../PROJECT_STATE.yaml` — единственный источник текущего статуса.
2. `../PROJECT_OPERATING_PROTOCOL.md` — process protocol v4.0.
3. `PROJECT_GOVERNANCE_SYSTEM.md` — источники истины, delta-first, consistency check.
4. `REALITY_CHECK_PROTOCOL.md` — внешняя проверка и falsification.
5. `REALITY_CHECK_REGISTER.md` — реестр Reality Check.
6. `RC-011_SP-S4-P07_ZERO_DELTA.md` — P07.
7. `RC-012_SP-S4-P08.md` + approval addendum — P08.
8. `RC-013_SP-S4-P09.md` + reanalysis + approval addendum — P09.
9. `RC-014_SP-S4-P10.md` + approval addendum — P10.
10. `SP-S4-P11_ARCHITECT_PASS_NOTES.md` — Architect pass P11.
11. `RC-015_SP-S4-P11.md` + approval addendum — P11.
12. `SP-S4-P12_ARCHITECT_PASS_NOTES.md` — Architect pass P12.
13. `RC-016_SP-S4-P12.md` + Red Team + approval addendum — P12.
14. `SP-S4-P13_ARCHITECT_PASS_NOTES.md` — revised Architect pass P13.
15. `RC-017_SP-S4-P13.md` — revised Reality Check P13.
16. `SP-S4-P13_RED_TEAM_NOTES.md` — revised Red Team / Falsification P13.

## Основной цикл

```text
3 вопроса
→ обсуждение / comparative synthesis
→ Architect pass
→ Reality Check
→ Red Team / Falsification
→ явное решение владельца
→ full theory
→ canonical при самостоятельной дельте
→ parameter delta
→ PROJECT_STATE.yaml
→ derived status sync
→ checkpoint
→ consistency check
```

## Последний закрытый governance cycle

**SP-S4-P12 — «Критерии перехода»** закрыт 4 сентября 2026 года.

> **Не непрерывный контроль, а достаточно надёжное сохранение и функциональное возвращение выбора под релевантной нагрузкой.**

## Активный governance cycle — SP-S4-P13

После первого прохода P13 Андрей уточнил механизм через временной масштаб. Уточнение сохранено как `SP-SRC-025`, после чего Architect pass, RC-017 и Red Team пересобраны.

Surviving candidate:

> **Выбор совершается в моменте. Траектория обнаруживается во времени.**

> **Ловушка S4 — риск того, что правильная ориентация на новый выбор в текущем моменте превращается в почти единственный масштаб оценки, а накопленная серия эпизодов не получает права изменить модель current position.**

Коротко:

> **Ошибка — считать момент достаточным масштабом для оценки траектории.**

Ключевые защиты:

```text
present moment ≠ problem
past = data ≠ verdict
single lapse ≠ trajectory
series ≠ proof of one cause
aggregation ≠ guilt score
macro-awareness ≠ total self-monitoring
```

Zero-delta обязателен, если temporal-scale distinction не добавляет practically useful отличие от P12.

## Текущая остановка

**Последний утверждённый параметр — SP-S4-P12. SP-S4-P13 повторно прошёл Architect / RC-017 / Red Team и ожидает явного решения владельца.**
