# Pilot Metrics Specification v0.1

**Статус:** working measurement specification / unvalidated  
**Дата:** 15 сентября 2026 года  
**Основание:** `REALITY_EVENT_MODEL_V0_2.md` + RC-018  
**Правило:** метрики описывают наблюдаемую структуру пилота; они не являются шкалой личности или доказательством эффективности Selection Point.

## 1. Принципы измерения

1. Не смешивать `Choice`, `Realization`, `Consequence` и `Feedback`.
2. Не присваивать произвольные веса частичному исполнению.
3. Не превращать `non_match` в автоматический диагноз слабой воли или саботажа.
4. Всегда сохранять признак `prompt_exposure`, чтобы отличать самостоятельное функционирование от поведения под scaffold.
5. Не строить единый композитный score до появления эмпирического основания.
6. Любая агрегированная метрика должна быть разворачиваема до исходных эпизодов.

## 2. M1 — Selected → Realized Continuation Rate

**Вопрос:** какая доля оценимых выбранных продолжений была реализована в соответствии с выбором?

```text
SRCR = count(match) / count(evaluable selected continuations)
```

Где `evaluable` исключает только записи со статусом `not_evaluable/unknown`, если невозможно установить фактическое продолжение.

Отдельно показываются:

```text
match
partial_match
non_match
not_evaluable
```

`partial_match` не получает произвольный коэффициент 0.5 и не включается в числитель основной метрики.

Обязательные срезы:

- with scaffold / without scaffold;
- planned / in-the-moment choice;
- circumstances changed / unchanged;
- context domain.

## 3. M2 — Plan Recall Loss

**Вопрос:** какая часть вечерних планов отсутствует в доступном поле участника утром до раскрытия системой?

Строго измерить показатель можно только если существует **pre-prompt recall observation**.

```text
PRL = planned continuations not recalled before reveal
      / planned continuations due for recall
```

Если интерфейс сразу показывает план, `Plan Recall Loss` **не измеряется**, а помечается `not_observed`.

Это важно: нельзя выводить забывание из последующего неисполнения.

## 4. M3 — Prompted vs Unprompted Realization

**Вопрос:** какая часть фактических продолжений произошла после внешнего scaffold и какая — без непосредственного prompt?

Для каждого `RealizationRecord` фиксируется:

```text
prompt_exposure = none | plan_recall | trajectory_check | other_scaffold | unknown
```

Минимальный отчёт:

```text
realizations_without_prompt
realizations_after_plan_recall
realizations_after_trajectory_check
unknown_prompt_exposure
```

Эта метрика не утверждает причинность prompt → action. Она лишь делает confound видимым.

## 5. M4 — Recovery Latency

**Вопрос:** сколько времени проходит между обнаруженным отклонением и первым фактически реализованным продолжением, вновь совместимым с актуальным направлением?

```text
recovery_latency = timestamp(first aligned realized continuation)
                   - timestamp(deviation detected)
```

Обязательные поля:

- `deviation_detected_at`;
- `recovery_realization_at`;
- `recovery_status: observed | censored | direction_revised | not_applicable`.

Если релевантные факты привели к пересмотру направления, это не считается «неудавшимся восстановлением».

## 6. M5 — Selected → Realized Gap Reasons

**Вопрос:** какие наблюдаемые классы чаще сопровождают несовпадение выбранного и реализованного продолжения?

Допустимые классы только при наличии данных:

```text
circumstances_changed
new_fact_changed_choice
forgotten
automatic_reaction
physical_constraint
planning_error
conscious_revision
unknown
```

Отчёт — распределение эпизодов, а не причинная модель.

## 7. M6 — Repeated Selection-Point Pattern

**Вопрос:** повторяется ли одна и та же наблюдаемая структура перед изменением траектории?

Минимальная единица паттерна:

```text
context/event class
→ state or interpretation marker
→ selected continuation
→ realized continuation
→ immediate consequence
```

Паттерн считается **candidate pattern**, а не установленным механизмом, пока:

- не повторился несколько раз;
- не найдено альтернативное объяснение;
- следующий эпизод не даёт возможности проверить ожидание.

На v0.1 порог повторений специально не утверждается.

## 8. Multi-timeframe report

Первый отчёт должен показывать не одну итоговую цифру, а набор наблюдений на уровнях:

```text
episode
→ day
→ week
→ month
```

Минимум для недели:

- число выбранных продолжений;
- `match / partial / non_match / not_evaluable`;
- prompt exposure;
- число unexpected events;
- recovery episodes и их latency;
- повторяющиеся candidate patterns;
- изменения направления, вызванные новыми фактами.

## 9. Что пока не измеряем

До отдельного обоснования не вводятся:

- общий `Selection Capacity Score`;
- `Trajectory Score`;
- OHLC по искусственному индексу;
- «процент осознанности»;
- «процент саботажа»;
- эффективность метода по одному self-pilot;
- причинный эффект напоминаний без сравнительного дизайна.

## 10. Критерий качества метрики

Каждая метрика должна отвечать на три вопроса:

1. Какие конкретные события входят в числитель и знаменатель?
2. Какие данные могут сделать значение `unknown/not_observed`?
3. Какое более сильное заключение **нельзя** делать из этой цифры?

Если хотя бы на один вопрос нет ответа, показатель остаётся названием идеи, а не рабочей метрикой.