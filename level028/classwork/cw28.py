listt=[1,2,3,4,5,6,7,8,9]
listt.append(10)
listt.insert(7, "9")
listt.pop(2)
print(listt)



nums= [1,2,3,4,5,7,6,8,9,10]
for index in range(len(nums)):
    if index % 2 == 0:
        odds.append(nums[index])
        print(nums)

nums.extend("aBc")

nums.sort()
print(nums)



def greet(first_name, last_name):
    return "hello"+first_name,last_name
message = greet("fname", "lname")
print(message)