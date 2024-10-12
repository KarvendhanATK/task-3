#Task-3.10
#Given a list [4,2,-3,1,6] Write a python program to find if there is a sub-list with sum equal to Zero ?

def subArray(arr, l):
    for i in range(l):
        a = 0  
        for j in range(i, l):
            a += arr[j]
            if a == 0:
                return True
    return False

array = [4, 2, -3, 1, 6]
print(subArray(array, len(array)))
