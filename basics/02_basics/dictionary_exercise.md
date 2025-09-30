# Dictionary Exercise: Student Grade Manager

Create a comprehensive student grade management system using dictionaries. This exercise will help you practice various dictionary operations and real-world data manipulation scenarios.

## Part 1: Basic Setup

Create a dictionary called `students` where:
- Keys are student names (strings)
- Values are dictionaries containing student information with keys: `'age'`, `'grades'` (list of grades), and `'subjects'` (list of subjects)

Example structure:
```python
students = {
    "Alice": {
        "age": 20,
        "grades": [85, 92, 78],
        "subjects": ["Math", "Physics", "Chemistry"]
    },
    "Bob": {
        "age": 19,
        "grades": [90, 87, 95],
        "subjects": ["Biology", "Chemistry", "English"]
    }
}
```

**Task**: Add at least 5 students with different ages, grades, and subjects.

## Part 2: Dictionary Operations

Complete the following tasks:

1. **Add a new student**: Write code to add a new student to the dictionary
2. **Update grades**: Add a new grade to an existing student's grade list
3. **Remove a student**: Remove a student from the dictionary
4. **Check if student exists**: Write code that checks if a student name exists in the dictionary

## Part 3: Data Analysis

1. **Calculate average grade**: For each student, calculate their average grade and store it in a new key `'average'`
2. **Find top performer**: Find the student with the highest average grade
3. **Subject popularity**: Count how many students are taking each subject (use a dictionary to store counts)
4. **Grade distribution**: Create a dictionary that shows how many students fall into different grade ranges:
   - "A" (90-100)
   - "B" (80-89) 
   - "C" (70-79)
   - "D" (60-69)
   - "F" (below 60)

## Part 4: Advanced Operations

1. **Nested dictionary access**: Write a function that safely gets a student's information, returning `None` if the student doesn't exist
   ```python
   def get_student_info(students_dict, student_name):
       # Your code here
       pass
   ```

2. **Dictionary comprehension**: Use dictionary comprehension to create a new dictionary with only students who have an average grade above 80

3. **Merge dictionaries**: Create two separate dictionaries of students and merge them into one

4. **Sort students**: Create a sorted list of students based on their average grades (highest to lowest)

## Part 5: Bonus Challenge

Create a simple menu-driven program that allows users to:
- View all students and their information
- Add a new student
- Update student grades
- Delete a student
- View statistics (top performer, subject popularity, grade distribution)
- Search for a student by name

Example menu:
```
=== Student Grade Manager ===
1. View all students
2. Add new student
3. Update student grades
4. Delete student
5. View statistics
6. Search student
7. Exit

Choose an option (1-7):
```

## Learning Objectives

This exercise covers key dictionary concepts:
- Dictionary creation and initialization
- Accessing, adding, updating, and deleting items
- Nested dictionaries
- Dictionary methods (`.keys()`, `.values()`, `.items()`, `.get()`)
- Dictionary comprehensions
- Error handling with dictionaries
- Practical data manipulation scenarios

## Hints

- Use `dict.get(key, default)` for safe access to dictionary values
- Remember that dictionary keys are case-sensitive
- Use `in` operator to check if a key exists in a dictionary
- Consider using `try/except` blocks for error handling
- The `sum()` function can calculate totals from lists of grades
- Use `max()` and `min()` functions with appropriate key functions for finding extremes

Good luck with your dictionary adventure! 🐍📚