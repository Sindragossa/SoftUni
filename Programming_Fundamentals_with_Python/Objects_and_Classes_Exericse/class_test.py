class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        if Class.__students_count:
            Class.__students_count -= 1
            self.students.append(name)
            self.grades.append(float(grade))

    def get_average_grade(self):
        return sum(self.grades) / len(self.students)

    def __repr__(self):
        score = self.get_average_grade()
        return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {score:.2f}"


a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)
