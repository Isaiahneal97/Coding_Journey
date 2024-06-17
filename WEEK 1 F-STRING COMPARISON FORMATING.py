#PROGRAM 1
# This program demonstrates:
# how a floating-point
# number is displayed with no formatting.

amount_due = 5000.0
monthly_payment = amount_due / 12.0
print(f'The monthly payment is {monthly_payment}.')

#OUTPUT (1)
# The monthly payment is 416.6666666666667.


# PROGRAM 2
# This program demonstrates:
# how a floating-point
# number can be rounded.
amount_due = 5000.0
monthly_payment = amount_due / 12.0
print(f'The monthly payment is {monthly_payment:.2f}.')

#OUTPUT (2)
# The monthly payment is 416.67.

