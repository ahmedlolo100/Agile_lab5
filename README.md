# SET 312 Agile Software Engineering — Lab 5 solution

## Contents
- `week5/grades.py`, `week5/test_grades.py`: Part B letter-grade kata and boundary tests.
- `week5/legacy_fees.py`: original legacy code from the handout, kept unchanged for comparison.
- `week5/fees.py`, `week5/test_fees.py`: Part D refactoring and characterization tests.
- `docs/week5/findings.md`: Part C findings, extra smells, and hidden-bug explanation.
- `docs/week5/before.txt`: Ruff summary supplied by the handout; add your actual Pylint output.
- `docs/week5/after.md`: before/after table and reflection draft.

## Setup (Windows PowerShell / VS Code terminal)
From the project root:

```bash
python --version
python -m venv .venv
.venv\Scripts\activate
pip install pytest ruff pylint
```

## Run tests and analysis

```bash
python -m pytest -v
ruff check week5
ruff format week5
pylint week5/fees.py
pylint week5/legacy_fees.py
```

The supplied tests should pass. Ruff may report issues in `legacy_fees.py` intentionally: it is the unmodified baseline used for Part C. Run Ruff on that file separately to capture the original report:

```bash
ruff check week5/legacy_fees.py --statistics
```

## Git workflow

The handout asks for branch `week5-quality`, a separate commit for each meaningful TDD/refactoring cycle, and a co-author line on the paired cleanup commit. Example:

```bash
git switch -c week5-quality
git add .
git commit -m "Add letter_grade and tests"
git commit -m "Add boundary tests"
git commit -m "Refactor tuition fee calculation"
git push -u origin week5-quality
```

For the paired commit, use the actual partner's name and email:

```bash
git commit -m "Clean up letter_grade" -m "Co-authored-by: Partner Name <partner@example.com>"
```

Then open a pull request from `week5-quality` to `main`. Do not invent a partner identity or email.

## Important submission checks
- Save your real Ruff/Pylint terminal output in `docs/week5/before.txt`.
- Replace the local measurement placeholders in `docs/week5/after.md`.
- Edit the reflection so it describes what you and your partner actually did.
- Submit the pull-request link on the LMS.
