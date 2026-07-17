# Input
# arr = [7, 2, 15, 9, 4]
# Output
# 15

arr = [7,2,15,9,4]
max_element = arr[0]
for i in arr:
    if max_element < i :
        max_element = i
print(max_element)