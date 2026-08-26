
nums = {1, 2, 3, 4, 5, 6, 7, 8, }

def manual_index(nums):
    i = 0
    for x in nums:
        if x == nums:
            return i
        i += 1
        return -1
        

def manual_count(numrs):
    count = 0
    for x in numrs:
        if x == numrs: 
            count += 1
    return count

fruits = ["apple", "banana", "orange", "banana"]
colors = ["red", "blue", "green", "blue"]
numbers = [5, 2, 9, 1, 2]

fruits.index("banana")
colors.index("green")
numbers.index(9)

fruits.count("banana")
colors.count("blue")
numbers.count(2)   


fruits.sort()
colors.sort()
numbers.sort()

sorted(fruits)
sorted(colors)
sorted(numbers)

min(fruits)
min(colors)
min(numbers)


max(fruits)
max(colors)
max(numbers)

animals = ("dog", "cat", "lion", "dog")
animals.count("cat")
animals.count("dog")
animals.index("lion")
animals.index("cat")

