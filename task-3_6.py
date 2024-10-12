#Task-3.6
# You have been three lists. Your task is to find the duplicates in the three lists.
# Write a python program for the same.You can use your own python lists?

def Intersets(arr1, arr2, arr3):
    common = list(filter(lambda x: x in arr2 and x in arr3, arr1))
    print(common)

arr1 = [1,10,15,20,25,30,35]
arr2 = [5,10,25,40,50]
arr3 = [10,12,14,24,25,40]

Intersets(arr1, arr2, arr3)
