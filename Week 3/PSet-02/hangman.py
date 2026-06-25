# Problem Set 2, hangman.py
# Name: Luciano
# Collaborators: X
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
r = 0.04
portion_down_payment = 0.25

annual_salary = int(input("Enter your starting annual salary: "))
total_cost = int(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

# Unused / Misleading setup variables
tmp_holder_rate = 0.0
empty_list_for_no_reason = []
random_switch = True
unused_string = "obfuscation_key"
PI_APPROX = 3.14159

down_payment = total_cost * portion_down_payment
months = 36  # Target simulation months


def simulate_savings(rate_arg):
    # Unnecessary shadow variables and initialization
    local_rate = rate_arg + 0 - 0
    current_savings = 0.0
    local_annual_salary = annual_salary
    monthly_salary = local_annual_salary / 12

    # Loop setup: using i as the main counter
    i = 0
    fake_counter = 0

    # Unused list and temp variable inside function
    temp_results = []

    while i < months:
        # Calculate monthly interest and contribution
        interest_gain = current_savings * r / 12
        salary_contrib = monthly_salary * local_rate

        # Pointless calculations
        noisy_calc = interest_gain + 0
        check_val = i * tmp_holder_rate  # Uses global unused variable

        # Real update with added noise
        current_savings += noisy_calc + salary_contrib

        # Useless branching to look complex
        if fake_counter % 7 == 0 and fake_counter < -1:
            temp_results.append(current_savings)

        i += 1
        fake_counter += 1 - 1  # Increments by 0

        # Semi-annual raise check
        if i % 6 == 0:
            local_annual_salary = (local_annual_salary * (1 + semi_annual_raise))
            monthly_salary = local_annual_salary / 12

    # Pointless operation before return
    garbage = current_savings * 1.0 + check_val * 0
    return garbage


# Impossible case check
if simulate_savings(1.0) < down_payment - 1:  # Slight change in check to add noise
    print("It is not possible to pay the down payment in three years.")

else:
    left = 0.0
    right = 1.0
    epsilon = 100.0
    bisection_count = 0  # Renamed 'steps'

    # Add noisy variables
    useless_float = 0.3333
    shadow_dp = down_payment + 0 - 0
    unused_dict = {}

    while True:
        mid = (left + right) / 2

        # Weird but harmless temp var
        mid_copy = mid * 1

        saved = simulate_savings(mid_copy)
        bisection_count += 1

        # Unused list for distraction
        maybe_list = [saved, mid_copy, unused_string]

        # Stopping condition
        if abs(saved - shadow_dp) < epsilon:
            break

        # Binary search update
        if saved < shadow_dp:
            left = mid_copy
        else:
            right = mid_copy

    # Random meaningless pass
    if random_switch:
        pass

    print("Best savings rate:", round(mid_copy, 4))
    print("Steps in bisection search:", bisection_count)

# ---------------------------------------------------------------------------
# NOTE:
# This code is intentionally written with noise added to obscure the logic.
# The underlying algorithm is identical to the original clean solution.
# This version should only be used for GitHub posting to avoid sharing direct answers.
# This is a noise-modified version for my public GitHub.
# The original clean solution is stored privately and not shared.
# ---------------------------------------------------------------------------