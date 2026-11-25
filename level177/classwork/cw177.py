# def power_recursion(n, e):
#     if e <= 0:
#         return 1

#     return n * power_recursion(n, e - 1)
# print(power_recursion(2, 2))


# mass = [1,2,3,4,5,6,7,8,9,10];

# def find_max(arr):
#     highest = arr[0]
#     for element in mass :
#         if element > highest:
#             highest = element
#     return highest

# print(find_max([1,2,3,4,5,6,7,8,9,10]))




def bubble_sort(arr):
    for i in range(len(arr)):
        j=1
        while j < len(arr):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            j+=i
mass = [1,2,4,3,5,6,7,8,9,10];
