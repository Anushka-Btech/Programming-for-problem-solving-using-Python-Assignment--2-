### Programming-for-problem-solving-using-Python-Assignment--2-
##GradeBook Analyzer

## Project Summary
Lecturers need a fast, accurate way to compute statistics on student marks. This CLI-based GradeBook Analyzer reads student marks either via manual input or from a CSV file, computes summary statistics, assigns letter grades, counts distribution, filters pass/fail students, and prints a formatted table. Optionally it exports the final grade table to CSV.

## Features (fulfills Tasks 1-6)
- Menu-driven CLI with manual / CSV input.
- Data stored in Python dictionaries.
- Statistical functions: average, median, min, max.
- Letter grade assignment: A (90+), B (80–89), C (70–79), D (60–69), F (<60).
- Grade distribution counts (A–F).
- Pass/Fail lists via list comprehension (pass threshold 40).
- Formatted results table and loop to repeat analysis.
- Bonus: export final table to CSV.

## Files
- `gradebook.py` — main script.
- `Student.csv` — sample CSV for testing.

## How to run
1. Place `gradebook.py` and `Student.csv` in same folder.
2. Open terminal/command prompt and `cd` to that folder.
3. Run `python3 gradebook.py` (or `python gradebook.py` on Windows).
4. Choose option `1` (manual) or `2` (CSV), follow prompts.

## Testing
- Manual: test with at least 5 students.
- CSV: use `Student.csv` provided (7 students sample included in it).

## Notes on evaluation rubric
- The script is modularized with functions for each task.
- Data validation and CSV reading include checks & helpful debug messages.
- Code comments explain each block; functions are reusable and testable.
- The final output is reproducible and optionally exportable as CSV for grading evidence.

