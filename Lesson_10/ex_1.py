from sys import stdin
from copy import deepcopy

class Matrix(object):
    def __init__(self, matrix):
        self.matrix = deepcopy(matrix)

    def __str__(self):
        return '\n'.join('\t'.join(map(str,row)) for row in self.matrix)

    def size(self):
        return (len(self.matrix), len(self.matrix[0]))


a1 = Matrix([[1, 2, 5], [3, 4, 10], [5, 6, 15]])

print(str(a1))
print(str(a1.size()))
