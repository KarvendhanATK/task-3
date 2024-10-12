#Task-3.4
#Write a python program to find the sum of the first and last digit of an integer?
#Ex:12345
number = 12345

number= str(number)

first_digit=int(number[0])
last_digit=int(number[-1])

addition=first_digit+last_digit

print('Addition of first and last digit number is', addition)
