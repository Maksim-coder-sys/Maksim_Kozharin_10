class Cell:
    def __init__(self, quan):
        self.quan = int(quan)

    def __add__(self, other):
        return f' Размер клетки равен: {self.quan + other.quan}'

    def __sub__(self, other):
        sub = self.quan - other.quan
        return f'Клетка стала меньше, теперь она равна: {sub} клеточкам' if sub > 0 else 'Клетка исчезла'

    def __truediv__(self, other):
        return self.quan // other.quan

    def __mul__(self, other):
        return self.quan * other.quan

    def make_order(self, row):
        result = ''
        for i in range(int(self.quan / row)):
            result += '*' * row + '\n'
        result += '*' * (self.quan % row) + '\n'
        return result


cell = Cell(24)
cell_2 = Cell(2)
print(cell + cell_2)
print(cell - cell_2)
print(cell / cell_2)
print(cell * cell_2)
print(cell.make_order(7))