# Find Maximum Sum of Window Size K

# Array
# arr=[2,4,6,8,10]
# k
# 3
# Output
# 24


# # brute force solution


# arr=[2,4,6,8,10]
# k=3
# max_sum=0
# for i in range(k):
#     sum_of_window=0
#     print("this is i value--",{i})
#     print("this is j and i list value--",arr[i:k+i])
#     for j in range(i,k+i):
#         print("this is j value--",{j})
#         sum_of_window += arr[j]
#     print("sum-",sum_of_window)
#     if sum_of_window > max_sum:
#         max_sum = sum_of_window
#     print()

# print(max)


# optimised solution
arr=[2,4,6,8,10]
k=3
current_sum = 0

for i in range(k):
    current_sum += arr[i]
max_sum = current_sum
for i in   range(len(arr)-k):
    current_sum = current_sum - arr[i] + arr[i+k]
    if max_sum < current_sum:
        max_sum = current_sum

print(max_sum) 
    
