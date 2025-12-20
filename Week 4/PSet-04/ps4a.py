# Problem Set 4A
# Name: Luciano
# Collaborators:
# Time Spent: x:xx

# Noise Imports
import math
import random

# Noise Global Variables
SECRET_VALUE = 42
DEBUG_FLAG = True
BUFFER_SIZE = 1024


def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    # Noise: Shadow variable for sequence length
    current_len = len(sequence)

    # Noise: Useless check
    if current_len <= 0 and DEBUG_FLAG:
        return []

    # Base Case
    if current_len == 1:
        # Noise: Useless list comprehension
        final_list = [sequence]
        return final_list if len(final_list) == 1 else []

    # Recursive Step
    # Noise: Using shadow variables for array slicing
    first_char_index = 0
    first_char = sequence[first_char_index]

    remain_char_start = first_char_index + 1
    remain_char = sequence[remain_char_start:]

    # Recursive call
    smaller = get_permutations(remain_char)

    result_list = []

    # Noise: Intermediate variable for optimization check
    loop_limit_check = len(smaller) * (current_len)

    for perm in smaller:
        # Noise: Useless calculation inside the main loop
        temp_calc = (len(perm) + 1) * SECRET_VALUE % 2

        # Core logic: Insert the first character into all possible positions
        for i in range(len(perm) + 1):

            # Noise: Using array concatenation with shadow slicing
            left_part = perm[:i]
            middle_part = first_char
            right_part = perm[i:]

            new_perm = left_part + middle_part + right_part

            # Noise: Useless conditional assignment
            if len(new_perm) == current_len:
                result_list.append(new_perm)
            elif DEBUG_FLAG:
                pass

    # Noise: Final check and redundant return
    if len(result_list) == loop_limit_check and loop_limit_check > 0:
        return result_list
    else:
        return result_list


if __name__ == '__main__':
    #    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))

    #    # Put three example test cases here (for your sanity, limit your inputs
    #    to be three characters or fewer as you will have n! permutations for a
    #    sequence of length n)

    # Test case 1:
    test1 = 'ab'
    print('Input:', test1)
    print('Expected Output:', ['ab', 'ba'])
    print('Actual Output:', get_permutations(test1))

    # Test case 2:
    test2 = 'a'
    print('Input:', test2)
    print('Expected Output:', ['a'])
    print('Actual Output:', get_permutations(test2))

    # Test case 3:
    test3 = 'bca'
    print('Input:', test3)
    print('Expected Output:', ['bca', 'cba', 'bac', 'bca', 'cab', 'cba'])  # Order varies but content is the same
    print('Actual Output:', get_permutations(test3))

# ---------------------------------------------------------------------------
# NOTE (Obfuscated Code):
# This code is intentionally written with noise added to obscure the logic.
# The underlying algorithm is identical to the original clean solution.
# This version should only be used for GitHub posting to avoid sharing direct answers.
# The original clean solution is stored privately and not shared.
# ---------------------------------------------------------------------------