# Peter Tamba
# 7/5/2024
# P3HW2 
# This program calculates the salary of an employee based on their hourly wage,
# hours worked, and overtime.

# Function to calculate salary
def calculate_salary(name, hours, rate):
    if hours > 40:
        overtime_hours = hours - 40
        regular_hours = 40
    else:
        overtime_hours = 0
        regular_hours = hours
    
    overtime_pay = overtime_hours * (rate * 1.5)
    regular_pay = regular_hours * rate
    gross_pay = regular_pay + overtime_pay
    
    return regular_hours, overtime_hours, regular_pay, overtime_pay, gross_pay

# Get employee details
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Calculate salary
regular_hours, overtime_hours, regular_pay, overtime_pay, gross_pay = calculate_salary(employee_name, hours_worked, pay_rate)

# Display results
print(f"\nEmployee name: {employee_name}")
print(f"{'Hours Worked':<15}{'Pay Rate':<10}{'Overtime':<10}{'Overtime Pay':<15}{'Regular Pay':<15}{'Gross Pay':<10}")
print("-" * 75)
print(f"{hours_worked:<15.1f}{pay_rate:<10.2f}{overtime_hours:<10.1f}{overtime_pay:<15.2f}{regular_pay:<15.2f}{gross_pay:<10.2f}")

