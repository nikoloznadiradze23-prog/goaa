# range(start, stop, step)
# for number in "goa":
#     print(number)
# total=0
# for num in range(0, 11, 1):
#     print(num)
#     total += num
#     print(total)

# print("hello")



# i = 0
# while i>0: 
#     print(i) or (i % 2 == 0)
#     i += 1
# print("loop ended")

test = 21
while test <41: 
    test += 1
    print("test")  

print("end")

test1 = 51
while test1 <= 101: 
    test1 += 1
    print("test1") 

print("end")

test2 = 19
while test2 >= 0: 
    test2 -= 1
    print("test2")  

print("end")

pin_code = "2144"

code = input("enter your pin code:")
while (code != pin_code) and (attemps > 3):
    attemps -=1
    print ("attemps" + str(attemps))
    code = input("enter pin code:")
print("autorized")