# Remove Duplicates from Sorted Array (LeetCode 26)

# Input:

# [1,1,2,2,3,3,4,5,5]

# Expected:

# [1,2,3,4,5,_,_,_,_]

# Return:

# 5
# Rules
# ❌ Extra array nahi use karni.
# ✅ In-place modify karna hai.
# ✅ Two Pointers use karne ki koshish kar.
# bruteforce

# arr = [1,1,2,2,3,3,4,5,5]
# def remove_duplicates(arr):
#     i,j=0,1
#     if not arr:
#         return
#     elif len(arr)<=j:
#         return
#     while j<len(arr):
#         if arr[i] == arr[j]:
#             arr.remove(arr[j])
#         else:
#             i+=1
#             j+=1
#     return arr
# print(remove_duplicates(arr))

arr = [1,1,2,2,3,3,4,5,5]

def return_unique_element(arr):
    i,j =0,0
    if not arr:
        return
    elif len(arr)<=1:
        return
    while j <= len(arr)-1:
        if arr[i] == arr[j]:
            j+=1
        else:
            i+=1
            arr[i] = arr[j]
            j+=1
    return arr[:i+1]

print(return_unique_element(arr))
print(arr)

