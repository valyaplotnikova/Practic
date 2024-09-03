def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            if value <= 0:
                continue
            else:
                matrix[i].append(value)
    return matrix


