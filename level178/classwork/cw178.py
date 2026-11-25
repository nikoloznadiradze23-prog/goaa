

arr = [2,5,7,8,4,6]

def insertion(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
insertion(arr)
print(arr)




# def merge_sort(arr):
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             arr[k] = left[i] 
#             i += 1
#     else:
#         arr[k] = right[j]
#         j += 1
#         k += 1
