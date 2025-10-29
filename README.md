# ЛР4
### Задание А
```python
import csv
from pathlib import Path
from typing import Iterable, Sequence

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    '''
    Открыть файл на чтение в указанной кодировке и вернуть содержимое как одну строку.
    Обрабатывать ошибки: если файл не найден — поднимать FileNotFoundError (пусть падает),
    если кодировка не подходит — поднимать UnicodeDecodeError (пусть падает).
    '''
    p = Path(path) #создает объект пути
    if not p.exists():  # явная проверка существования файла
        raise FileNotFoundError('нет файла')
    return p.read_text(encoding=encoding) #читает весь файл как строку в указанной кодировке


def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    '''
    Создать/перезаписать CSV с разделителем , .
    Если передан header, записать его первой строкой.
    Проверить, что каждая строка в rows имеет одинаковую длину (иначе ValueError).
    '''
    if not rows and header is None:           # проверка на пустые данные
        Path(path).write_text("", encoding="utf-8") # создаем пустой файл 
        return
    
    p = Path(path)
    rows = list(rows)
    with p.open("w", newline="", encoding="utf-8") as f: # открывем файл. 
        # Открытие файла - newline="" важен для корректных переносов строк в Windows
        w = csv.writer(f) # создаем CSV writer
        if header is not None: # записываем заголовок
            w.writerow(header) #записывает одну строку 
        if rows:
            for r in rows:
                if len(r) != len(rows[0]):
                    raise ValueError('строки не одинаковой длины')
        for r in rows: # построчно записываем данные
            w.writerow(r)


def ensure_parent_dir(path: str | Path) -> None:
    """
    Создает родительские директории, если их нет.
    Args:
        path: путь к файлу или директории
    """
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True) # создаем директории, 
    # parents=True создает все родительские директории, exist_ok=True игнорирует существующие
```
## тест1 
![1](/images/lab04/ex01.png)
![2](/images/lab04/ex01.2.png)

## тест2
![3](/images/lab04/ex02.png)
![4](/images/lab04/ex02.2.png)

## тест3
![5](/images/lab04/ex03.png)
![6](/images/lab04/ex03.2.png)
![7](/images/lab04/ex03.3.png)

## тест4
![8](/images/lab04/ex04.png)
![9](/images/lab04/ex04.2.png)

### Задание B
```python
import sys
from pathlib import Path
# Добавляем пути для импорта модулей

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.lab04.io_txt_csv import read_text, write_csv, ensure_parent_dir
from src.lib.text import normalize, tokenize, count_freq, top_n

def generate_report(input_file: Path, output_file: Path, encoding: str = "utf-8") -> dict:
    """
    Генерирует отчет по словам из входного файла.
    """
    # читаем и обрабатываем текст
    text = read_text(input_file, encoding=encoding)
    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)

    # считаем статистику
    frequencies = count_freq(tokens)
    sorted_words = top_n(frequencies, len(frequencies))  # все слова отсортированные

    # подготавливаем данные для CSV
    csv_rows = []
    for word, count in sorted_words: # формируем строки CSV
        csv_rows.append((word, count))

    # записываем CSV
    ensure_parent_dir(output_file) # создаем директории если нужно
    write_csv(csv_rows, output_file, header=("word", "count"))

    # возвращаем статистику для вывода в консоль
    return {
        'total_words': len(tokens),
        'unique_words': len(frequencies),
        'top_5': top_n(frequencies, 5)
    }

if __name__ == '__main__':
    # жестко заданные пути
    input_file = Path('data/lab04/input.txt')  # входной файл
    output_file = Path('data/lab04/report.csv')  # выходной файл
    encoding = 'utf-8'  # кодировка

    # проверка аргументов командной строки
    #sys.argv - это список (массив), который содержит все аргументы командной строки, переданные при запуске Python-скрипта.
    if len(sys.argv) > 1:
        input_file = Path(sys.argv[1])  # первый аргумент - входной файл
    if len(sys.argv) > 2:
        output_file = Path(sys.argv[2])  # второй аргумент - выходной файл
    if len(sys.argv) > 3:
        encoding = sys.argv[3]  # третий аргумент - кодировка

    try:
        # анализируем файл и получаем статистику
        stats = generate_report(input_file, output_file, encoding)

        # Выводим результаты в консоль
        print(f"Всего слов: {stats['total_words']}")
        print(f"Уникальных слов: {stats['unique_words']}")
        print("Топ-5:")
        for word, count in stats['top_5']:
            print(f"{word}:{count}")

        print(f"\nОтчет сохранен в: {output_file}")

    except FileNotFoundError:
        print(f"Ошибка: файл {input_file} не найден")
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"Ошибка: не удается прочитать файл {input_file} в кодировке {encoding}")
        sys.exit(1)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        sys.exit(1)
```

## Тест А 
![10](/images/lab04/exA1.png)
![11](/images/lab04/exA2.png)
![12](/images/lab04/exA3.png)

## Тест B
![13](/images/lab04/exB1.png)
![14](/images/lab04/exB2.png)
![15](/images/lab04/exB3.png)

## Тест C
![16](/images/lab04/exC1.png)
![17](/images/lab04/exC2.png)
![18](/images/lab04/exC3.png)