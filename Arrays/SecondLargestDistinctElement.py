# Problem

# Find the second largest distinct element.

# Example:

# arr = [12, 35, 1, 10, 34, 1]

# Output:

# 34
# Edge Cases

# Think about these while writing your solution:

# [5, 5, 5, 5]

# Should it return 5 or indicate that there is no second largest distinct element?

# [-10, -5, -20]

# Should still work.


arr = [12, 35, 1, 10, 34, 1]
count = 0
max_ele = arr[0]

# for ele in arr:
#     if ele > max_ele:
#         max_ele = ele
# arr.remove(max_ele)
# second_max = arr[0]
# for ele in arr:
#     if ele > second_max:
#         second_max = ele

# print(second_max)


largets =  float("-inf")
second_larg = float("-inf")
for ele in arr:
    if  ele > largets :
        second_larg = largets
        largets = ele
    elif  ele > second_larg and ele != largets:
         second_larg = ele
          
         
print(second_larg)


