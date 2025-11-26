import argparse
from pathlib import Path
from src.lib.text import tokenize, count_freq, top_n




def main():
    parser = argparse.ArgumentParser(description='CLI-утилиты лабораторной №6')
    '''Создает основной парсер аргументов с описанием'''
    subparsers = parser.add_subparsers(dest='command')
    '''Создает подкоманды - в дальнейшем cat и stats'''

    # Подкоманда cat - утилита для просмотра содержимого текстовых файлов в терминале.
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Путь к входному файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")
    '''action="store_true" - если флаг указан, значение становится True, иначе False'''

    # Подкоманда stats -  утилита для адализа текстовой статистики
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