def saddle_points(matrix):
    saddle, maxes, mins = [], [], []
    columns = [[0]*len(matrix) for x in range(len(matrix[0]))]
    for i, row in enumerate(matrix):
        for i2, c in enumerate(row):
            columns[i2][i] = c
        maxes.append(max(row))
    for col in columns:
        mins.append(min(col))
    for x, n1 in enumerate(maxes):
        for y, n2 in enumerate(mins):
            if n1 == n2:
                saddle.append({"row" : x + 1, "column" : y + 1})
    return saddle
