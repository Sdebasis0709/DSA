# Reverse an Array (In-place)
# Rules

# Allowed:

# ✅ Loops
# ✅ Variables
# ✅ Swapping

# Not Allowed:

# ❌ reverse()
# ❌ [::-1]
# ❌ Creating another array
# Input
# arr = [1, 2, 3, 4, 5]
# Expected Output
# [5, 4, 3, 2, 1]
# Challenge

# Do it in O(n) time and O(1) extra space.

# 💡 Hint: You don't need to traverse the entire array. Think about what happens if you use two pointers—one at the beginning and one at the end.

arr= [1,2,3,4,5]
l,r = 0 , len(arr)-1
while l<r:
    arr[l],arr[r] = arr[r],arr[l]
    l+=1
    r-=1
print(arr)