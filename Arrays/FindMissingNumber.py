
nums = [9,6,4,2,3,5,7,0,1]
# nums = [3, 0, 1]
# def missingNumber(nums):
#     array_sum =0
#     n = len(nums)
#     for i in range(len(nums)):
#         array_sum += nums[i]
#     total_sum = (n*(n +1))// 2
#     missing_number = total_sum - array_sum
#     return missing_number

# print(missingNumber(nums))

# Xor method

nums = [9,6,4,2,3,5,7,0,1]
nums = [3, 0, 1]
def missingNumber(nums):
    xor = 0
    for i in range(len(nums)):
        xor ^= i
        xor ^= nums[i]
    xor ^= len(nums)
    return xor


print(missingNumber(nums))
