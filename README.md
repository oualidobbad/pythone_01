# pythone_01

Python Module 01: intermediate exercises covering data structures, file I/O, object-oriented basics, and functional patterns across 3 exercises (ex0–ex2).

## Project Overview
- What it does: builds on Module 00 with deeper Python exercises — list/dict comprehensions, file manipulation, and basic class design.
- Use cases: intermediate Python practice for students with C/C++ backgrounds.
- Problem solved: transitions from script-level Python to structured, object-oriented code.

## Architecture & Design
- 3 exercise directories (`ex0/`–`ex2/`), each with self-contained `.py` files.
- Subject PDF (`en.subject.pdf`) provides full specifications.
- Exercises increase in complexity: data structures → file I/O → OOP.

## Core Concepts
- List/dict comprehensions and generator expressions.
- File I/O: `open()`, context managers (`with`), `read()`/`write()`/`readlines()`.
- Classes: `__init__`, `__str__`, `__repr__`, instance methods, `self`.
- Error handling: `try/except`, custom exceptions.

### Example: file processing
```python
# Typical exercise pattern
def process_file(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    return [line for line in lines if line]
```

## Installation & Setup
- Requires Python 3.
- Run: `python3 ex0/exercise.py`.

## Usage Guide
- Follow the subject PDF; work through ex0 → ex2 sequentially.
- Test with sample inputs described in the subject.

## Technical Notes
- Pure Python standard library — no pip dependencies.
- Exercises enforce clean error handling and resource management.

## Improvements & Future Work
- Add exercises on decorators and context managers.
- Include pytest test suites for each exercise.

## Author
Oualid Obbad (@oualidobbad)