#симулятор навчального закладу (база даних)
class School:
    def __init__(self, name, students):
        self.name = name
        self.students + students #список студентів
    def admit__student(self, student):
        self.student.append(student)
        print(f'{student.name} був допущений до школи {self.name}') #дописати, коли створимо клас студентів

    def expel_student(self, student):
        '''expelled_student ='''
        pass



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
    def __str__(self):
        return f'{self.name} - Ранг {self.grade}'

multiplay = lambda x, y: x * y
print(multiplay(2,5))


