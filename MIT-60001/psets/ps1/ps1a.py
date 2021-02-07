#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 11:13:53 2020

@author: paulgrote
"""

# salary variables
annual_salary = float(input("Enter your annual salary: "))
monthly_salary = annual_salary/12
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))

# house variables
total_cost = float(input("Enter the cost of your dream home: "))
portion_down_payment = 0.25
down_payment = portion_down_payment * total_cost

# savings variables
current_savings = 0
annual_return = 0.04


month = 0
print("Down payment is: ", down_payment)
while current_savings < down_payment:
    month += 1
    
    monthly_return = current_savings*(annual_return/12)
    current_savings = current_savings + (monthly_salary * portion_saved) + monthly_return
    
    print("Month", month, ":", current_savings)

print("Number of months: ", month)