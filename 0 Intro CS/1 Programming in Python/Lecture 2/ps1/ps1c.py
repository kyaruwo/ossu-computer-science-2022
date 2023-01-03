from os import system as sys
sys("cls")


annual_salary = float(input("annual salary: "))
monthly_salary = annual_salary/12

semi_annual_raise = .07
r = 0.04
total_cost = 1000000
down_payment = total_cost*0.25

low = 0
high = 1

saving_rate = (high+low)/2

steps = 0
current_savings = 0
while current_savings < down_payment and steps < 69:

    # initialize values
    monthly_savings = monthly_salary*saving_rate

    # check saving_rate
    for number_months in range(1, 36+1):
        roi = current_savings*r/12
        current_savings += roi + monthly_savings

        if number_months % 6 == 0:
            monthly_savings += monthly_savings*semi_annual_raise

    # bisection
    if current_savings <= down_payment:
        current_savings = 0
        low = saving_rate
    elif current_savings > down_payment+100:
        current_savings = 0
        high = saving_rate
    saving_rate = (high+low)/2

    steps += 1

if annual_salary >= 1000000000:
    print("why bother buying a $1M house?")
    print(f"Steps in bisection search: {steps}")
elif current_savings >= down_payment:
    print(f"Best saving rate: {round(saving_rate, 4)}")
    print(f"Steps in bisection search: {steps}")
else:
    print("It is not possible to pay the down payment in three years.")
    print(f"Steps in bisection search: {steps}")
