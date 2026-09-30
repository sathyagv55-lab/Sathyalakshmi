#Function 2: Calculate total deductions
def deduction(*deductions):
    """ Accept any number of deductions using *args. """
    total_deduction = sum(deductions)
    return total_deduction
# Function 3: Tax Calculate
def calculate_tax(gross_salary):
    """ Calculate tax based on gross salary. Tax slabs: Up to 30,000 -> 0% 30,001 - 50,000 -> 5% 50,001 - 1,00,000 -> 10% Above 1,00,000 -> 15% """
    if gross_salary <= 30000:
        tax = 0
    elif gross_salary <= 50000:
        tax = gross_salary * 0.05
    elif gross_salary <= 100000:
        tax = gross_salary * 0.10
    else: tax = gross_salary * 0.15
    return tax
# Function 4: Calculate net salary
def calculate_net_salary(gross_salary, total_deduction):
    """ Calculate the final salary after deductions. """
    net_salary = gross_salary - total_deduction
    return net_salary

def incentives_bonus(emp_salary, bonus_rate=10,incentive=2000):
    """ Calculate bonus based on basic salary. Default bonus rate is 10% """
    bonus = emp_salary * (bonus_rate / 100)
    total_bonus = emp_salary + bonus + incentive
    return total_bonus