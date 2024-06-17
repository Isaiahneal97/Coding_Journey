#************PROGRAM*****************


#print end and sep and newline and tab
print("one")       #OUTPUT: 'one'
print("two")       #OUTPUT: 'two'
print("one", "two")        #OUTPUT: 'one two'


print("one", "two", end = '*')  #OUTPUT: one two*
print("one", "two", sep = '*')  #OUTPUT: one*two


print("100\n200")  #OUTPUT: 100
                    #OUTPUT: 200

print("100\t200")  #OUTPUT: 100   200


#how to write fstrings-[alignment][width][,][.precision][type]
num = 123456.123456
num2 = 123456

print(f'{num:.2f}')  #OUTPUT: 123456.12
print(f'{num:,.2f}') #OUTPUT: 123,456.12
print(f'{num:.2%}')  #OUTPUT: 12345612.35%
print(f'{num2:,d}')  #OUTPUT: 123,456
print(f'The number is {num:12,.2f}')  #OUTPUT:  The number is   123,456.12


#ALIGNMENT
print(f'{num:<20.2f}')
print(f'{num:>20.2f}') 
print(f'{num:^20.2f}')

