#task-3.1
#You have been given Python List[10,501,22,37,100,999,87,351] your task is to 
# create two List one which have all the Even Numbers and another 
# List which will have all the ODD numbers in it?


# Given list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

#lists for even and odd numbers
even_numbers = []
odd_numbers = []


for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)  
    else:
        odd_numbers.append(num)    

# Results
print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)
