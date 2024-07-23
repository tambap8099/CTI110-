# Peter Tamba
# 6/27/2024
# P2HW2
# This program collects grades for six modules, stores them in a list, and displays the lowest grade, highest grade, sum of grades, and average of grades.

# Collect grades

grades = []
grades.append(float(input("Enter grade for Module 1: ")))
grades.append(float(input("Enter grade for Module 2: ")))
grades.append(float(input("Enter grade for Module 3: ")))
grades.append(float(input("Enter grade for Module 4: ")))
grades.append(float(input("Enter grade for Module 5: ")))
grades.append(float(input("Enter grade for Module 6: ")))

# Calculate required values

lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average_grade = sum_of_grades / len(grades)

# Display results

print("\n------------Results------------")
print(f"Lowest Grade:       {lowest_grade:.1f}")
print(f"Highest Grade:      {highest_grade:.1f}")
print(f"Sum of Grades:      {sum_of_grades:.1f}")
print(f"Average:            {average_grade:.2f}")
print("------------------------------")
