# Delta — Core choice/action/feedback boundary

**Статус:** approved cross-cutting delta  
**Дата:** 15 сентября 2026 года  
**RC:** RC-018

## Новая practically useful дельта

До RC-018 ядро Selection Point уже содержало последовательность:

```text
выбор
→ действие
→ последствия
→ обратная связь
```

Но не было достаточно жёстко зафиксировано, что внутренне выбранный ход может не стать фактически реализованным.

Утверждённая дельта:

```text
selected continuation
≠ realized continuation
```

и поэтому:

```text
feedback на действие
требует, чтобы соответствующее действие фактически произошло
```

## Ключевая формула

> **Выбрать ≠ сделать. Сделать ≠ получить желаемое. Последствия ≠ автоматически использованная обратная связь.**

## Диагностическая функция

Теперь различаются два самостоятельных вопроса:

```text
Что было выбрано?
≠
Что фактически произошло?
```

При несовпадении исследуется execution gap без автоматической моральной интерпретации.

## Ограничения

```text
internal choice = real event
selected ≠ realized ≠ sabotage by default
conscious non-action may be realized continuation
partial execution gives partial test only
action ≠ guaranteed desired outcome
action ≠ guaranteed causal clarity
```

## Связь

- Full foundation: `../CORE_CHOICE_ACTION_FEEDBACK_BOUNDARY.md`
- Canonical: `../CANONICAL/01B_CORE_CHOICE_ACTION_FEEDBACK_BOUNDARY_CANONICAL.md`
- Reality Check: `../GOVERNANCE/RC-018_CORE_CHOICE_ACTION_FEEDBACK.md`
- Approval: `../GOVERNANCE/RC-018_CORE_CHOICE_ACTION_FEEDBACK_APPROVAL_ADDENDUM.md`
