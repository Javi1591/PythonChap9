# Program 9 – Dictionary and Course Grade Analysis

A Python program that demonstrates the use of dictionaries to store, process, and modify course grades.  
This project emphasizes the use of key-value pairs, loops, and aggregate calculations such as averages and lowest scores.

---

## Description
The program allows a user to enter multiple course codes and their corresponding numeric grades (as percentages).  
After data entry, it calculates and displays:
- Each course and its grade.
- The current term average.
- The lowest-scoring course, which is then removed.
- The revised course list and the new average after dropping the lowest grade.

---

## Features
- Uses a **dictionary** to store course names as keys and grades as values.
- Allows unlimited input until the user presses Enter with no text.
- Calculates both **average grade** and **lowest-scoring course** dynamically.
- Demonstrates the `items()` and `keys()` dictionary methods for iteration.
- Provides formatted numeric output with one decimal precision.

---

## Core Logic
1. Initialize an empty dictionary named `grades`.
2. Continuously prompt for course codes and corresponding grades inside a `while` loop.
3. Use a `for` loop to:
   - Display each course and grade.
   - Calculate total and average scores.
   - Determine the lowest course grade using the `min()` function.
4. Display the lowest grade and simulate dropping that course.
5. Recalculate and print the updated course list and the revised average using the `items()` method.

---

## Input Validation
- User must input integer grades.
- Loop terminates cleanly when the user presses **Enter** with no course name.

---

## Build & Run

### Requirements
- Python 3.8 or newer

### Execution
Run the program from a terminal or command prompt:
```bash
python program9_1.py
