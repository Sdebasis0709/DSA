# Problem

# Write a function that returns the index of the target if found, otherwise returns -1.

# arr = [5, 10, 15, 20, 25, 30, 35]
# target = 25

# # Output:
# 4

def index_value(arr:list,num:int):
    low , high = 0, len(arr) - 1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            low = mid + 1
        else :
            high = mid - 1
    return -1


print(index_value([5, 10, 15, 20, 25, 30, 35],25))