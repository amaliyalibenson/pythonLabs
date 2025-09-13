n = int(input('in_1: '))
och=0
zaoch=0
for i in range(n):
    s= str(input('id:'))
    s=s.split()
    #инфу об студенте разбиваю по сплитам и беру самый последний
    s1=s[-1]
    if s1=='True':
        och+=1
    else:
        zaoch+=1

print('очно:',och, ' заочно:',zaoch, sep='')