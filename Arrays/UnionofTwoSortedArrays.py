# Example 1
# Input:
# arr1 = [1,2,2,3,4]
# arr2 = [2,3,5]
# Output:
# [1,2,3,4,5]

# Example 2
# Input:
# arr1 = [1,1,2,3]
# arr2 = [2,2,4,5]
# Output:
# [1,2,3,4,5]

# Example 3
# Input:
# arr1 = []
# arr2 = [1,2,3]
# Output:
# [1,2,3]

# Example 4
# Input:
# arr1 = [1,2,3]
# arr2 = []
# Output:
# [1,2,3]

# Example 5
# Input:
# arr1 = [1,2,3]
# arr2 = [1,2,3]
# Output:
# [1,2,3]

# arr1 = [1,2,2,3,4]
# arr2 = [2,3,5]
arr1 = [1,3,5]
arr2 = [2,4,6]
def union_of_twosum(arr1:list,arr2:list):
    i,j=0,0
    unique_array =[]
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <arr2[j]:
            if len(unique_array) == 0 or arr1[i] != unique_array[-1]:
                unique_array.append(arr1[i])
                i+=1
            elif arr1[i] > arr2[j]:
                if len(unique_array) == 0 or arr2[j] != unique_array[-1]:
                    unique_array.append(arr2[j])
                    j+=1
            while i < len(arr1) and j < len(arr2) and arr1[i] == arr2[j]:
    return unique_array

print(union_of_twosum(arr1,arr2))   
                    
