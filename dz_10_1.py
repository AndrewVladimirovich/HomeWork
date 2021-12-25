
mtrx_1 = [[3, 6, 4, 7, 9], [2, 3, 5, 1, 9], [7, 4, 2, 5, 7]]
mtrx_2 = [[3, 4, 3, 5, 7], [3, 3, 5, 5, 2], [1, 5, 3, 7, 7]]


class Matrix:
    def __int__(self, lists):
        self.lists = lists

    def __str__(self):
        return '\n'.join(map(str, self.lists))

    def __add__(self, other):
        mtrx_3 = []
        for n in range(len(self.lists)):
            mtrx_3.append([])
            for k in range(len(self.lists[0])):
                mtrx_3[n].append(self.lists[n][k] + other.lists[n][k])
        return '\n'.join(map(str, mtrx_3))


matrix_1 = Matrix(mtrx_1)
matrix_2 = Matrix(mtrx_2)
print(f'Matrix 1\n{matrix_1}\n{"-" * 20}')
print(f'Matrix 2\n{matrix_2}\n{"-" * 20}')
print(f'matrix 1 + matrix 2\n{matrix_1 + matrix_2}')


