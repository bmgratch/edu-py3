class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string   
        self.rows = self.matrix_string.split('\n')
        for x in range(0, len(self.rows)):
            n = []
            for i in self.rows[x].split():
                n.append(int(i))
            self.rows[x] = n

    def row(self, index):
        return self.rows[index - 1]

    def column(self, index):
        col = []
        for x in self.rows:
            col.append(x[index-1])
        return col
