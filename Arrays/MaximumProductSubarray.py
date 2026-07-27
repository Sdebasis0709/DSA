# arr = [2, 3, -2, 4]
# arr = [-2, 3, -4]
# arr = [-2, -3, -4, -5]
arr = [2, -5, -2]
# arr = [2, -5]
max_end ,min_end =arr[0],arr[0]
ans =arr[0]
for i in arr[1:]:
    if i < 0:
        max_end,min_end = min_end,max_end
    max_end = max(max_end*i,i)
    min_end = min(min_end*i,i)
    ans = max(ans,max_end)
print(ans)


