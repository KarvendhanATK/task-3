#Task-3.9
#You have been given a Python list [10,20,30,9] and a value of 59. 
# Write a python program to find the triplet in the list whose sum is equal to the given value ?

from itertools import combinations

def findTriplets(lst, key):
    def valid(val):
        return sum(val) == key

    return list(filter(valid, combinations(lst, 3)))

lst = [10, 20, 30, 9]
result = findTriplets(lst, 59)
print(result)
