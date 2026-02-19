# AIM: Write a Python program to calculate the gross salary of an employee.
# Coder:
# Date:
basic = float(input())

da = basic * 0.70
ta = basic * 0.30
hra = basic * 0.10
gross = basic + da + ta + hra

print("Salary Details:")
print(f"Basic Salary:    {basic:g}")
print(f"DA (70%):        {da:g}")
print(f"TA (30%):        {ta:g}")
print(f"HRA (10%):       {hra:g}")
print(f"Gross Salary:    {gross:g}")
# Write your code here
