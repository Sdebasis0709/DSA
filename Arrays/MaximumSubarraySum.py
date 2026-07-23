# Subarray:
# [4, -1, 2, 1]
# Sum:
# 4 + (-1) + 2 + 1 = 6

# arr = [-2, -3, 4, -1, -2, 1, 5, -3]
# sum = 7


arr = [-2, -3, 4, -1, -2, 1, 5, -3]
arr = [-3, -7, -1, -2, -5]
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum = arr[0]
arr_left , array_right = 0,0
l,r =0,0
current_sum = 0
for i in range(len(arr)):
    current_sum += arr[i]
    r+=1
    if max_sum < current_sum:
        max_sum = current_sum
        arr_left = l
        array_right = r
    if current_sum < 0:
        current_sum = 0
        l=r
print(max_sum)
print(arr[arr_left:array_right])






# max_sum = arr[0]
# current_sum = 0
# for i in arr:
#     current_sum += i
#     max_sum = max(current_sum,max_sum)
#     if current_sum < 0:
#         current_sum = 0
# print(max_sum)