#Task-3.7
# Write a python program to find the first non - repeating elements in a given list of integers?

def count(arr, n):
    a = [False for i in range(n)]

    for i in range(n):
        if a[i]:
            continue

        count = 1
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                a[j] = True
                count += 1
        
        if count == 1:
            print(arr[i])

arr = [5, 10, 15, 20, 10, 20, 5,12, 10]
n = len(arr)
count(arr, n)
