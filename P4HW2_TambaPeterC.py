# Peter Tamba
# 7/21/2024
# P4HW2
# The program however will calculate gross pay for multiple employees, determined by user,
# and also calculates total amount paid for overtime, total amount paid for regular pay and total amount paid for all employees.

def calculate_pay(hours_worked, pay_rate):
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_pay = 40 * pay_rate
        overtime_pay = overtime_hours * pay_rate * 1.5
    else:
        overtime_hours = 0
        regular_pay = hours_worked * pay_rate
        overtime_pay = 0

    gross_pay = regular_pay + overtime_pay
    return regular_pay, overtime_pay, gross_pay, overtime_hours

def main():
    total_employees = 0
    total_overtime_pay = 0
    total_regular_pay = 0
    total_gross_pay = 0

    while True:
        employee_name = input('Enter employee\'s name or "Done" to terminate: ')
        if employee_name.lower() == 'done':
            break

        hours_worked = float(input(f'How many hours did {employee_name} work? '))
        pay_rate = float(input(f'What is {employee_name}\'s pay rate? '))

        regular_pay, overtime_pay, gross_pay, overtime_hours = calculate_pay(hours_worked, pay_rate)

        print(f"\nEmployee name: {employee_name}")
        print("---------------------------------------------------------")
        print(f"Hours Worked  Pay Rate  OverTime  OverTime Pay  RegHour Pay  Gross Pay")
        print(f"{hours_worked:<13} {pay_rate:<9} {overtime_hours:<8} ${overtime_pay:<12.2f} ${regular_pay:<11.2f} ${gross_pay:<9.2f}")
        print("---------------------------------------------------------\n")

        total_employees += 1
        total_overtime_pay += overtime_pay
        total_regular_pay += regular_pay
        total_gross_pay += gross_pay

    print(f"Total number of employees entered: {total_employees}")
    print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
    print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
    print(f"Total amount paid in gross: ${total_gross_pay:.2f}")

if __name__ == "__main__":
    main()
