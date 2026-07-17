# Example:

# [1, 2, 3, 4, 5]

# k = 1

# Shift sabko ek step left:
# [2, 3, 4, 5, ?]

# Last mein temp:
# [2, 3, 4, 5, 1]


# # Brute Force
# arr= [1,2,3,4,5,6,7]
# k=3
# for i in range(k):
#     temp = arr[0]
#     arr.remove(arr[0])
#     arr.append(temp)
# print(arr)

# optimal solution

# arr =[ 1,2,3,4,5,6,7]
# k= 3
# l,r,m=0,len(arr)-1,k-1
# while l < m:
#     arr[l],arr[m] = arr[m],arr[l]
#     m-=1
#     l+=1
# print("array",arr)
# print(f"l-{l}-r-{r}-m-{m}")
# while k<r:
#     arr[k],arr[r] = arr[r],arr[k]
#     k+=1
#     r-=1
# left,right = 0,len(arr)-1
# while left < right:
#     arr[left],arr[right] = arr[right],arr[left]
#     left +=1
#     right-=1
# print(arr)



# rotate array by k element

arr =[ 1,2,3,4,  5,6,7]
k= 3
def rotate_right(left:int,right:int,arr):
    while left < right:
        arr[left] ,arr[right] = arr[right],arr[left]
        left +=1 
        right -=1
    return arr

rotate_right(len(arr)-k,len(arr)-1,arr)
print(arr)
rotate_right(0,len(arr)-k-1,arr)
print(arr)
rotate_right(0,len(arr)-1,arr)
print(arr)