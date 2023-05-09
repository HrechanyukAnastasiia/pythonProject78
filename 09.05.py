#симулятор навчального закладу (база даних)
class School:
    def __init__(self, name, students):
        self.name = name
        self.students + students #список студентів
    def admit__student(self, student):
        self.student.append(student)
        print(f'{student.name} був допущений до школи {self.name}') #дописати, коли створимо клас студентів

    def expel_student(self, student):
        expelled_student = next(filter(lambda s: s.name == student.name
                                                 and s.grade = student.grade, self.students), None)
        if expelled_student is not None:
            self.student.remove(expelled_student)
            print(f'{expelled_student.name} був видалений з {self.name}')
        else:
            print(f'{student.name} не був знайдений {self.name}')

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
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = list(filter(lambda x : x % 2 == 0, numbers))
print(filtered_numbers)

lisa = Student("Alisa", 6)
masha = Student("Maria", 2)
andriiko = Student("Andriy", 50)
dima = Student("Dmytro", 23)
gleb = Student("Gleb", 100)
my_school = School("ItStep", [lisa, masha, andriiko, dima, gleb])
print("Початкові студенти")
for student in my_school.students:
    print(student)

my_school.admit__student(Student("Bogdan", 3))
my_school.expel_student(Student("Alisa"))
print("Оновлення")
for student in my_school.students:
    print(student)