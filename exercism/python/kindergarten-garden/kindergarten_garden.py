STUDENTS = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']
SEEDS = {
    'V': 'Violets',
    'R': 'Radishes',
    'G': 'Grass',
    'C': 'Clover'}

class Garden:
    def __init__(self, diagram, students=STUDENTS):
        self.students = sorted(students)
        self.diagram = diagram.split('\n')

    def plants(self, student):
        if student not in self.students:
            return None
        else:
            plot = self.students.index(student)*2
        seeds = [self.diagram[0][plot],
                 self.diagram[0][plot+1],
                 self.diagram[1][plot],
                 self.diagram[1][plot+1]]
        return [SEEDS[seed] for seed in seeds]
