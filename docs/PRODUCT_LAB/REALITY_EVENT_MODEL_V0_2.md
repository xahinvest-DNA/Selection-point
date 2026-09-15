# Reality Event Model v0.2

**Статус:** working research schema / Product Lab  
**Дата:** 15 сентября 2026 года  
**Основание:** RC-018 `choice → realized continuation → feedback`  
**Не является:** доказанной психологической моделью, медицинской схемой или готовой продуктовой БД.

## 1. Назначение

Эта схема задаёт минимальный язык данных для Reality Loop так, чтобы Selection Point не смешивал:

```text
что человек видел
≠ что выбрал
≠ что фактически произошло в его поведении
≠ что произошло после этого
≠ что было замечено как данные
≠ что реально изменило следующий цикл
```

Главная граница RC-018:

> **Selected continuation ≠ realized continuation.**

Неисполненный выбор остаётся реальным внутренним событием, но не считается совершённым ходом и не получает внешней проверки как неслучившееся действие.

## 2. Минимальная цепочка Reality Loop

```text
PositionSnapshot
→ SelectionPointEvent
→ ChoiceRecord
→ RealizationRecord
→ ConsequenceRecord
→ FeedbackRecord
→ ModelUpdateRecord
→ next PositionSnapshot
```

`UnexpectedEvent` может возникнуть между любыми двумя узлами и изменить фактическую позицию.

## 3. Сущности

### 3.1. PositionSnapshot

Что релевантно известно о текущей позиции в момент фиксации.

Минимальные поля:

```text
position_id
participant_id
timestamp
context_domain
relevant_facts
state_notes_optional
direction_id_optional
source: self_report | observation | system
```

`state_notes` — данные, а не диагноз.

### 3.2. SelectionPointEvent

Момент, в котором дальнейшее продолжение ещё не полностью определено уже произошедшим автоматизмом или внешними ограничениями.

```text
selection_point_id
position_id
timestamp_detected
detected_by: participant | prompt | retrospective_review
available_continuations_optional
constraints_known_optional
```

Наличие нескольких вариантов не обязательно. Объективно единственный доступный ход не означает потерю Selection Capacity.

### 3.3. ChoiceRecord

Что участник внутренне выбрал как следующее продолжение.

```text
choice_id
selection_point_id
timestamp_selected
selected_continuation
selection_basis_optional
expected_first_step_optional
```

`ChoiceRecord` не является доказательством исполнения.

### 3.4. RealizationRecord

Что фактически произошло после выбора.

```text
realization_id
choice_id_optional
started_at_optional
ended_at_optional
realized_continuation
execution_status
evidence_type
prompt_exposure
notes_optional
```

Допустимые `execution_status`:

```text
executed
partially_executed
conscious_non_action
not_executed
circumstances_changed
revised_after_new_fact
forgotten
unknown
```

Правила:

- `conscious_non_action` может быть полноценным realized continuation, если именно невмешательство было выбранным и фактически выдержанным продолжением;
- `partially_executed` даёт частичный тест, а не автоматически успех или провал;
- `circumstances_changed` не равняется саботажу;
- `revised_after_new_fact` может быть функциональным изменением решения;
- `forgotten` фиксирует разрыв доступности плана, но не объясняет его причину;
- `unknown` предпочтительнее выдуманной классификации.

`prompt_exposure`:

```text
none
plan_recall
trajectory_check
other_scaffold
unknown
```

Это поле необходимо, чтобы позже отличать самостоятельное функционирование от поведения под внешним scaffold.

### 3.5. UnexpectedEvent

Факт, который не входил в исходный план и мог изменить позицию.

```text
unexpected_event_id
participant_id
timestamp
event_class
intensity_optional
position_change_optional
linked_choice_id_optional
linked_realization_id_optional
```

Конкретные данные о третьих лицах не должны храниться в публичном репозитории.

### 3.6. ConsequenceRecord

Наблюдаемое непосредственное или отложенное последствие реализованного продолжения.

```text
consequence_id
realization_id
timestamp_observed
observation_window
observed_consequence
source
causal_confidence: unknown | low | moderate | high
```

`causal_confidence` — дисциплина интерпретации, а не статистическое доказательство причинности.

### 3.7. FeedbackRecord

Что из последствий или новых фактов было замечено как релевантная информация.

```text
feedback_id
consequence_id_optional
timestamp_noticed
noticed_data
interpretation_optional
contradicts_previous_model: yes | no | unclear
```

Последствие, которое не было замечено или не повлияло на модель, не следует автоматически считать использованным feedback.

### 3.8. ModelUpdateRecord

Что изменилось в следующем рабочем представлении или продолжении.

```text
model_update_id
feedback_id_optional
timestamp
previous_assumption_optional
updated_assumption_optional
next_continuation_change_optional
direction_change_optional
```

Отсутствие изменения допустимо и само по себе не является ошибкой.

## 4. Selected → Realized gap

Центральный исследовательский объект:

```text
selected_continuation
vs
realized_continuation
```

Минимальная классификация отношения:

```text
match
partial_match
non_match
not_evaluable
```

Это **описание данных**, а не оценка личности.

`non_match` может возникнуть из-за:

- изменившихся обстоятельств;
- нового факта;
- забывания;
- автоматической реакции;
- сознательного пересмотра;
- физического ограничения;
- ошибки планирования;
- неизвестной причины.

Причина не присваивается без наблюдаемого основания.

## 5. Временная структура

Каждая запись должна поддерживать минимум четыре масштаба:

```text
episode → day → week → month
```

`quarter` допустим после накопления достаточного числа наблюдений.

Агрегация не имеет права уничтожать трассировку к исходным событиям.

## 6. Что не вводится в v0.2

Схема сознательно не содержит:

- универсального score Selection Capacity;
- морального балла дня;
- автоматического диагноза `саботаж`;
- единого числового `trajectory score`;
- обязательного OHLC-представления;
- вывода о причине только из последовательности событий;
- медицинских или психотерапевтических интерпретаций.

## 7. Критерий пригодности схемы

Схема полезна только если по записи можно восстановить различие:

```text
что было выбрано
→ что было реализовано
→ что произошло после
→ что стало данными
→ что изменилось в следующем цикле
```

Если эти различия теряются, Reality Loop снова превращается в ретроспективный рассказ вместо проверяемой цепочки.