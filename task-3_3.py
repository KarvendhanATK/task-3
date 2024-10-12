#Task-3.3
# Given a Python List [10, 501, 22, 37, 100, 999, 87, 351] 
# Find out how many numbers are there in the given Python List which are Happy Numbers?
a = [10, 501, 22, 37, 100, 999, 87, 351]
b = []

def happy(a):
    for i in range(len(a)):
        sum_value = a[i]
        while sum_value != 1 and sum_value != 4:
            tempsum = 0
            for digit in str(sum_value):
                tempsum += int(digit)**2
            sum_value = tempsum
        if sum_value == 1:
            b.append(a[i])
    return b

print(happy(a))
