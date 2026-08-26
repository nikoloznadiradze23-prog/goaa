class Group:
    def __init__(self, mentor, students, assistant):
        self.mentor = mentor
        self.students = students
        self.assistant = assistant
    def get_assistant(self):
        return self.assistant

group_88 = Group("luka", 15, "Giorgi")
print(group_88.mentor)
print(group_88.students)
print(group_88.get_assistant())