class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list




    # def __str__(self):
    #   return '\n'.join(map(str, self.my_list))

    def __str__(self):
         return str('\n'.join(['\t'.join([str(el) for el in i]) for i in self.my_list]))

    def __add__(self, other):
        A = self.my_list
        B = other.my_list
        C = A.copy()
        for i in range(len(self.my_list)):
            for j in range(len(other.my_list[i])):
                C[i][j] = A[i][j] + B[i][j]
        return '\n'.join([''.join(['%d\t' % i for i in row]) for row in C])


m = Matrix([[4, 5, 1], [4, 0, 3], [2, 1, 2], [4, 6, 1]])
new_m = Matrix([[3, 0, 7], [1, 0, 5], [6, 5, 3], [2, 2, 8]])


print(m)
print()
print(new_m)
print()
print(m + new_m)