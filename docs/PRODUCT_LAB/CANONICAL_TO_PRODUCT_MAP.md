# Canonical → Product Map

**Статус:** skeleton / LAB-0  
**Обновлено:** 15 сентября 2026 года  
**Назначение:** не переводить канон в маркетинг напрямую, а показать, какое пользовательское обучение и наблюдение может быть обосновано утверждённой архитектурой.

## Правило

Каждая будущая обучающая единица должна иметь трассировку:

```text
canonical source
→ functional distinction
→ user capability hypothesis
→ training event hypothesis
→ observable change
→ measurement candidate
→ limits / confounds
```

Если трассировки нет, упражнение или продуктовая формулировка не считается обоснованной Selection Point только потому, что «похожа по духу».

## Поля карты

| Поле | Смысл |
|---|---|
| Canonical source | утверждённый источник Selection Point |
| Functional distinction | какое различение или функция утверждены |
| User capability hypothesis | чему предположительно может научиться человек |
| Training event hypothesis | в каком типе эпизода это можно тренировать |
| Observable change | что должно стать наблюдаемо иначе |
| Measurement candidate | как это можно фиксировать |
| Limits / confounds | альтернативные объяснения и границы вывода |
| Evidence status | untested / exploratory / supported / contradicted |

## LAB-0

На текущем проходе карта не заполняется по всем 5 × 13 параметрам. Сначала определяется минимальная сквозная модель способности выбирать и проверяется её наблюдаемость в owner self-pilot.

Массовое заполнение до этого создаст ложную точность и преждевременное проектирование курса.

## Сквозная рабочая цепочка

После RC-018 обязательна следующая продуктовая проекция:

```text
фактическая позиция
→ доступная Selection Point
→ selected continuation
→ realized continuation
→ consequence
→ observed/interpreted feedback
→ model update
→ новая фактическая позиция
```

## Первый явный mapping — RC-018

| Поле | Рабочая проекция |
|---|---|
| Canonical source | `FOUNDATION/CANONICAL/01B_CORE_CHOICE_ACTION_FEEDBACK_BOUNDARY_CANONICAL.md` |
| Functional distinction | внутренне выбранное продолжение не равно фактически реализованному; последствия не равны автоматически использованному feedback |
| User capability hypothesis | человек может точнее различать намерение, реальное продолжение и ответ реальности без ретроспективного смешения |
| Training event hypothesis | реальный эпизод с предварительным выбором, фактическим продолжением и последующим review |
| Observable change | меньше неразличённых selected→realized gaps; feedback чаще приводит к явному model/next-move update, когда он релевантен |
| Measurement candidate | `Selected → Realized Continuation Rate`, gap classes, Recovery Latency, Feedback→Update trace |
| Limits / confounds | reminders/scaffold, retrospective reconstruction, changed circumstances, new facts, self-report bias, unclear causality |
| Evidence status | exploratory / owner self-pilot only |

### Обязательные ограничения mapping

```text
internal choice = real event
≠ execution evidence

conscious non-action
may be realized continuation

partial execution
→ partial test

selected → realized gap
= data first
≠ moral failure

consequence
≠ automatically feedback
```

## Measurement bridge

Текущие рабочие документы:

- `REALITY_EVENT_MODEL_V0_2.md` — сущности и event trace;
- `PILOT_METRICS_SPEC_V0_1.md` — рабочие показатели;
- `PERSONAL_TRAJECTORY_PILOT_V0.md` — active owner self-pilot.

## Что пока запрещено выводить из карты

Карта не обосновывает автоматически:

- готовое упражнение;
- доказанную trainability;
- универсальный Selection Capacity Score;
- причинный эффект prompts;
- конкретную аудиторию;
- длительность формирования навыка;
- приложение или курс;
- эффективность Selection Point.

Текущая задача карты — сохранять трассировку между каноном и наблюдаемой продуктовой гипотезой, не превращая гипотезу в канон.