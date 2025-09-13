price = float(input('Цена :'))
discount = float(input('Скидка :'))
vat = float(input('НДС :'))
base = price * (1 - discount/100)
vat = base * (vat/100)
total = base + vat
print('База после скидки:', round(base,2))
print('НДС:', round(vat,2))
print('Итого к оплате:', round(total,2))

