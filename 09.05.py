#симулятор навчального закладу (база даних)
class School:
    def __init__(self, name, students):
        self.name = name
        self.students + students #список студентів
    def admit__student(self, student):
        self.student.append(student)
        print(f'{student.name} був допущений до школи {self.name}') #дописати, коли створимо клас студентів

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def promote(self):
        self.grade += 1
        print(f'{self.name} був підвищений до {self.grade}')
    def demote(self):
        self.grade -= 1
        print(f'{self.name} був понижений до {self.grade}')




