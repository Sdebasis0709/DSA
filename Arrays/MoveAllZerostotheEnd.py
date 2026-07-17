# Problem Statement

# Move all 0s to the end of the array while maintaining the order of the non-zero elements.

# Input
# arr = [0, 1, 0, 3, 12]
# Output
# [1, 3, 12, 0, 0]
# Example 2
# arr = [1, 2, 3]

# Output

# [1, 2, 3]
# Example 3
# arr = [0, 0, 0]

# Output

# [0, 0, 0]
arr = [0, 1, 0, 3, 12]
l,r=0,len(arr)-1 
while l<r:
    if arr[r] == 0:
        r-=1
    elif arr[l] == 0:
        arr[l] ,arr[r]=arr[r],arr[l]
        l+=1
        r-=1
    else:
        l+=1

print(arr)