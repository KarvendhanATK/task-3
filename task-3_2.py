#Task-3.2
# Given a Python List [10, 501, 22, 37, 100, 999, 87, 351] your task is to Count 
# all the Prime Numbers and create a new Python List which will
# contain all the Prime Numbers in it?

mylist = [10, 501, 22, 37, 100, 999, 87, 351]

prime = []

for i in mylist:
    c = 0
    if i > 1:
        for j in range(1, i + 1):
            if i % j == 0:
                c += 1
        if c == 2: 
            prime.append(i)

print(prime)
