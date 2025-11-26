# ЛР6
### CLI_text

```python
import argparse
from pathlib import Path
from src.lib.text import tokenize, count_freq, top_n




def main(): #объявление главной функции программы
    parser = argparse.ArgumentParser(description='CLI-утилиты лабораторной №6') #создает основной парсер аргументов
    #парсер это программа или часть программы, которая анализирует и обрабатывает параметры (аргументы), передаваемые при запуске скрипта из командной строки
    subparsers = parser.add_subparsers(dest='command')#создает подкоманды - в дальнейшем cat и stats

    # Подкоманда cat - утилита для просмотра содержимого текстовых файлов в терминале.
    #/stats позволяет связать «селекторы» и «задачи» с нужной сущностью/блоком и одной из его статистики
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Путь к входному файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")
    '''action="store_true" - если флаг указан, значение становится True, иначе False'''

    #/stats позволяет связать «селекторы» и «задачи» с нужной сущностью/блоком и одной из его статистики
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)
    '''type=int - автоматически преобразует введенное значение в число, по дефолту
       выводит топ-5'''

    args = parser.parse_args()  # "Анализирует" значения на входе

    file = Path(args.input)

    if args.command == "cat":
        with open(file, 'r', encoding='utf-8') as f:
            count = 1
            for line in f:  # Построчное чтение файла
                line = line.rstrip("\n")  # Очищаем строку от символа переноса
                if args.n:  # Если указан флаг -n, то проводим нумерацию строк
                    print(f'{count}: {line}')
                    count += 1
                else:
                    print(line)

    elif args.command == 'stats':
        with open(file, 'r', encoding='utf-8') as f:
            file = [i for i in f] 
            tokens = tokenize(''.join(file))
            freq = count_freq(tokens)
            top = top_n(freq, n=args.top)
            '''Работаем с входными данными'''

            num = 1

            for word, count in top:
                print(f'{num}. {word} - {count}')
                num += 1


# Точка - запуск программы
if __name__ == "__main__":
    main()
```
![1](/images/lab06/01.png)
![2](/images/lab06/02.png)
![3](/images/lab06/03.png)
![4](/images/lab06/04.png)
![5](/images/lab06/05.png)
![6](/images/lab06/06.png)

### CLI_convert

```python
import argparse
import sys
from src.lab05.json_csv import json_to_csv
from src.lab05.json_csv import csv_to_json
from src.lab05.cvs_xlsx import csv_to_xlsx

def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="command")

    p1 = sub.add_parser("json2csv")
    p1.add_argument("--in", dest="input", required=True)
    p1.add_argument("--out", dest="output", required=True)

    p2 = sub.add_parser("csv2json")
    p2.add_argument("--in", dest="input", required=True)
    p2.add_argument("--out", dest="output", required=True)

    p3 = sub.add_parser("csv2xlsx")
    p3.add_argument("--in", dest="input", required=True)
    p3.add_argument("--out", dest="output", required=True)

    args = parser.parse_args() # "Анализирует" значения на входе

    if args.command == "json2csv":
        # Python -m src.lab06.cli_convert json2csv --in data/samples/people2.json --out data/out/people_from_json.csv
        json_to_csv(json_path=args.input, csv_path=args.output)

    if args.command == "csv2json":
        # Python -m src.lab06.cli_convert csv2json --in data/samples/people.csv --out data/out/people_from_csv.json
        csv_to_json(csv_path=args.input, json_path=args.output)

    if args.command == "csv2xlsx":
        # Python -m src.lab06.cli_convert csv2xlsx --in data/samples/cities1.csv --out data/out/cities.xlsx
        csv_to_xlsx(csv_path=args.input, xlsx_path=args.output)

if __name__ == "__main__":
    main()
```
![7](/images/lab06/07.png)
![8](/images/lab06/08.png)
![9](/images/lab06/09.png)
![10](/images/lab06/10.png)
![11](/images/lab06/11.png)
