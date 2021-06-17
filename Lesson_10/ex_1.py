from sys import stdin
from copy import deepcopy

class Matrix(object):
    def __init__(self, matrix):
        self.matrix = deepcopy(matrix)

    def __str__(self):
        return '\n'.join('\t'.join(map(str,row)) for row in self.matrix)

    def size(self):
        return (len(self.matrix), len(self.matrix[0]))

    def __add__(self, other):
        matrix = []
        for i in range(len(self.matrix)):
            matrix.append([])
            for j in range(len(self.matrix[0])):
                matrix[i].append(self.matrix[i][j] + other.matrix[i][j])
        return Matrix(matrix)


a1 = Matrix([[1, 2, 5], [3, 4, 10], [5, 6, 15]])
a2 = Matrix([[3, 2, 1], [6, 5, 4], [9, 8, 7]])
print(str(a1))
print(str(a1.size()))
print(a1 + a2)
