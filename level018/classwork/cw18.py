# score = int(input("type score:"))
# mid = int(input("type mid:"))
# if score > mid:
#     print("pass")
# if score < mid:
#     print("fail")
# if score > mid:
#     print("grade a")
# if score < mid:
#     print("grade b")

# exam_score = int(input("score:"))

# mid = int(input("mid:"))

# if exam_score > mid:
#     print("A")

# elif exam_score == mid:
#     print("B")

# elif exam_score < mid:
#     print("C")



# num = int(input("num:"))

# if(num % 2 ) == 0:
#     print("even")

# else:
#     print("odd")


# exam_score = int(input())

# if exam_score > 90:
#     print("A")

# elif exam_score > 80:
#     print("B")

# elif exam_score > 70:
#     print("C")

# elif exam_score > 60:
#     print("d")

# elif exam_score > 50:
#     print("e")

# elif exam_score > 40:
#     print("f")

# else:
#     print("G")



# secret = "1234"

# attemps = 3
# pincode = ""
# while (secret != pincode) and (attemps > 0 ):
#     pincode = input("pin")
#     attemps = -1
#     print(f"you have {attemps} attemps left")
#     if secret == pincode:
#         print("welcome")
#         break

for i in range (30, 61):
    if i ==50:
        continue
    if i ==55:
        break
    print(i)