# Текущая контрольная точка проекта Selection Point

**Статус:** человекочитаемое представление `PROJECT_STATE.yaml`  
**Дата обновления:** 5 сентября 2026 года  
**Авторитетный источник:** `PROJECT_STATE.yaml`

## 1. Текущий статус

- Фаза 3 — «Точная архитектура пяти ступеней».
- Ступени 1–3 завершены полностью.
- Ступень 4: **SP-S4-P01–SP-S4-P12 утверждены**, P07 и P09 = `zero-delta`.
- Последний утверждённый параметр: **SP-S4-P12 — «Критерии перехода»**.
- Активный параметр: **SP-S4-P13 — «Ловушка четвёртой ступени»**.
- После owner refinement P13 повторно прошёл **Architect pass, RC-017 и Red Team / Falsification**.
- Статус P13: **owner-decision-pending**.

## 2. Новое уточнение P13

Рабочий источник:

- `SOURCE_MATERIALS/25_2026-09-05_P13_TEMPORAL_SCALE_AND_TRAJECTORY.md` — SP-SRC-025.

Предшествующий источник:

- `SOURCE_MATERIALS/24_2026-09-05_P13_COMPENSATION_THINKING_AND_REALITY_CONTACT.md` — SP-SRC-024.

Центральное owner-различение:

> **Выбор совершается в моменте. Траектория обнаруживается во времени.**

И:

> **Прошлое не должно определять следующий выбор, но релевантная история должна иметь право изменить описание текущей позиции.**

## 3. Surviving candidate после revised Architect / RC / Red Team

> **Ловушка S4 возникает, когда полезная способность возвращаться к доступному выбору в каждом отдельном моменте непреднамеренно превращает moment-level view в основной и почти единственный масштаб оценки. Тогда серия функционально сходных эпизодов может не получить достаточного веса как новая фактическая позиция, и человек локально остаётся в выборе, одновременно недооценивая устойчивое изменение собственной траектории во времени.**

Коротко:

> **Ошибка — считать момент достаточным масштабом для оценки траектории.**

## 4. Дельта относительно P12

P12:

```text
отдельное выпадение не отменяет освоение
→ functional re-entry остаётся возможным
```

P13 candidate:

```text
каждый новый выбор остаётся возможным
но
серия выпадений сама становится feedback
→ history must update current-position model
```

Право на новый выбор **не равно** праву обнулить накопленную информацию.

## 5. Обязательные ограничения

```text
present moment ≠ problem
past = data ≠ verdict / identity / destiny
single lapse ≠ trajectory
series ≠ proof of one hidden cause
aggregation ≠ guilt score
negative outcomes alone ≠ negative trajectory
macro-awareness ≠ total self-monitoring
```

Временной горизонт не задаётся универсально в Фазе 3.

## 6. External compatibility

RC-017 обнаружил совместимость отдельных компонентов с:

- различением lapse / relapse в behaviour-maintenance literature;
- EMA-различением локальных процессов и unfolding trajectory;
- моделями поведения во времени и контексте;
- context-dependent relapse / habit literature.

Это не доказывает пятиступенчатую архитектуру и не задаёт универсальный период агрегации.

## 7. Zero-delta condition

P13 должен стать `zero-delta` / быть пересмотрен, если temporal aggregation не добавляет practically useful distinction к P12, если окно всегда выбирается post hoc, если macro-review неизбежно создаёт guilt / hyper-control или если невозможно наблюдаемо показать случай, где local recovery работает, но trajectory-level feedback систематически недоучитывается.

## 8. Активные документы

- `SOURCE_MATERIALS/25_2026-09-05_P13_TEMPORAL_SCALE_AND_TRAJECTORY.md`;
- `SOURCE_MATERIALS/24_2026-09-05_P13_COMPENSATION_THINKING_AND_REALITY_CONTACT.md`;
- `GOVERNANCE/SP-S4-P13_ARCHITECT_PASS_NOTES.md`;
- `GOVERNANCE/RC-017_SP-S4-P13.md`;
- `GOVERNANCE/SP-S4-P13_RED_TEAM_NOTES.md`.

## 9. Текущая рабочая точка

**SP-S4-P13 повторно прошёл Architect pass, RC-017 и Red Team после temporal-scale refinement. Параметр ожидает явного решения Андрея. Full theory / canonical / delta пока не создаются.**
