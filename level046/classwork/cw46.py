# events = ["bmw","lamborghini","range rover","jaguar"]
# index = int(input())
# try:
#     print(events[5])
# except IndexError:
#     print("index error")
# except SyntaxError:
#     print("syntax error nigga")
# else:
#     ("event successfuly fount")
# finally:
#     print("code block of finally")


# try:
#     index = int(input())
# except IndexError:
#     print(" zangi")
# except ValueError:
#     print("value erorrr")

# sentence = "1"
# sentences = []


# while sentence != "":
#     sentence = input("enter a sentence:  ")
#     sentences.append(sentence)
# sentences.pop()
# print(sentence)

# file_name = "sents.txt"
# with open(file_name, "w",encoding="utf-8") as file:
#     for sentence in sentences:
#         file.writelines(sentence + "\n")
# with open(file_name, "r" , encoding="utf-8") as file:
#     lines = file.reading()
#     words_count = []
#     for line in lines:
#         line = line.strip()
#         words = line.split(' ')
#         words_count.append(len(words))
#         longest_line = max(words_count)
#         longest_index = words_count.index(longest_line)
#         longest_line = lines[longest_index]
#         print(longest_line)

