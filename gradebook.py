# -------------------------------------------------------------
# GradeBook Analyzer
# Author: Anushka 
# Date: 25th December, 2025
# Description: A CLI tool to analyze student grades and marks.
# -------------------------------------------------------------

import csv

# ---------------------- Task 3: Statistical Functions ----------------------

def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict) if marks_dict else 0


def calculate_median(marks_dict):
    scores = sorted(marks_dict.values())
    n = len(scores)
    if n == 0:
        return 0
    if n % 2 == 1:
        return scores[n // 2]
    return (scores[n//2 - 1] + scores[n//2]) / 2


def find_max_score(marks_dict):
    return max(marks_dict.values()) if marks_dict else None


def find_min_score(marks_dict):
    return min(marks_dict.values()) if marks_dict else None


# ---------------------- Task 2: Input Methods ----------------------

def manual_input():
    marks = {}
    count = int(input("Enter number of students: "))
    for _ in range(count):
        name = input("Enter student name: ")
        score = float(input("Enter marks: "))
        marks[name] = score
    return marks


def load_csv():
    filename = input("Enter CSV filename: ")
    marks = {}

    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 2:
                    marks[row[0]] = float(row[1])
        print("CSV loaded successfully!")

    except FileNotFoundError:
        print("File not found.")

    return marks


# ---------------------- Task 4: Grade Assignment ----------------------

def assign_grades(marks):
    grades = {}
    for name, score in marks.items():
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"
        grades[name] = grade
    return grades


def grade_distribution(grades):
    dist = {"A":0, "B":0, "C":0, "D":0, "F":0}
    for g in grades.values():
        dist[g] += 1
    return dist


# ---------------------- Task 5: Pass / Fail ----------------------

def pass_fail_lists(marks):
    passed = [name for name, score in marks.items() if score >= 40]
    failed = [name for name, score in marks.items() if score < 40]
    return passed, failed


# ---------------------- Task 6: Result Table ----------------------

def print_table(marks, grades):
    print("\nName\t\tMarks\tGrade")
    print("--------------------------------------------")
    for name in marks:
        print(f"{name}\t\t{marks[name]}\t{grades[name]}")


# ---------------------- Main Program ----------------------

def main():
    print("===== Welcome to GradeBook Analyzer =====")
    print("1. Manual Input")
    print("2. Load CSV File")
    print("3. Exit Program")

    while True:
        choice = input("\nEnter your choice: ")

        if choice == "1":
            marks = manual_input()

        elif choice == "2":
            marks = load_csv()

        elif choice == "3":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid option. Try again.")
            continue

        if not marks:
            print("No data to analyze.")
            continue

        # Statistics
        avg = calculate_average(marks)
        median = calculate_median(marks)
        mx = find_max_score(marks)
        mn = find_min_score(marks)

        # Grades
        grades = assign_grades(marks)
        dist = grade_distribution(grades)

        # Pass/Fail
        passed, failed = pass_fail_lists(marks)

        # Output
        print("\n===== Analysis Summary =====")
        print(f"Average Marks: {avg:.2f}")
        print(f"Median Marks : {median:.2f}")
        print(f"Highest Marks: {mx}")
        print(f"Lowest Marks : {mn}")

        print("\nGrade Distribution:", dist)
        print("\nPassed Students:", passed)
        print("Failed Students:", failed)

        print_table(marks, grades)


main()

# End of GradeBook Analyzer
