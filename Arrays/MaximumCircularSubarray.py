arr = [1,-2,3,-2]
arr = [4, -5, 6, 7]
arr = [3, -2, 2, -3,7]
arr=[2,-3,4,5,-7,5]
def circular_sum(arr):
    current_sum,total_sum,current_min_sum  =0,0,0
    max_sum = arr[0]    
    min_sum =arr[0]
    for i in arr:
        total_sum +=i
        
        current_sum += i
        max_sum = max(max_sum , current_sum)
        if current_sum < 0:
            current_sum = 0
        
        current_min_sum +=i
        min_sum = min(min_sum , current_min_sum)
        if current_min_sum > 0:
            current_min_sum = 0

    if max_sum < 0:
        return max_sum
    else:
        return max(max_sum,total_sum - min_sum)

print(circular_sum(arr))
