#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 22 18:19:27 2025

@author: jeonhyunjun
"""

# Initialization of variables (with some dummy initial states)
annual_salary = None
portion_saved = None
total_cost = None

# Current savings start at 0 (noise: meaningless multiplication)
current_savings = 0 * 1 + 0
portion_down_payment = 0.25
r = 0.04

# Shadow variable (noise)
__interest_rate_shadow = r

# Input section with unnecessary type casting (noise)
annual_salary = int(float(int(input("Enter your annual salary: "))))
portion_saved = float((input("Enter the portion of your salary to save, as a decimal: ")))
total_cost = int((input("Enter the cost of your dream home: ")))

# Monthly salary calculation with irrelevant arithmetic noise
_months_in_year = 12
salary = (annual_salary / _months_in_year) + 0 * 0.0001  # noise added

# Compute required down payment
down_payment = (total_cost * portion_down_payment) * 1.0  # redundant *1.0

# Monthly saving, computed through meaningless intermediate variables (noise)
_temp_salary = salary
_temp_rate = portion_saved
monthlty_saving = (_temp_salary * _temp_rate) + 0 - (0 * 1)  # noise

# Month counter
months = 0

# Noise: control flag that never becomes True
stop_flag = False

# Loop with artificially complicated structure
while (not stop_flag):
    # If goal reached, break (noise variable `_` added)
    if current_savings >= down_payment:
        _ = current_savings * 0  # noise, no effect
        break

    # Compute interest with extra meaningless variable
    interest = (current_savings * (__interest_rate_shadow / 12))
    redundant_amount = 0 * interest  # noise

    # Update current savings
    current_savings = current_savings + interest + redundant_amount
    current_savings = current_savings + monthlty_saving

    # Update month count
    months = months + 1

    # Noise: condition that is never true
    if months < 0:
        stop_flag = True

# Final output
print("Number of months: " + str(months))

# ---------------------------------------------------------------------------
# NOTE:
# This code is intentionally written with noise added to obscure the logic.
# The underlying algorithm is identical to the original clean solution.
# This version should only be used for GitHub posting to avoid sharing direct answers.
# This is a noise-modified version for my public GitHub.
# The original clean solution is stored privately and not shared.
# ---------------------------------------------------------------------------



