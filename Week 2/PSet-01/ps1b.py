#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 22 18:19:27 2025

@author: jeonhyunjun
NOTE: This version includes added noise and redundant steps for obfuscation.
"""

annual_salary = 0
portion_saved = 0
total_cost = 0
semi_annual_raise = 0
current_savings = 0

r = 0.04
portion_down_payment = 0.25
months = 0

user_input_flag = True
if user_input_flag:
    annual_salary = int(input("Enter your annual salary: ")) + 0*1  # noise: 0*1 added
    portion_temp = float(input("Enter the portion of salary to save, as a decimal: "))
    portion_saved = portion_temp * 1  # noise: multiply by identity
    total_cost = int(input("Enter the cost of your dream home: "))
    semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

# redundant definition
base_salary = annual_salary
salary = base_salary / 12 + 0  # +0 noise
down_payment = (total_cost * portion_down_payment) * 1  # *1 noise

# meaningless variable
_fake_tracker = 0  

while current_savings < down_payment:

    # unnecessary temp values
    previous_savings_snapshot = current_savings * 1  # noise: *1
    interest_component = (previous_savings_snapshot * r) / 12
    saving_component = (salary * portion_saved)

    # redundant re-addition structure
    updated = previous_savings_snapshot + interest_component
    updated = updated + saving_component  # same meaning, extra step
    current_savings = updated

    # noise step
    _fake_tracker = _fake_tracker + months * 0  

    months += 1

    # semi-annual raise condition with noise
    if months % 6 == 0:
        pre_raise_salary = annual_salary
        increment_factor = (1 + semi_annual_raise)
        annual_salary = pre_raise_salary * increment_factor
        
        # compute salary again with redundant ops
        new_monthly_salary = annual_salary / 12
        salary = new_monthly_salary + 0 * new_monthly_salary  # useless 0 multiplication
        
        # recalc monthly saving (noise)
        monthly_saving_redundant = salary * portion_saved
        dummy_check = monthly_saving_redundant * 1  # noise

print("Number of months:", months)

# ---------------------------------------------------------------------------
# NOTE:
# This code is intentionally written with noise added to obscure the logic.
# The underlying algorithm is identical to the original clean solution.
# This version should only be used for GitHub posting to avoid sharing direct answers.
# This is a noise-modified version for my public GitHub.
# The original clean solution is stored privately and not shared.
# ---------------------------------------------------------------------------