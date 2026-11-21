# Part D — Before/after results

| Measure | Before (`legacy_fees.py`) | After (`fees.py`) |
|---|---:|---:|
| Ruff issues (total) | 17 | 0 |
| Highest cyclomatic complexity | 9 (`calc`) | Record the value from your local Ruff/Pylint report |
| Arguments of the main function | 6 | 5 (`tuition_fee`) |
| Pylint score (/10) | 4.86/10 | 10.00/10 |
| Tests passing | 0 (no tests) | 18 with the supplied grade and fee tests |

## Pair-programming reflection (edit to match your actual experience)

Driver: I focused on implementing the current change and explaining my decisions while typing.  
Navigator: I reviewed the code, checked edge cases, and suggested tests before changes were made.  
Pair programming helped us find mistakes earlier and share knowledge of the code.  
The main cost was that two people had to coordinate and take turns during the task.

## Note

Run the commands in the README and replace the measurement placeholders with your own terminal results before submission.
