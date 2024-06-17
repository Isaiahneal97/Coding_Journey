#PROGRAM

# run a few of these examples
# in the interactive shell the one with the arrows so you can understand

#INPUT
# x and y are integers
# z and t are strings

x=5
y=6
t="4"
z="name"

# (1) when you use the + sign to combine (concatenate) it
#both are numbers it will add them up so answer will be 11

print (x+y)
print ("---------------")
#OUTPUT   11


# (2) when you use + to concantenate if one is a string
# and the other a number it will not print and you have to have both
# as same data type, in this case
# we change the type of x to string since we cannot chane z to a number
# notice + concatenation has no spaces

print (str(x)+z)
print ("---------------")
#OUTPUT     5name


# (3) since t is an integer masquerading as a string
# we can use + to convert t to an int and combine that with x
# because now they are same data type. This adds to 9 

print(x+int(t))
print ("---------------")
# OUTPUT     9


# (4) when we use comma to combibe they do not have to be same data
# type, notice the automatic addition of spaces between

print(x, y, z)
print ("---------------")
#OUTPUT     5 6 name


# (5) we can use , to combine multiple variables and strings and
# numbers of differeent types

print('this is z =', z, x, 8)
print ("---------------")
#OUTPUT     this is z = name 5 8
