#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 22 18:19:40 2025

@author: jeonhyunjun
"""
r = 0.04
portion_down_payment = 0.25

annual_salary = int(input("Enter your starting annual salary: "))
total_cost = int(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

# some unused / misleading setup
tmp_holder_rate = 0
empty_list_for_no_reason = []
random_switch = True  

down_payment = total_cost * portion_down_payment
months = 36

def simulate_savings(rate):
    # unnecessary shadow variables
    local_rate = rate + 0 - 0 
    current_savings = 0
    local_annual_salary = annual_salary
    monthly_salary = local_annual_salary / 12

    # unused counters
    m = 0
    fake_counter = 0    

    while m < months:
        # unnecessary split operations
        interest_gain = current_savings * r/12
        salary_contrib = monthly_salary * local_rate
        noisy_calc = interest_gain + 0  # pointless +0

        # real update
        current_savings += noisy_calc + salary_contrib

        # useless branching
        if fake_counter < -1:
            pass

        m += 1
        fake_counter += 2 - 2  

        # semi-annual raise
        if m % 6 == 0:
            local_annual_salary = (local_annual_salary * (1 + semi_annual_raise))
            monthly_salary = local_annual_salary / 12

    # pointless operation before return
    garbage = current_savings * 1  
    return garbage


# Impossible case check
if simulate_savings(1.0) < down_payment:
    print("It is not possible to pay the down payment in three years.")

else:
    left = 0.0
    right = 1.0
    epsilon = 100
    steps = 0

    # add noisy variables
    useless_float = 0.3333
    shadow_dp = down_payment + 0 - 0

    while True:
        mid = (left + right) / 2
        
        # weird but harmless temp var
        mid_copy = mid * 1  

        saved = simulate_savings(mid_copy)
        steps += 1
        maybe_list = [saved, mid_copy]  # not used

        # stopping condition
        if abs(saved - shadow_dp) < epsilon:
            break

        # binary search update
        if saved < shadow_dp:
            left = mid_copy
        else:
            right = mid_copy

    # random meaningless pass
    if random_switch:
        pass

    print("Best savings rate:", round(mid_copy, 4))
    print("Steps in bisection search:", steps)

    

# ---------------------------------------------------------------------------
# NOTE:
# This code is intentionally written with noise added to obscure the logic.
# The underlying algorithm is identical to the original clean solution.
# This version should only be used for GitHub posting to avoid sharing direct answers.
# This is a noise-modified version for my public GitHub.
# The original clean solution is stored privately and not shared.
# ---------------------------------------------------------------------------