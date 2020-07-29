from collections import defaultdict

class School:
    def __init__(self):
        self.grades = defaultdict(list)

    def add_student(self, name, grade):
        self.grades[grade].append(name)

    def roster(self):
        return [student for grade in sorted(self.grades) for student in sorted(self.grades[grade])]

    def grade(self, grade_number):
        return sorted(self.grades[grade_number])
