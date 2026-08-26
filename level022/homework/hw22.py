veg_list = ["tomato","potato","brocoli","bean"]
veg_list[2] = "carrot"
veg_list[3] = "cucumber"
print(veg_list)


veg_list = ["tomato","potato","brocoli","bean"]
user_choice = int(input("choose 0-3:" ))
if user_choice == 0 or user_choice == 1 or  user_choice == 2 or  user_choice == 3:

print("your choice is:", veg_list[user_choice])
else:
print("error")

num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(num[5:10])

num1 = ["sun","mercury","earth","mars","saturn"]
print(num1[::2])

num2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(num2[::3])

string = ["nikoloz", "nadiradze"]
print(string[0:1])
print(string[1:2])