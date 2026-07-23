# Example 1
# nums = [1,1,0,1,1,1]

# Output

# 3
# Explanation
# [1,1]      -> 2 ones
# [1,1,1]    -> 3 ones ✅

# Maximum = 3

# Example 2
# nums = [1,0,1,1,0,1]

# Output

# 2
# Example 3
# nums = [0,0,0,0]

# Output

# 0
# Example 4
# nums = [1,1,1,1]

# Output

# 4
# Constraints
# 1 <= len(nums) <= 10^5

# nums[i] is either 0 or 1
arr =  [1, 1, 0, 1, 0, 0, 1, 1]

# def maximum_count(arr):
#     curr_count =0
#     max_count =0
#     for i in arr:
#         if i == 1:
#             curr_count += 1
#         elif i ==0 :
#             if max_count  < curr_count :
#                 max_count = curr_count
#                 curr_count = 0
#     return max_count if max_count >= curr_count else curr_count

arr =  [1, 1, 0, 1, 0, 1, 1, 1 ,0, 1, 1]
arr = [1, 1, 1, 0]
def maximum_count(arr):
    left,right =0,0
    zeros = 0
    max_length = 0
    while left <= right and right < len(arr):
        if zeros <= 1:
            if arr[right] == 1:
                max_length = max(max_length,right-left+1)
                right+=1
            elif arr[right] == 0:
                zeros +=1
                max_length = max(max_length,right-left+1)
                right +=1
        else:
            while zeros > 1:
                if arr[left] == 0:
                    zeros -= 1
                    left +=1
                else:
                    left +=1
    return max_length
        


print(maximum_count((arr)))