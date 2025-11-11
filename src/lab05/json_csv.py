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
    json_file = Path(json_path)
    if not json_file.exists():
        raise FileNotFoundError(f"JSON файл не найден: {json_path}")
    # чтение JSON
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Некорректный JSON формат: {e}")

    # валидация данных
    if not data:
        raise ValueError("Пустой JSON или неподдерживаемая структура")
    if not isinstance(data, list):
        raise ValueError("JSON должен содержать список объектов")
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Все элементы JSON должны быть словарями")

    # получение заголовков из первого элемента
    if not data[0]:
        raise ValueError("Первый элемент не может быть пустым словарем")

    fieldnames = list(data[0].keys()) #метод словаря, который возвращает объект представления (view object), содержащий все ключи словаря

    # запись CSV
    try:
        with open(csv_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            #позволяет записывать словари в CSV-файл. Он создает объект, который сопоставляет ключи словаря с выходными строками, где f — это объект файла, а fieldnames — список ключей, определяющих порядок столбцов.
            writer.writeheader()
            writer.writerows(data)
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
            reader = csv.DictReader(f)
            # проверка заголовков
            if not reader.fieldnames:
                raise ValueError("CSV файл не содержит заголовков")
            for row in reader:
                # преобразование пустых строк в None и чисел в int/float
                processed_row = {}
                for key, value in row.items():
                    if value == '':
                        processed_row[key] = None
                    else:
                        # попытка преобразовать в число
                        try:
                            if '.' in value:
                                processed_row[key] = float(value)
                            else:
                                processed_row[key] = int(value)
                        except ValueError:
                            processed_row[key] = value

                data.append(processed_row)

    except Exception as e:
        raise ValueError(f"Ошибка чтения CSV: {e}")
    # валидация данных
    if not data:
        raise ValueError("CSV файл пустой или содержит только заголовок")
    # запись JSON
    try:
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        raise ValueError(f"Ошибка записи JSON: {e}")


json_to_csv("data/samples/people.json", "data/out/people_from_json.csv")
csv_to_json("data/samples/people1.csv", "data/out/people_from_csv.json")