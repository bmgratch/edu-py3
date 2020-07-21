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
        self.plots = {}
        plot_max = len(self.diagram[0])//2
        for plot in range(0, plot_max):
            self.plots[self.students[plot]] = [
                self.diagram[0][plot*2],
                self.diagram[0][(plot*2)+1],
                self.diagram[1][plot*2],
                self.diagram[1][(plot*2)+1]]
            

    def plants(self, student):
        if student not in self.plots.keys():
            return None
        return [SEEDS[seed] for seed in self.plots[student]]
