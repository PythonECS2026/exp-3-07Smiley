# AIM: Write a Python program to calculate the gross salary of an employee.
# Coder:
# Date:
print("Salary Calculator")

basic = float(input("Enter the basic salary: "))

da = basic * 0.70
ta = basic * 0.30
hra = basic * 0.10
gross = basic + da + ta + hra

print("\nSalary Details:")
print(f"Basic Salary:\t{basic:.1f}")
print(f"DA (70%):\t{da:.1f}")
print(f"TA (30%):\t{ta:.1f}")
print(f"HRA (10%):\t{hra:.1f}")
print(f"Gross Salary:\t{gross:.1f}")
# Write your code here
