# # # # # # # # ####################
# # # # # # # # ## EXAMPLE: for loops over strings
# # # # # # # # ####################
# # # # # # # # # s = "demo loops"
# # # # # # # # # for index in range(len(s)):
# # # # # # # # #    if s[index] == 'i' or s[index] == 'u':
# # # # # # # # #        print("There is an i or u")
# # # # # # # # #
# # # # # # # # # for char in s:
# # # # # # # # #    if char == 'i' or char == 'u':
# # # # # # # # #        print("There is an i or u")
# # # # # # # #
# # # # # # # # # x = 0
# # # # # # # # # x = int(input())
# # # # # # # #
# # # # # # # # # Source - https://stackoverflow.com/q/71738854
# # # # # # # # # Posted by viveooo, modified by community. See post 'Timeline' for change history
# # # # # # # # # Retrieved 2025-12-02, License - CC BY-SA 4.0
# # # # # # # # #
# # # # # # # # # x=input("what is your real name?")
# # # # # # # # # print(type(x))
# # # # # # # # #
# # # # # # # # # x = len(input("what is your name?"))
# # # # # # # # # print(type(x))
# # # # # # # # #
# # # # # # # # # x = int(input("test:"))
# # # # # # # # #
# # # # # # # # # print(len(x))
# # # # # # # # # x = input()
# # # # # # # # # y = len(x)
# # # # # # # # #
# # # # # # # # # print(y)
# # # # # # # #
# # # # # # # # # x = 2
# # # # # # # # # y = 4
# # # # # # # # # z = x/y
# # # # # # # # # q = len(z)
# # # # # # # # #
# # # # # # # # # print(q)
# # # # # # # #
# # # # # # # # #error cuz float has no len()
# # # # # # # #
# # # # # # # # ####################
# # # # # # # # ## EXAMPLE: while loops and strings
# # # # # # # # ## CHALLENGE: rewrite while loop with a for loop
# # # # # # # # ####################
# # # # # # # # an_letters = "aefhilmnorsxAEFHILMNORSX"
# # # # # # # # word = input("I will cheer for you! Enter a word: ")
# # # # # # # # times = int(input("Enthusiasm level (1-10): "))
# # # # # # # #
# # # # # # # # # i = 0
# # # # # # # # # while i < len(word):
# # # # # # # # #    char = word[i]
# # # # # # # # #    if char in an_letters:
# # # # # # # # #        print("Give me an " + char + "! " + char)
# # # # # # # # #    else:
# # # # # # # # #        print("Give me a  " + char + "! " + char)
# # # # # # # # #    i += 1
# # # # # # # # # print("What does that spell?")
# # # # # # # # # for i in range(times):
# # # # # # # # #    print(word, "!!!")
# # # # # # # #
# # # # # # # #
# # # # # # # # ####################
# # # # # # # # ## EXAMPLE: perfect cube
# # # # # # # # ####################
# # # # # # # # cube = 27
# # # # # # # # #cube = 8120601
# # # # # # # # for guess in range(cube+1):
# # # # # # # #    if guess**3 == cube:
# # # # # # # #        print("Cube root of", cube, "is", guess)
# # # # # # # #        # loops keeps going even after found the cube root
# # # # # # #
# # # # # # #
# # # # # # # ####################
# # # # # # # ## EXAMPLE: guess and check cube root
# # # # # # # ####################
# # # # # # # # cube = 27
# # # # # # # ##cube = 8120601
# # # # # # # # for guess in range(abs(cube)+1):
# # # # # # # #    # passed all potential cube roots
# # # # # # # #    if guess**3 >= abs(cube):
# # # # # # # #        # no need to keep searching
# # # # # # # #        break
# # # # # # # # if guess**3 != abs(cube):
# # # # # # # #    print(cube, 'is not a perfect cube')
# # # # # # # # else:
# # # # # # # #    if cube < 0:
# # # # # # # #        guess = -guess
# # # # # # # #    print('Cube root of ' + str(cube) + ' is ' + str(guess))
# # # # # # #
# # # # # # # x = 3
# # # # # # # ans = 0 #variable initialization
# # # # # # # num_iterations = 0
# # # # # # #
# # # # # # # while (num_iterations < x):
# # # # # # #     ans = ans + x #changing binding of ans
# # # # # # #     num_iterations = num_iterations + 1 #changing binding of num_iterations
# # # # # # #
# # # # # # # print(f'{x}*{x} = {ans}') #f-string formatting
# # # # # # #
# # # # # # #
# # # # # # # ####################
# # # # # # # ## EXAMPLE: approximat                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          e cube root
# # # # # # # ####################
# # # # # # # # cube = 27
# # # # # # # ##cube = 8120601
# # # # # # # ##cube = 10000
# # # # # # # # epsilon = 0.1
# # # # # # # # guess = 0.0
# # # # # # # # increment = 0.01
# # # # # # # # num_guesses = 0
# # # # # # # ## look for close enough answer and make sure
# # # # # # # ## didn't accidentally skip the close enough bound
# # # # # # # # while abs(guess**3 - cube) >= epsilon and guess <= cube:
# # # # # # # #    guess += increment
# # # # # # # #    num_guesses += 1
# # # # # # # # print('num_guesses =', num_guesses)
# # # # # # # # if abs(guess**3 - cube) >= epsilon:
# # # # # # # #    print('Failed on cube root of', cube, "with these parameters.")
# # # # # # # # else:
# # # # # # # #    print(guess, 'is close to the cube root of', cube)
# # # # # # #
# # # # # # #
# # # # # # # ####################
# # # # # # # ## EXAMPLE: bisection cube root (only positive cubes!)
# # # # # # # ####################
# # # # # # # # cube = 27
# # # # # # # ##cube = 8120601
# # # # # # # ## won't work with x < 1 because initial upper bound is less than ans
# # # # # # # ##cube = 0.25
# # # # # # # # epsilon = 0.01
# # # # # # # # num_guesses = 0
# # # # # # # # low = 0
# # # # # # # # high = cube
# # # # # # # # guess = (high + low)/2.0
# # # # # # # # while abs(guess**3 - cube) >= epsilon:
# # # # # # # #    if guess**3 < cube:
# # # # # # # #        # look only in upper half search space
# # # # # # # #        low = guess
# # # # # # # #    else:
# # # # # # # #        # look only in lower half search space
# # # # # # # #        high = guess
# # # # # # # #    # next guess is halfway in search space
# # # # # # # #    guess = (high + low)/2.0
# # # # # # # #    num_guesses += 1
# # # # # # # # print('num_guesses =', num_guesses)
# # # # # # # # print(guess, 'is close to the cube root of', cube)
# # # # # #
# # # # # # x = int(input('enter an int:'))
# # # # # # ans = 0 # variable initialization
# # # # # #
# # # # # # while ans**3 < abs(x): #abs is used to handle negative input , kor : 절댓값
# # # # # #     ans = ans + 1
# # # # # #
# # # # # # if ans ** 3 != abs(x):
# # # # # #     print(x, 'is not a perfect cube')
# # # # # # else:
# # # # # #     if x < 0:
# # # # # #         ans = -ans
# # # # # #     print('cube root of', x, 'is',ans)
# # # # #
# # # # # max_val = abs(int(input('enter your positive int:')))
# # # # # i = 0
# # # # #
# # # # # while i < max_val:
# # # # #     i = i + 1
# # # # # print(i)
# # # # #
# # # #
# # # #
# # # # x = int(input('enter an int greater than 2: '))
# # # # smallest_divisor = None
# # # #
# # # # for guess in range(2, x):
# # # #     if x % guess == 0:
# # # #         smallest_divisor = guess
# # # #         break
# # # #
# # # # if smallest_divisor != None:
# # # #     print('Smallest divisor of', x, 'is', smallest_divisor)
# # # # else:
# # # #     print(x, 'is prime')
# # # #
# # #
# # # # x = 1
# # # #
# # # # epsilon = 0.01
# # # # step = epsilon**2
# # # # num_guesses = 0
# # # # ans = 0.0
# # # #
# # # # while abs(ans**2 - x) >= epsilon and ans <= x:
# # # #     ans += step
# # # #     num_guesses += 1
# # # # print('nuber of guesses = ', num_guesses)
# # # #
# # # # if abs(ans**2 - x) >= epsilon:
# # # #     print('failed to find the square root of ', x)
# # # # else:
# # # #     print(ans, 'is close to the square root of ', x)
# # #
# # # epsilon = 0.01
# # # num_guesses, low = 0,0
# # # high = max(1,x)
# # #
# # # ans = (high + low) / 2.0
# # #
# # # while abs(ans**2 - x \>= epsilon):
# # #     if ans**2 < x:
# # #         low = ans
# # #     else:
# # #         high = ans
# #
# # x = float(input("Enter a number: "))
# #
# # epsilon = 0.01
# # num_guesses, low = 0, 0
# # high = max(1, x)
# # mid = (high + low) / 2
# #
# # while abs(mid ** 2 - x) >= epsilon:
# #     print("low =", low, "high =", high, "mid =", mid)
# #     num_guesses += 1
# #
# #     if mid ** 2 < x:
# #         low = mid
# #     else:
# #         high = mid
# #
# #     mid = (high + low) / 2
# #
# # print("number of guesses =", num_guesses)
# # print(mid, "is close to square root of", x)
#
# x = float(input("Enter a number: "))
# epsilon = 0.01
#
# lower_bound = 0
#
# while 2**lower_bound < x:
#     lower_bound += 1
#
# low = lower_bound - 1
# high = lower_bound + 1
# mid = (high + low) / 2
#
# while abs(mid ** 2 - x) >= epsilon:
#     if 2**mid < x:
#         low = mid
#     else:
#         high = mid
#     mid = (high + low) / 2
#
# print(mid, 'is close to the log base 2 of', x)

x = 0.0

for i in  range(10):
    x = x + 0.1

if x == 1.0:
    print("x is exactly 1.0")
else:
    print(x, 'is not 1.0')

