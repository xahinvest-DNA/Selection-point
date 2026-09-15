# Governance Selection Point

**Статус:** действующий индекс управления проектом  
**Дата обновления:** 15 сентября 2026 года

## Действующие документы

1. `../PROJECT_STATE.yaml` — единственный источник текущего статуса параметров.
2. `../PROJECT_OPERATING_PROTOCOL.md` — process protocol v4.1.
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
16. `SP-S4-P13_RED_TEAM_NOTES.md` — revised Red Team P13.
17. `RC-017_SP-S4-P13_APPROVAL_ADDENDUM.md` — явное утверждение P13.
18. `CORE_CHOICE_ACTION_FEEDBACK_ARCHITECT_PASS_NOTES.md` — Architect pass сквозной boundary choice → realized continuation.
19. `RC-018_CORE_CHOICE_ACTION_FEEDBACK.md` — Reality Check этого boundary.
20. `CORE_CHOICE_ACTION_FEEDBACK_RED_TEAM_NOTES.md` — Red Team / Falsification.
21. `RC-018_CORE_CHOICE_ACTION_FEEDBACK_APPROVAL_ADDENDUM.md` — явное утверждение RC-018.

## Основной цикл

```text
3 вопроса для нового архитектурного параметра
→ обсуждение / comparative synthesis
→ Architect pass
→ Reality Check
→ Red Team / Falsification
→ явное решение владельца
→ PROJECT_STATE.yaml first
→ approved full / canonical layers
→ delta / libraries
→ derived status sync
→ checkpoint
→ consistency check
```

Для сквозных уточнений уже утверждённого ядра действует тот же Architect / Reality Check / Red Team / owner-decision принцип, но обязательные три вопроса не добавляются механически, если новый параметр не открывается.

## Последний закрытый parameter cycle

**SP-S4-P13 — «Ловушка четвёртой ступени»** закрыт 5 сентября 2026 года.

> **Выбор совершается в моменте. Траектория обнаруживается во времени.**

> **Ошибка — считать момент достаточным масштабом для оценки траектории.**

Ступень 4 завершена полностью.

## Последний закрытый cross-cutting review — RC-018

15 сентября 2026 года после Architect pass, Reality Check и Red Team Андрей явно утвердил boundary:

> **Внутренне выбранное продолжение не равно фактически реализованному продолжению.**

Коротко:

```text
выбрать ≠ сделать
сделать ≠ получить желаемое
последствия ≠ автоматически feedback
```

Обязательные защиты:

```text
internal choice remains real
selected ≠ realized ≠ moral failure
conscious non-action may be realized continuation
partial execution → partial test
action ≠ clear causal attribution automatically
```

RC-018 утверждён как cross-cutting clarification, не как SP-HCM-10.

Утверждённые файлы:

- `../CORE_CHOICE_ACTION_FEEDBACK_BOUNDARY.md`;
- `../CANONICAL/01B_CORE_CHOICE_ACTION_FEEDBACK_BOUNDARY_CANONICAL.md`;
- `../LIBRARIES/CORE_CHOICE_ACTION_FEEDBACK_BOUNDARY_DELTA.md`;
- `RC-018_CORE_CHOICE_ACTION_FEEDBACK_APPROVAL_ADDENDUM.md`;
- `../PROJECT_OPERATING_PROTOCOL_CHECKPOINT_2026-09-15_RC-018.md`.

## Текущая остановка

**Ступень 4 завершена. RC-018 закрыт как owner-approved. SP-S5-P01 не открыт.**
