def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    '''
    Если casefold=True — привести к casefold
    Если yo2e=True — заменить все ё/Ё на е/Е.
    Убрать невидимые управляющие символы (например, \t, \r) → заменить на пробелы, схлопнуть повторяющиеся пробелы в один.
    '''
    if casefold == True:
        text = text.casefold()
        #к нижнему регистру привели
    if yo2e == True:
        text = text.replace('é', 'e').replace('è', 'e').replace('ê', 'e').replace('ë', 'e').replace('ē', 'e').replace('ĕ', 'e').replace('ė', 'e').replace('ę', 'e').replace('ё', 'e')
        #реплейсаем ешки
    spec = {'\t', '\r', '\n'}
    for x in spec:
        text = text.replace(x, ' ') #реплейсаем с помощью словаря
    while '  ' in text:  #удаляем двойные пробелы пока они есть
        text = text.replace('  ', ' ')
    text = text.strip()#подрезаем кончики

    return text



def tokenize(text: str) -> list[str]:
    '''
    Разбить на «слова» по небуквенно-цифровым разделителям.
    В качестве слова считаем последовательности символов \w (буквы/цифры/подчёркивание) плюс дефис внутри слова (например, по-настоящему).
    Числа (например, 2025) считаем словами.
    '''
    #работаем с нужными дефисами
    text_def=[]
    i=0
    while i<len(text):
        if text[i] == '-':
            if i > 0 and i < len(text) - 1: #если он не с краю
                if (text[i-1].isalnum() or text[i-1] == '_') and (text[i+1].isalnum() or text[i+1] == '_'): #слева и справа буквы или цифры или двойной дефис
                    text_def.append('_')  #временно заменяем дефис на подчёркивание
        else:
            text_def.append(text[i])
        i += 1
    text_def = ''.join(text_def)+' '

    #разбиваем по токенам
    slovo=''
    res=[]
    for x in text_def:
        if x.isalnum() or x=='_':
            slovo+=x
        else:
            if len(slovo)!=0:
                slovo=slovo.replace('_', '-')#обратно дефисы вставляем
                res.append(slovo) #добавляем слово
                slovo='' #освобождаем ячейку для след слова
    return res



def count_freq(tokens: list[str]) -> dict[str, int]:
    '''
    Подсчитать частоты, вернуть словарь слово → количество
    '''
    res={}
    for x in tokens:
        res[x]=res.get(x, 0) + 1 #функция для словаря (запомнить!)
    sorted_res = sorted(res.items(), key=lambda x: (x[0], x[1])) #items для словарей, превращает в список кортежей
    return dict(sorted_res)


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    '''
    Вернуть топ-N по убыванию частоты; при равенстве — по алфавиту слова.
    '''
    kolvo= count_freq(freq) #создаем с помощью айтемс список кортежей и делаем его полноценным списком (без "dict_items")
    return kolvo



'''
n="ПрИвЕт\nМИр\t"
print(normalize(n))

t="привет мир"
print(tokenize(t))
'''

