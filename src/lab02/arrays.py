# min_max
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    """
    вернуть кортеж (минимум, максимум). если список пуст — ValueError.
    """
    if len(nums) == 0:
        return 'ValueError'
    return (min(nums), max(nums))

a = str(input())
# a2 = str(input()) и тд
l = [int(float(x)) for x in a.split() if float(x) % 1 == 0] + [float(i) for i in a.split() if float(i) % 1 != 0]
# l2 аналогично
print(min_max(l))
# print(min_max(l2)) и тд


# unique_sorted
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    """
    Вернуть отсортированный список уникальных значений (по возрастанию)
    """
    nums.sort()
    res=[]
    maxi=-9999
    for x in nums:
        if x>maxi:
            res.append(x)
            maxi=x
    return res
a = str(input())
# a2 = str(input()) и тд
l = [int(float(x)) for x in a.split() if float(x) % 1 == 0] + [float(i) for i in a.split() if float(i) % 1 != 0]
# l2 аналогично
print(unique_sorted(l))
# print(unique_sorted(l2)) и тд


#flatten
def flatten(mat: list[list | tuple]) -> list:
    '''
    «Расплющить» список списков/кортежей в один список по строкам. Если встретилась строка/элемент, который не является списком/кортежем — TypeError
    '''
    for x in mat:
        if not(isinstance(x, list) or isinstance(x, tuple)):
            return 'TypeError'
    res=[]
    for x in range(len(mat)):
        for y in range(len(mat[x])):
            res.append(mat[x][y])
    return res
m=[[1, 2], [3, 4]]
m2=([1, 2], (3, 4, 5))
m3=[[1], [], [2, 3]]
m4=[[1, 2], "ab"]
print(flatten(m))
print(flatten(m2))
print(flatten(m3))
print(flatten(m4))

