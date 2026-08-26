def insertion_sort(arr):
    for i in range(len(arr)):
        j=i
        while arr[j-1] > arr[j] and j>0:
            temp = arr[j-1]
            arr[j - 1] = arr[j]
            arr[j]=temp
            j-=1
        return arr