#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 11:13:53 2020

@author: paulgrote
"""

# salary variables
salary_input = float(input("Enter the starting salary: "))
semi_annual_raise = .07

# house variables
total_cost = 1000000
portion_down_payment = 0.25
down_payment = portion_down_payment * total_cost

# savings variables
current_savings = 0
annual_return = 0.04

# bisection search variables
numGuesses = 0
low = 0
high = 10000
guess = (high + low)//2

if (salary_input*3) < down_payment:
   print("It is not possible to save for the down payment.")
else:

# bisection loop
    while abs(down_payment-current_savings) >= 100:
        numGuesses += 1
        month = 0
        annual_salary = salary_input
        current_savings = 0
        print("#",numGuesses)
        print("Guess:", guess, "Savings:", current_savings)
    
    # calculate savings using current guess    
        for i in range(36):
            month += 1
            monthly_salary = annual_salary/12
            monthly_return = current_savings*(annual_return/12)
            current_savings = current_savings + (monthly_salary * (guess*.0001)) + monthly_return
            
            if month%6 == 0:
                annual_salary = annual_salary + (annual_salary * semi_annual_raise)
            
            print("Month", month, ":", current_savings)
            
        if current_savings > (down_payment + 100):
            high = guess
        elif current_savings < (down_payment - 100):
            low = guess
        guess = (high+low)//2
        
        if numGuesses >=15:
            break
        
    print("Best savings rate: ", guess*.0001)
    print("Steps in bisection search: ", numGuesses)

