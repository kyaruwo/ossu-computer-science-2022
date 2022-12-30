from os import system as sys
sys("cls")

annual_salary = float(input("annual salary: "))
portion_saved = float(input("percent of salary to save in decimal: "))
total_cost = float(input("cost of dream home: "))
semi_annual_raise = float(input("semi-annual raise in decimal: "))

monthly_salary = annual_salary/12
monthly_savings = monthly_salary*portion_saved
current_savings = 0

r = 0.04

portion_down_payment = total_cost*0.25

number_months = 0
while current_savings < portion_down_payment:
    number_months += 1

    roi = current_savings*r/12
    current_savings += roi + monthly_savings

    if number_months % 6 == 0:
        monthly_savings += monthly_savings*semi_annual_raise

print(f"Number of Months: {number_months}")
