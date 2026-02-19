# AIM: Write a Python program to calculate the gross salary of an employee.
# Coder:
# Date:print("Salary Calculator")

basic = float(input("Enter the basic salary: "))

da = basic * 0.70
ta = basic * 0.30
hra = basic * 0.10
gross = basic + da + ta + hra

print("\nSalary Details:")
print(f"Basic Salary:\t{basic:.2f}")
print(f"DA (70%):\t{da:.2f}")
print(f"TA (30%):\t{ta:.2f}")
print(f"HRA (10%):\t{hra:.2f}")
print(f"Gross Salary:\t{gross:.2f}")
# Write your code here
