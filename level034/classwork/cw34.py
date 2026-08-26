fruits = ("apple","banana","cherry","orange","kiwi")

def manual_index(sequence, target):
    for index in range(len(sequence)):
        if sequence[index] == target:
            return index
    return - 1
print(manual_index(fruits, "cherry"))
nums=(10,20,30,40,50)

first,second,*other = nums
print(min(nums))
print(max(nums))


nums = [1,2,2,3,4,4,4,5]
res = list(set(nums))
print(res)

nums.remove(1)
nums.add(8)
print(nums)


nums1 = {1,2,3,4,5,}
nums2 = {5,6,7,8,9}
print(nums1.union(nums2))
print(nums1.intersection(nums2))
print(nums1.difference(nums2))
print(nums1.symmetric_difference(nums2))