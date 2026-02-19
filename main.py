# AIM: Write a Python program to calculate the gross salary of an employee.
# Coder:
# Date:
basic = float(input())

da = basic * 0.70
ta = basic * 0.30
hra = basic * 0.10
gross = basic + da + ta + hra

print("Salary Details:")
print(f"Basic Salary:    {basic}")
print(f"DA (70%):        {da}")
print(f"TA (30%):        {ta}")
print(f"HRA (10%):       {hra}")
print(f"Gross Salary:    {gross}"
# Write your code here
