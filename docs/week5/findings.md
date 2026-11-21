# Part C — Static-analysis findings

## Ruff findings table

| Rule | Count | Smell (lecture name) | Refactoring |
|---|---:|---|---|
| F401 | 2 | Dead code (unused imports) | Delete the imports |
| PLR2004 | 6 | Magic numbers | Replace with named constants / an enum |
| C901 | 1 | Complex structure | Replace the conditional chain with a rate table / simpler logic |
| PLR0913 | 1 | Too many arguments | Introduce a data object or group related parameters |
| PLR0917 | 1 | Too many positional arguments | Group related parameters into a data object |
| ARG001 | 1 | Unused function argument | Remove the unused argument |
| B006 | 1 | Mutable argument default | Use an immutable tuple default (`extras=()`) |
| E711 / E712 | 1 each | Incorrect singleton comparisons | Use `is None` / `is not None` and direct Boolean conditions |
| F841 | 1 | Unused local variable | Delete `tmp` |
| N802 | 1 | Invalid function name | Rename `ProcessAll` to `process_all` |

My local Ruff run reports 17 findings in total, including PLR0917, which was missing from the handout summary.

## At least three smells Ruff does not report

1. **Mysterious names:** parameters such as `d`, `t`, `y`, `s`, and `disc` do not explain their meaning. Rename them to descriptive names such as `courses`, `student_type`, and `summer`.
2. **Duplicated logic:** `ProcessAll` repeats almost the same `calc` call for different student types. Use one call driven by the student's type.
3. **Mixed responsibilities:** `report` calculates a fee and prints it. Separate calculation from presentation; return a string from the report function.
4. **Primitive obsession / type-code comment:** student categories are represented by unexplained integers 1, 2, and 3. Replace them with a `StudentType` enum.
5. **Hidden state bug:** `ProcessAll` does not assign a fee for scholarship students, so the previous loop iteration's `fee` can be reused.

## Hidden bug explanation

`ProcessAll` has conditions for type 1 and type 2, but no condition for type 3. When Omar (a scholarship student) follows Sara, neither condition assigns a new value to `fee`, so Omar is printed with Sara's previous fee (1050). If the scholarship student is first, `fee` may be undefined and Python raises `UnboundLocalError`. The refactored `process_all` calculates a fee for every student, and a scholarship student's fee is 0.

## One-sentence answer for the hidden-bug task

Omar incorrectly receives Sara's previous fee because the original `ProcessAll` function does not calculate or assign a fee for scholarship students.
