# Daily Trajectory Questionnaire v0.2

> **Operational status update — 11 October 2026.** The Owner disabled the questionnaire and all automatic Selection Point reminders and required the questionnaire to be fully redesigned. This v0.2 artifact is retained only as historical design material. It must not be deployed, automatically delivered, or treated as a current candidate for approval. Questionnaire redesign is not the current course task and starts only when explicitly resumed by the Owner.

**ID:** SP-DTQ-002  
**Status:** withdrawn_pending_full_redesign  
**Date:** 20 September 2026  
**Operational withdrawal:** 11 October 2026  
**Role:** historical longitudinal trajectory telemetry draft  
**Domain:** body / health / physical efficiency  
**Target burden (historical design):** ~2–4 minutes once per evening  
**Not:** Selection Point training, mastery test, psychological scale, medical assessment or composite score.

## 1. Purpose of the historical draft

The questionnaire was designed to create a stable daily observation stream from which a participant's trajectory could later be reconstructed and visualized across multiple time scales.

~~~text
episode
→ day
→ week
→ month
→ quarter
→ 6 months / year
~~~

Each scale answers a different question.

The daily questionnaire was intended to preserve enough continuity to make trends and repeated structures visible without trying to explain the whole person.

This purpose remains useful research context, but the v0.2 instrument itself is not active.

## 2. Core distinction

~~~text
questionnaire = trajectory telemetry
questionnaire ≠ course
questionnaire ≠ Selection Point capability
questionnaire completion ≠ successful day
~~~

The questionnaire may itself influence attention or behavior. This measurement reactivity remains important evidence for the future redesign.

## 3. Historical participant-facing questionnaire

The following questions are preserved as the v0.2 historical draft and are **not currently delivered**.

### 1. Вес

> **Вес сегодня, кг?**

If not measured: `не измерял`.

### 2. Сон

> **Сколько часов спал? Качество сна 1–5?**

### 3. Питание и алкоголь

> **Как прошёл режим питания? Был ли алкоголь? Если да — сколько?**

Short factual answer is enough.

Examples:
- режим соблюдён, без алкоголя;
- питание хаотичное, алкоголь — 1 банка пива;
- порции больше обычного, без алкоголя.

### 4. Тренировка / движение

> **Была тренировка или отдельная физическая активность? Что и сколько? Если нет — кратко почему.**

No moral evaluation.

### 5. Общая активность / нагрузка

> **Общая активность дня: низкая / средняя / высокая? Было ли что-то необычное по нагрузке?**

The second part is optional.

### 6. Состояние

> **Энергия 1–5, боль/дискомфорт 0–10, стресс 0–10.**

These are self-reported state indicators, not diagnoses.

### 7. Вчерашнее намерение → факт

> **Что было выбрано/запланировано на сегодня и что фактически произошло?**

Use one status where useful:

~~~text
реализовано
частично реализовано
не реализовано
обстоятельства изменились
решение изменено после нового факта
не знаю / не могу оценить
~~~

This preserves:

~~~text
intention
≠
realization
~~~

### 8. Один значимый эпизод дня

> **Какой один эпизод сегодня заметно повлиял на состояние или траекторию?**

Answer briefly:

~~~text
что произошло
→ когда я это заметил: до / во время / после / не знаю
→ что я фактически сделал
→ что произошло сразу после
~~~

Important: the questionnaire did not require the participant to identify a hidden motive or a “correct Selection Point.”

### 9. Фактическая позиция на конец дня

> **С какими 1–3 фактами ты входишь в завтра?**

Examples:

- работа не завершена;
- тренировка выполнена;
- алкоголь был / не был;
- еда на завтра приготовлена;
- боль или дискомфорт усилились;
- спал мало и усталость сохраняется;
- важная договорённость выполнена / не выполнена.

The participant was not asked to infer what had become psychologically “more available” or “less available.”

### 10. Одно проверяемое действие на завтра

> **Какое одно конкретное действие завтра поддержит направление “эффективное тело”? Какой первый физический шаг?**

The action could later be revised if reality changed.

## 4. Optional measurement-reactivity note

The v0.2 design did not require a separate mandatory leading question every day.

If the participant spontaneously noticed that future reporting/questionnaire expectation affected behavior, the draft allowed:

> **Опросник/будущий отчёт сегодня повлиял на действие: ...**

No note did not prove there was no measurement effect.

## 5. Why v0.2 differed from the preceding form

The stable body/trajectory fields were retained:

~~~text
weight
sleep
nutrition/alcohol
training
activity/load
energy/pain/stress
intention → fact
end-of-day factual position
tomorrow action
~~~

The main revision was question 8.

The previous form used a more explicitly framed “точка выбора” question.

v0.2 used a neutral event formulation:

~~~text
significant episode
→ noticing timing
→ actual continuation
→ immediate consequence
~~~

Reason:

- a directed question can change attention and behavior;
- retrospective questions can manufacture a coherent alternative after the fact;
- the trajectory instrument should observe first and interpret later.

Therefore the draft avoided requiring:

~~~text
“what else was open?”
or
“what was the correct choice?”
~~~

These may belong to course practice or later analysis, not mandatory daily measurement.

## 6. Multi-timeframe use considered by v0.2

### Episode level

Shows:
- state/context;
- noticing timing;
- actual continuation;
- immediate consequence.

### D1 — day

Shows:
- body state;
- sleep;
- nutrition/alcohol;
- activity;
- training;
- intended vs realized continuation;
- end-of-day factual position.

### W1 — week

Can show:
- weight trend;
- sleep/energy/pain/stress series;
- alcohol frequency/amount;
- training/activity recurrence;
- intended → realized pattern;
- recurring event/context classes;
- recurring changes in end-of-day factual position.

### M1 — month

Can show:
- sustained direction or absence of direction;
- repeated body-state/behavior relationships;
- repeated selected → realized gaps;
- changes in the practical organization of life.

### Quarter / 6M / 1Y

Can show larger trajectory structure only if enough comparable data exist.

~~~text
higher timeframe
= aggregation of traceable lower-level observations
≠ verdict about the person
~~~

## 7. Visualization boundary

Do not collapse questionnaire data into one “health score” or “Selection Capacity score.”

The historical design considered:

- parallel time series;
- event markers;
- weekly/monthly summaries;
- selected → realized traces;
- behavior/activity recurrence;
- state overlays;
- expandable lower-level events.

OHLC or a single synthetic trajectory coordinate remains deferred until there is a defensible underlying measure.

## 8. Data quality rules retained for future redesign

- `unknown` / `не знаю` is valid.
- Missing report ≠ bad day.
- No reported episode ≠ no episode objectively occurred.
- Self-report remains self-report.
- Sequence ≠ causality.
- Measurement may affect behavior.
- Historical versions are not rewritten; version changes are preserved.

## 9. Current status

v0.2 is **withdrawn from operational use and from the approval queue**.

A replacement questionnaire requires a full redesign when the Owner explicitly resumes that work. The redesign must start from purpose and required trajectory information rather than treating v0.2 as the default form to edit.
