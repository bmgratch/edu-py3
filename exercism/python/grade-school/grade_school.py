from collections import defaultdict

class School:
    def __init__(self):
        self.grades = defaultdict(list)

    def add_student(self, name, grade):
        if not grade in self.grades.keys():
            self.grades[grade] = []
        self.grades[grade].append(name)

    def roster(self):
        ros = []
        for grade in sorted(self.grades.keys()):
            ros += sorted(self.grades[grade])
        return ros

    def grade(self, grade_number):
        return sorted(self.grades[grade_number])
