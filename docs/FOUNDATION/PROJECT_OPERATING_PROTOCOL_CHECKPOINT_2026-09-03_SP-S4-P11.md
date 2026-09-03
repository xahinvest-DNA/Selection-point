# Project Operating Protocol Checkpoint — SP-S4-P11

**Дата:** 3 сентября 2026 года  
**Статус:** final approved checkpoint  
**Фаза:** 3 — «Точная архитектура пяти ступеней»  
**Ступень:** 4 — «Сохранение выбора под напряжением»

## Явное решение владельца

Полный цикл:

```text
3 вопроса владельцу
→ гипотезы владельца
→ source / comparative analysis
→ Architect pass
→ Reality Check
→ Red Team / Falsification
→ stage-specific delta recommendation
→ явное решение владельца
```

Андрей ответил:

> **«Утверждаем».**

## Утверждённый результат SP-S4-P11

> **Тренировать цикл выбора под нагрузкой, а не отдельную технику снятия нагрузки.**

Полный смысл:

> **Практики четвёртой ступени тренируют доступность reality-coupled цикла выбора в условиях нагрузки и повторный вход в него после частичного снижения доступности; нагрузка становится частью учебной позиции, но не целью и не мерой зрелости.**

Дополнительная формула:

> **Нагрузка становится частью учебной позиции, а не целью практики.**

## Семь функциональных классов

1. load recognition;
2. relevant reorientation;
3. graded / context-relevant load;
4. available entry;
5. functional move;
6. reality-coupled feedback;
7. recovery / re-entry.

## Обязательные границы

```text
нагрузка ≠ цель практики
выдержать больше стресса ≠ иметь больше выбора
максимальная нагрузка ≠ лучшая тренировка
load-awareness ≠ доказательство потери выбора
«панель управления» ≠ тотальный self-monitoring
state regulation ≠ восстановление выбора
визуализация может помогать ≠ достаточная reality-coupled проверка
feedback ≠ обязательный KPI
```

Практика должна сохранять право реальности скорректировать внутреннюю версию и следующий ход.

## Граница Фазы 5

P11 утверждает функциональный профиль, но не конкретные упражнения, инструкции, дозирование, частоту, длительность или delivery. Эти решения отложены до Фазы 5.

## Зафиксированные источники

- full theory: `FIVE_STAGES_THEORY/50_STAGE_4_CORRESPONDING_PRACTICES.md`;
- canonical: `CANONICAL/40_STAGE_4_P11_CANONICAL.md`;
- local delta: `LIBRARIES/S4_P11_CORRESPONDING_PRACTICES_DELTA.md`;
- source: `SOURCE_MATERIALS/21_2026-09-03_P11_LOAD_DASHBOARD_AND_FEEDBACK.md`;
- Architect pass: `GOVERNANCE/SP-S4-P11_ARCHITECT_PASS_NOTES.md`;
- Reality Check: `GOVERNANCE/RC-015_SP-S4-P11.md`;
- approval: `GOVERNANCE/RC-015_SP-S4-P11_APPROVAL_ADDENDUM.md`.

## Текущая остановка

```text
last approved: SP-S4-P11
active parameter: none
next candidate: SP-S4-P12
next status: unopened
```

**SP-S4-P12 не открывается автоматически.**
