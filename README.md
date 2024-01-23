# Riddle Challenge

Rick is a fan of logic-based games, but he's grown tired of Sudoku and Mastermind. He recently discovered a new game that involves replacing question marks in a string with letters, following a specific rule: no two consecutive letters can be the same.

## Task

Write a function named `solution(riddle)` that takes a string `riddle` containing lowercase letters and question marks ("?") as input. The function should return a copy of the string with all question marks replaced by lowercase letters such that no two consecutive letters are the same. Any valid solution that meets this requirement is acceptable.

## Examples

**Input:**

```python

riddle = "ab?ac?"

# Possible Outputs:
"abcaca"
"abzacd"
"abfacf"

# Other Examples:
solution("rd?e?wg??")  # Possible output: "rdveawgab"
solution("????????")  # Possible output: "codility"
```

## Assumptions

- The length of the string `riddle` is within the range [1..100,000].
- The string `riddle` consists only of lowercase letters (a-z) or question marks ("?").
- It is always possible to solve the riddle and create a string without two identical consecutive letters.

## Algorithm Efficiency

Consider performance optimization techniques when designing your algorithm, especially for longer riddles.

## Usage

The file `main.py` runs the script `rick_riddle.py` that solves the challenge. Its necesary to create a folder calles `files` with two .txt files: `inputs.txt` and `outputs.txt`.

```bash
python3 main.py
```

The file `test_solution.py` contains all the tests cases for this solution. It's necesary to have pytest installed.

```bash
python3 pytest test_solution.py
```