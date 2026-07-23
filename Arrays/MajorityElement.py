arr = [3, 3, 4, 2, 3]
major,count = 0,0
for i in range(len(arr)):
    if count == 0:
        major = arr[i]
        count +=1
    elif major == arr[i]:
        count +=1
    else:
        count -=1
major_ele = arr.count(major) > len(arr)//2
if major_ele:
    print(major)
else:
    print(None)


print(major)