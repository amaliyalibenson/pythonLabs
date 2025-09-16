# ЛР1
### Задание №1
```
name = str(input('Имя: '))
age = int(input('Возраст: '))
print('Привет, '+name+'! Через год тебе будет '+str(age+1)+'.')
```
![имя и возраст](/images/lab01/ex01.png)

### Задание №2
```
#сначала у введеной строки меняю запятые, потом превращаю это в вещ-ное число
a= float(str(input('a: ')).replace(',', '.'))
b= float(str(input('b: ')).replace(',', '.'))
avg=((a+b)/2)
print('sum='+str(a+b)+'; avg='+str(round(avg,2)))
```
![nomer 2](/images/lab01/ex02.png)

### Задание №3
```
price = float(input('Цена :'))
discount = float(input('Скидка :'))
vat = float(input('НДС :'))
base = price * (1 - discount/100)
vat = base * (vat/100)
total = base + vat
print('База после скидки:', round(base,2))
print('НДС:', round(vat,2))
print('Итого к оплате:', round(total,2))
```
![nomer 2](/images/lab01/ex03.png)

### Задание №4
```
m = int(input('Минуты: '))
hour= m//60
minut = m % 60
print(hour, ':', minut, sep = '')
```
![nomer 2](/images/lab01/ex04.png)

### Задание №5
```
s=str(input('ФИО: '))
otvet=''
otvet2=0
for i in s:
    #прохожусь по строке
    if i.isupper():
        otvet+=i
        #если попался верхний регистр, то его записываю в ответ
    if i!=' ':
        otvet2+=1
        #считаю символы без лишних пробелов

print(otvet2+2, otvet+'.')
```
![nomer 2](/images/lab01/ex05.png)

### Задание №6
```
n = int(input('in_1: '))
och=0
zaoch=0
for i in range(n):
    s= str(input('id:'))
    s=s.split()
    #инфу об студенте разбиваю по сплитам и беру самый последний3
    s1=s[-1]
    if s1=='True':
        och+=1
    else:
        zaoch+=1

print('очно:',och, ' заочно:',zaoch, sep='')
```
![nomer 2](/images/lab01/ex06.png)

### Задание №7
```
s=str(input('in:'))
index1=0
index2=0
w=0
# нахожу индекс первого вхождения верхнего регистра
for r in s:
    if r.isupper():
        index1=w
        break
    w += 1
# нахожу индекс второй буквы по первому вхождению цифры
for i in range(len(s)):
    if s[i] in '0123456789':
        index2=i+1
        break
itog=''
#прохожусь по списку с шагом, который я вычислила из двух индексов
for q in range(index1, len(s)+1, index2-index1):
    if s[q]=='.':
        #конец шифра
        itog+='.'
        break
    else:
        itog+=s[q]
print(itog)
```
![nomer 2](/images/lab01/ex07.png)
🤍
