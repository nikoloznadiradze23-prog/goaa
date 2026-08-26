for num in range(21):
    if num % 2 == 0:
        print("even", num)
    else:
        print("odd", num)

num = 0
while num <= 20:
    if num % 2 == 0:
        print("even", num)
    else:
        print("odd", num)
    num += 1

name = "nikoloz"
user_name = input("enter your name: ")
if user_name == name:
    print("coincidence")

score = int(input("enter score: "))
if score >= 70:
    print("passed")
else:
    print("failed")

score = int(input("enter grade:"))
if score > 80:
    grade = "a"
elif score > 60:
    grade = "b"
elif score > 40:
    grade = "c"
elif score > 20:
    grade = "d"
else:
    grade = "f"
print("grade:", grade)

sum_positive = 0
while True:
    num = int(input("enter num : "))
    if num < 0:
        break  
    if num > 0:
        sum_positive += num
print("positive sum: ", sum_positive)


correct_pin = "1234"
max_attempts = 3
for attempt in range(max_attempts):
    entered_pin = input("enter pin code: ")
    if entered_pin == correct_pin:
        print("Access Granted")
        break
    else:
        print("Incorrect PIN")
else:
    print("Access Denied")
