# def main():
#     text = input("enter 4 word: ")
#     with open("words.txt", "w", encoding="utf-8") as f:
#         f.write(text)
#     with open("words.txt", "r", encoding="utf-8") as f:
#         content = f.read()
#     words = content.split()
#     consonants = "wawtzkWYhfzhdREHJREDewysg"
#     consonant = sum(1 for ch in content.lower() if ch in consonants)
#     shortest = min(words, key=len)
#     processed_text = content.swapcase()
#     with open("processed.txt", "w", encoding="utf-8") as f:
#         f.write(processed_text)
#     print(len(words))
#     print(consonant)
#     print(shortest)



students = {
    "ana": [95, 88, 92, 85, 90],
    "giorgi": [70, 75, 68, 72, 74],
    "mariami": [82, 85, 80, 88, 84],
    "nika": [60, 55, 58, 62, 59],
    "luka": [40, 45, 38, 42, 44]
}
def average(scores):
    return sum(scores) / len(scores)
def grade(average):
    if 91 <= average <= 100:
        return "A"
    elif 81 <= average <= 90:
        return "B"
    elif 71 <= average <= 80:
        return "C"
    elif 61 <= average <= 70:
        return "D"
    elif 51 <= average <= 60:
        return "E"
    elif 41 <= average <= 50:
        return "FX"
    else:
        return "F"
def calculate_average(scores):
    return sum(scores) / len(scores)
def get_grade(average):
    if 91 <= average <= 100: return "A"
    if 81 <= average <= 90: return "B"
    if 71 <= average <= 80: return "C"
    if 61 <= average <= 70: return "D"
    if 51 <= average <= 60: return "E"
    if 41 <= average <= 50: return "FX"
    return "F"
def average(item):
    return item[1]
def average(item):
    return average(item[1])
def find_top_student(students_dict):
    return max(dict.items(), key=average)
results = []
for name, scores in students.items():
    avg = average(scores)
    grade = grade(avg)
    results.append((name, avg, grade))
results.sort(key=average, reverse=True)
top_name, top_scores = find_top_student(students)
top_avg = average(top_scores)
print("answers:")
for name, avg, grade in results:
    print(f"{name}: mid = {avg:.2f}, rate = {grade}")
print("\nbest:")
print(f"{top_name}: mid = {top_avg:.2f}, rate = {get_grade(top_avg)}")
