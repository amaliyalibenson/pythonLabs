#сначала у введеной строки меняю запятые, потом превращаю это в вещ-ное число
a= float(str(input('a: ')).replace(',', '.'))
b= float(str(input('b: ')).replace(',', '.'))
avg=((a+b)/2)
print('sum='+str(a+b)+'; avg='+str(round(avg,2)))