# ЛР5
### Задание А
```python
import json
import csv
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8.
    FileNotFoundError: Если JSON файл не существует
    ValueError: Если JSON пустой, не список или содержит не словари
    """
    # проверка существования файла
    json_file = Path(json_path) #создаем объект Path для работы с путями
    if not json_file.exists():
        raise FileNotFoundError(f"JSON файл не найден: {json_path}")
    # чтение JSON
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f) #загружает JSON из файлового объекта
    except json.JSONDecodeError as e: #исключение при синтаксических ошибках в JSON
        raise ValueError(f"Некорректный JSON формат: {e}")

    # валидация данных
    if not data:
        raise ValueError("Пустой JSON или неподдерживаемая структура")
    if not isinstance(data, list):
        raise ValueError("JSON должен содержать список объектов")
    if not all(isinstance(item, dict) for item in data): #проверяем что ВСЕ элементы словари
        raise ValueError("Все элементы JSON должны быть словарями")

    # получение заголовков из первого элемента
    if not data[0]:
        raise ValueError("Первый элемент не может быть пустым словарем")

    fieldnames = list(data[0].keys()) #метод словаря, который возвращает объект представления, содержащий все ключи словаря

    # запись CSV
    try:
        with open(csv_path, 'w', encoding='utf-8', newline='') as f: #newline='' предотвращает проблемы с переносами строк в Windows
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            #позволяет записывать словари в CSV-файл. Он создает объект, который сопоставляет ключи словаря с выходными строками, где f — это объект файла, а fieldnames — список ключей, определяющих порядок столбцов.
            writer.writeheader()
            writer.writerows(data) #записывает все данные сразу
    except Exception as e:
        raise ValueError(f"Ошибка записи CSV: {e}")


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    FileNotFoundError: Если CSV файл не существует
    ValueError: Если CSV пустой или без заголовка
    """
    # проверка существования файла
    csv_file = Path(csv_path)
    if not csv_file.exists():
        raise FileNotFoundError(f"CSV файл не найден: {csv_path}")
    data = []
    # чтение CSV
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f) #читает CSV как список словарей, где ключи - заголовки
            # проверка заголовков
            if not reader.fieldnames: #автоматически получает заголовки из первой строки
                raise ValueError("CSV файл не содержит заголовков")
            for row in reader:
                # преобразование пустых строк в None и чисел в int/float
                processed_row = {} #создаем новый словарь для обработанных данных
                for key, value in row.items():
                    if value == '': 
                        processed_row[key] = None #проверяем пустые строки, заменяем на None
                    else:
                        # попытка преобразовать в число
                        try:
                            if '.' in value: #проверяем есть ли десятичная точка
                                processed_row[key] = float(value)
                            else:
                                processed_row[key] = int(value)
                        except ValueError:
                            processed_row[key] = value #если преобразование не удалось, оставляем строкой

                data.append(processed_row)

    except Exception as e:
        raise ValueError(f"Ошибка чтения CSV: {e}")
    # валидация данных
    if not data:
        raise ValueError("CSV файл пустой или содержит только заголовок")
    # запись JSON
    try:
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2) #записывает Python объект в JSON файл
            #ensure_ascii=False разрешает русские символы (не экранирует как \u0430). indent=2 красивое форматирование с отступами
    except Exception as e:
        raise ValueError(f"Ошибка записи JSON: {e}")


json_to_csv("data/samples/people.json", "data/out/people_from_json.csv")
csv_to_json("data/samples/people1.csv", "data/out/people_from_csv.json")
```
## тест json_to_csv
![1](/images/lab05/ex01.png)
![2](/images/lab04/ex02.png)
## тест csv_to_json
![3](/images/lab05/ex03.png)
![4](/images/lab05/ex04.png)

### Задание B

```python
import csv
from pathlib import Path
from openpyxl import Workbook
from openpyxl.utils import get_column_letter


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    Использовать openpyxl ИЛИ xlsxwriter.
    Первая строка CSV — заголовок.
    Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
    FileNotFoundError: Если CSV файл не существует
    ValueError: Если CSV пустой или без заголовка
    """
    # проверка существования файла
    csv_file = Path(csv_path)
    if not csv_file.exists():
        raise FileNotFoundError(f"CSV файл не найден: {csv_path}")

    data = []

    # чтение CSV
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f) #читает CSV как список списков (в отличие от DictReader)
            for row in reader:
                data.append(row)
    except Exception as e:
        raise ValueError(f"Ошибка чтения CSV: {e}")

    # валидация данных
    if not data:
        raise ValueError("CSV файл пустой")

    if not data[0]:  # Проверка заголовка
        raise ValueError("CSV файл не содержит заголовка")

    # создание Excel книги
    wb = Workbook() #создает новую Excel книгу
    ws = wb.active #получает активный лист (по умолчанию создается один)
    ws.title = "Sheet1" #переименовывает лист

    # запись данных
    for row in data:
        ws.append(row) #добавляет целую строку в Excel. Автоматически определяет типы данных (строки, числа, даты)

    # настройка авто-ширины колонок
    for col_num, column_cells in enumerate(ws.columns, 1): #перебираем колонки с номерами начиная с 1
        #ws.columns - генератор всех колонок листа
        max_length = 0
        column_letter = get_column_letter(col_num) #преобразует номер в букву (1→A, 2→B, 27→AA)

        for cell in column_cells:
            try:
                if len(str(cell.value)) > max_length: #cell.value получаем значение ячейки
                    max_length = len(str(cell.value))
            except:
                pass

        # минимальная ширина 10, максимальная 50
        adjusted_width = min(max_length + 2, 50) # добавляем запас в 2 символа и ограничиваем максимальную ширину 50
        adjusted_width = max(adjusted_width, 10) #ограничиваем максимальную ширину 50

        ws.column_dimensions[column_letter].width = adjusted_width #устанавливаем вычисленную ширину

    # сохранение файла
    try:
        wb.save(xlsx_path)
        #wb.save() - записывает книгу в файл. Автоматически определяет формат по расширению (.xlsx)
    except Exception as e:
        raise ValueError(f"Ошибка сохранения XLSX: {e}")


csv_to_xlsx("data/samples/people1.csv","data/out/people.xlsx")
```
## тест 
![5](/images/lab05/ex05.png)
![6](/images/lab05/ex06.png)