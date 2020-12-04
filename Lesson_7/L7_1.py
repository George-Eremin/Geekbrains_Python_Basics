class Matrix:
    matrix_list = []
    __matrix_str = ''

    def __init__(self, args_list: []):
        self.matrix_list = []
        for arg in args_list:
            # Проверяем, одинаковое ли количество столбцов в каждой строке
            if len(arg) == len(args_list[0]):
                self.matrix_list.append(arg)
            # Если нет - выдаем ошибку
            else:
                print('В каждой строке матрицы должно быть одинаковое количество столбцов')
                exit(1)

    def __str__(self):
        self.__matrix_str = ''
        for raw in self.matrix_list:
            for column in raw:
                self.__matrix_str += f'{column}\t'
            self.__matrix_str += '\n'
        return self.__matrix_str

    def __add__(self, other):
        __matrix_temp = []
        __raw_temp = []
        # Проверяем равенство размеров матриц по строкам и столбцам
        if len(self.matrix_list) != len(other.matrix_list) or len(self.matrix_list[0]) != len(other.matrix_list[0]):
            print('Матрицы должны иметь одинаковые размеры для выполнения операции сложения')
            exit(1)
        for raw in range(len(self.matrix_list)):
            __raw_temp = []
            for column in range(len(self.matrix_list[raw])):
                __raw_temp.append(self.matrix_list[raw][column] + other.matrix_list[raw][column])
            __matrix_temp.append(__raw_temp)
        return Matrix(__matrix_temp)


M1 = Matrix([
    [3, 5, 7],
    [2, 4, 6]])
print(f'Создана матрица M1:\n{M1}')

M2 = Matrix([
    [1, 1, 1],
    [10, 10, 10]])
print(f'Создана матрица M2:\n{M2}')

M3 = M1 + M2
print(f'Создана матрица M3 = M1 + M2:\n{M3}')
