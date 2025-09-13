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