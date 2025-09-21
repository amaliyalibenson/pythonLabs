# ЛР2
### Задание №1 А
```python
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
```
![min_max](/images/lab02/ex01a.png)

### Задание №1 B
```python
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
```
![unique_sorted](/images/lab02/ex01b.png)

### Задание №1 C
```python
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
```
![flatten](/images/lab02/ex01c.png)

### Задание №2 A
```python
#transpose
def transpose(mat: list[list[float | int]]) -> list[list]:
    '''
    Поменять строки и столбцы местами. Пустая матрица [] → [].
    Если матрица «рваная» (строки разной длины) — ValueError
    '''
    if not all(len(x)==len(mat[0]) for x in mat): #если не все равны друг другу
        return 'ValueError'

    elif len(mat)==0:
        return []

    res=[[0 for i in range(len(mat))]for x in range(len(mat[0]))]
    #кол-во рядов это кол-во строк и наоборот
    for x in range(len(mat)):
        for y in range(len(mat[x])):
            res[y][x]=mat[x][y]
    return res
m=[[1, 2, 3]]
m1=[[1], [2], [3]]
m2=[[1, 2], [3, 4]]
m3=[]
m4=[[1, 2], [3]]
print(transpose(m))
print(transpose(m1))
print(transpose(m2))
print(transpose(m3))
print(transpose(m4))
```
![transpose](/images/lab02/ex02a.png)

### Задание №2 B
```python
#row_sums
def row_sums(mat: list[list[float | int]]) -> list[float]:
    '''
    Сумма по каждой строке. Требуется прямоугольность
    '''
    if not all(len(x)==len(mat[0]) for x in mat):
        return 'ValueError'

    res=[]
    for x in mat:
        sum=0
        for i in range(len(x)):
            sum+=x[i]
        res.append(sum)
    return res
m=[[1, 2, 3],[4, 5, 6]]
m2=[[-1, 1], [10, -10]]
m3=[[0, 0], [0, 0]]
m4=[[1, 2], [3]]
print(row_sums(m))
print(row_sums(m2))
print(row_sums(m3))
print(row_sums(m4))
```
![#row_sums](/images/lab02/ex02b.png)

### Задание №2 C
```python
#col_sums
def col_sums(mat: list[list[float | int]]) -> list[float]:
    """
    Сумма по каждому столбцу. Требуется прямоугольность
    """
    if not all(len(x) == len(mat[0]) for x in mat):
        return 'ValueError'

    res=[]
    for y in range(len(mat[0])):
        s=0
        for x in range(len(mat)):
            s+=mat[x][y]
        res.append(s)
    return res
m=[[1, 2, 3], [4, 5, 6]]
m2=[[-1, 1], [10, -10]]
m3=[[0, 0], [0, 0]]
m4=[[1, 2], [3]]
print(col_sums(m))
print(col_sums(m2))
print(col_sums(m3))
print(col_sums(m4))
```
![col_sums](/images/lab02/ex02c.png)

### Задание №3
```python
def format_record(rec: tuple[str, str, float]) -> str:
    if any(str(x)=='' for x in rec):
        return 'ValueError'

    fio=str(rec[0]).split()
    group=str(rec[1])
    gpa=f'{float(rec[2]):.2f}'
    fio1=''
    flag=0 #флаг для фамилии

    for i in range(len(fio)):
        if fio[i]!='' and flag==0:
            first_let=str(fio[i])[0].upper() #первую букву в фамилии в верхний регистр
            fio1+=first_let+str(fio[i][1:])+' ' #вся фамилия с большой буквы
            flag=1
        elif fio[i]!='' and flag==1:
            first_let=str(fio[i])[0].upper()
            fio1 += first_let + '.'
            #просто инициалы сохраняем
    res=fio1+', гр. '+group+', GPA '+str(gpa)
    return res
r=("Иванов Иван Иванович", "BIVT-25", 4.6)
r2=("Петров Пётр", "IKBO-12", 5.0)
r3=("Петров Пётр Петрович", "IKBO-12", 5.0)
r4=("  сидорова  анна   сергеевна ", "ABB-01", 3.999)
print(format_record(r))
print(format_record(r2))
print(format_record(r3))
print(format_record(r4))
```
![tuples](/images/lab02/ex03.png)