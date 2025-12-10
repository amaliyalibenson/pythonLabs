# transpose
def transpose(mat: list[list[float | int]]) -> list[list]:
    """
    Поменять строки и столбцы местами. Пустая матрица [] → [].
    Если матрица «рваная» (строки разной длины) — ValueError
    """
    if not all(len(x) == len(mat[0]) for x in mat):  # если не все равны друг другу
        return "ValueError"

    elif len(mat) == 0:
        return []

    res = [[0 for i in range(len(mat))] for x in range(len(mat[0]))]
    # кол-во рядов это кол-во строк и наоборот
    for x in range(len(mat)):
        for y in range(len(mat[x])):
            res[y][x] = mat[x][y]
    return res


m = [[1, 2, 3]]
m1 = [[1], [2], [3]]
m2 = [[1, 2], [3, 4]]
m3 = []
m4 = [[1, 2], [3]]
print(transpose(m))
print(transpose(m1))
print(transpose(m2))
print(transpose(m3))
print(transpose(m4))


# row_sums
def row_sums(mat: list[list[float | int]]) -> list[float]:
    """
    Сумма по каждой строке. Требуется прямоугольность
    """
    if not all(len(x) == len(mat[0]) for x in mat):
        return "ValueError"

    res = []
    for x in mat:
        sum = 0
        for i in range(len(x)):
            sum += x[i]
        res.append(sum)
    return res


m = [[1, 2, 3], [4, 5, 6]]
m2 = [[-1, 1], [10, -10]]
m3 = [[0, 0], [0, 0]]
m4 = [[1, 2], [3]]
print(row_sums(m))
print(row_sums(m2))
print(row_sums(m3))
print(row_sums(m4))


# col_sums
def col_sums(mat: list[list[float | int]]) -> list[float]:
    """
    Сумма по каждому столбцу. Требуется прямоугольность
    """
    if not all(len(x) == len(mat[0]) for x in mat):
        return "ValueError"

    res = []
    for y in range(len(mat[0])):
        s = 0
        for x in range(len(mat)):
            s += mat[x][y]
        res.append(s)
    return res


m = [[1, 2, 3], [4, 5, 6]]
m2 = [[-1, 1], [10, -10]]
m3 = [[0, 0], [0, 0]]
m4 = [[1, 2], [3]]
print(col_sums(m))
print(col_sums(m2))
print(col_sums(m3))
print(col_sums(m4))
