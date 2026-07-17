# Problem Statement
# Write a function that returns:
# True
# if the array is sorted in ascending order, otherwise
# False
# Example 1
# arr = [1, 2, 3, 4, 5]
# Output
# True
# Example 2
# arr = [1, 5, 3, 4]
# Output
# False
# Example 3
# arr = [5]
# Output
# True
# (A single element array is always sorted.)
# Example 4
# arr = [2, 2, 2, 2]
# Output
# True
# Equal consecutive elements are still considered sorted in ascending order.
# 🎯 Challenge
# Try to solve it in one traversal.


arr= [1, 2, 3, 4,1]
arr=[5]
def sorted_check(arr:list):
    for i in range(len(arr)-1):
        if i+1 <= len(arr)-1:
            if arr[i] <= arr[i+1]:
                pass
            else:
                return False
        else:
            arr[i] < arr[i-1]
    return True

print(sorted_check(arr))




# optimal 
def sorted_check(arr:list):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True
        