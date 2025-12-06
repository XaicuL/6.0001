###################
## EXAMPLE: strings 
###################
# hi = "hello there"
# name = "ana"
# greet = hi + name  
# print(greet)
# greeting = hi + " " + name
# print(greeting)
# silly = hi + (" " + name)*3
# print(silly)

############
## testcode
# Luciano = "JeonHyunJun"
# L_age = input("age:")

# print("His real name is:",Luciano," ","&Luciano age is:",L_age)

############


####################
## EXAMPLE: output 
####################
# x = 1 #int
# print(x)
# x_str = str(x) #str
# print("my fav number is", x, ".", "x=", x)
# print("my fav number is", x_str + "." + "x=" + x_str)
# print("my fav number is" + x_str + "." + "x=" + x_str)


####################
## EXAMPLE: input
####################
# text = input("Type anything... ")
# print(5*text)
# num = int(input("Type a number... "))
# print(5*num)


####################
# # EXAMPLE: conditionals/branching 
# ###################
# x = float(input("Enter a number for x: "))
# y = float(input("Enter a number for y: "))
# if x == y:
#    print("x and y are equal")
#    if y != 0:
#        print("therefore, x / y is", x/y)
# elif x < y:
#    print("x is smaller")
# elif x > y:
#    print("y is smaller")
# print("thanks!")

    

############
# Data Type Strategy
# 1) Prefer int whenever the domain is mathematically integer.
#    -> int is exact, reliable, and avoids floating-point roundoff.
#
# 2) Use float only when the problem requires real numbers:
#       - division producing non-integers
#       - logarithms, roots, approximations
#       - continuous values
#
# 3) float is not exact (binary representation error),
#    so comparisons must be done with tolerance (epsilon), not ==.
#
# Summary:
# First try int. If the math fundamentally requires reals → use float.

# if-elif-else strategy

# 1) 'if' handles event A, 'elif' handles event B,
#    and 'else' represents the remaining complementary event.

# 2) You can think about it like the inclusion–exclusion mindset:
#    defining A and B clearly, then letting the rest fall  into the complement.


####################
## EXAMPLE: remainder 
####################
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#    print("number is even")
# else:
#    print("number is odd")


####################
## EXAMPLE: while loops 
## Try expanding this code to show a sad face if you go right
## twice and flip the table any more times than that. 
## Hint: use a counter
####################
# n = input("You are in the Lost Forest\n****************\n****************\n :)\n****************\n****************\nGo left or right? ")
# while n == "right" or n == "Right":
#    n = input("You are in the Lost Forest\n****************\n******       ***\n  (â•¯Â°â–¡Â°ï¼‰â•¯ï¸µ â”»â”â”»\n****************\n****************\nGo left or right? ")
# print("\nYou got out of the Lost Forest!\n\o/")



# n = 0
# while n < 5:
#    print(n)
#    n = n+1
        

####################
## EXAMPLE: for loops
####################
# for n in range(5):
#    print(n)
#
# mysum = 0
# for i in range(10):
#    mysum += i
# print(mysum)
#
# mysum = 0
# for i in range(7, 10):
#    mysum += i
# print(mysum)
# 
# mysum = 0
# for i in range(5, 11, 2):
#    mysum += i
#    if mysum == 5:
#        break
#        mysum += 1
# print(mysum)

# range(5, 11, 2) means:
#   5  → start value (inclusive)
#   11 → stop value (exclusive, so up to 10)
#   2  → step size (increment by 2 each loop)
#
# Therefore, this loop will generate:
#   i = 5, 7, 9
#
# It stops BEFORE reaching 11.
#
# So:
# for i in range(5, 11, 2):
#     ...
#
# is equivalent to iterating over these numbers:
#     5 → 7 → 9


####################
## EXAMPLE: perfect squares
####################
# ans = 0
# neg_flag = False
# x = int(input("Enter an integer: "))
# if x < 0:
#    neg_flag = True
# while ans**2 < x:
#    ans = ans + 1
# if ans**2 == x:
#    print("Square root of", x, "is", ans)
# else:
#    print(x, "is not a perfect square")
#    if neg_flag:
#        print("Just checking... did you mean", -x, "?")


####################
## TEST YOURSELF!
## Modify the perfect squares example to print 
## imaginary perfect sqrts if given a negative num.
####################