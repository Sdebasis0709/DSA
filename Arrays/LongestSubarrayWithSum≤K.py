# Question 1
# arr = [2, 1, 3, 2, 4, 1]
# k = 7
arr = [2, 1, 3, 1,2, 4, 1]
left, right = 0,0
max_length = 0
current_sum = 0
k= 7

while left <= right and right < len(arr):
    current_sum += arr[right]
    while current_sum > k:
        current_sum -= arr[left]
        left += 1
    max_length = max(max_length, right - left + 1)
    right += 1
print(max_length)