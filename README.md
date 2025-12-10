# ЛР7
### Задание A: test_text

```python
import pytest
import sys
from src.lib.text import normalize, tokenize, count_freq, top_n

""" Проводим параметризацию, далее - для каждого теста. """


@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлкa", "ежик, елкa"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
        ("", ""),
    ],
)
def test_normalize_basic(source, expected):
    assert normalize(source) == expected


@pytest.mark.parametrize(
    "source, expected",
    [
        ("привет, мир!", ["привет", "мир"]),
        ("по-настоящему круто", ["по-настоящему", "круто"]),  # работа с дефисом
        ("2025 год", ["2025", "год"]),  # чтение
        ("emoji 😀 не слово", ["emoji", "не", "слово"]),  # удаление эмоджи
        ("    мноооооого ненужного!!", ["мноооооого", "ненужного"]),
        ("", []),  # пустой -> пустой
    ],
)
def test_tokenize_basic(source, expected):
    assert tokenize(source) == expected


@pytest.mark.parametrize(
    "tokens, expected",
    [
        (["a", "b", "a", "c", "b", "a"], {"a": 3, "b": 2, "c": 1}),
        ([], {}),  # пустой -> пустой
        (["test", "test", "test"], {"test": 3}),  # одинаковые слова
        (["🌍", "🚀", "🌍"], {"🌍": 2, "🚀": 1}),  # обработка эмодзи
    ],
)
def test_count_freq_and_top_n(tokens, expected):
    assert count_freq(tokens) == expected


@pytest.mark.parametrize(
    "words, n, expected",
    [
        (
            {"b": 5, "a": 5, "c": 3, "d": 2},
            2,
            [("a", 5), ("b", 5)],
        ),  # равные значения -> по алфавиту
        ({"x": 10}, 5, [("x", 10)]),  # n > dicts
        ({}, 3, []),  # пустой -> пустой
        ({"a": 1, "b": 1}, 0, []),  # n = 0
    ],
)
def test_top_n_tie_breaker(words, n, expected):
    assert top_n(words, n) == expected
```
![1](/images/lab07/01.png)

### Задание B: json2csv и csv2json

```python
import pytest
from pathlib import Path
import sys
import json, csv

sys.path.append("C:/Users/user/Desktop/python_labs/")
from src.lab05.json_csv import json_to_csv, csv_to_json


"""
С помощью фикстуры tmp_path создаём временные файлы для чтения и записы данных.
1 тест - проверка правильности записи базового случая
"""


def test_json_to_csv_roundtrip(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    json_to_csv(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2
    assert {"name", "age"} <= set(rows[0].keys())


"""Пустой файл"""


def test_json_to_csv_empty_file(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = []
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    with pytest.raises(ValueError, match="Пустой файл"):
        json_to_csv(str(src), str(dst))


"""Несуществующий путь"""


def test_json_to_csv_empty_file(tmp_path: Path):
    src = tmp_path / "nothing.json"
    dst = tmp_path / "people.csv"

    with pytest.raises(FileNotFoundError, match="Путь не найден"):
        json_to_csv(str(src), str(dst))


"""1 проверка формата"""


def test_json_to_csv_not_list(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = {"name": "Alice", "age": 22}

    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    with pytest.raises(ValueError, match="Файл не JSON формата: не список словарей"):
        json_to_csv(str(src), str(dst))


"""2 проверка формата"""


def test_json_to_csv_not_dict(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = ['name": "Alice", "age": 22', 'name": "Bob", "age": 25']

    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    with pytest.raises(ValueError, match="Файл не JSON формата: в списке не словари"):
        json_to_csv(str(src), str(dst))


"""Аналогично для обратного перевода"""


def test_csv_to_json_roundtrip(tmp_path: Path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"

    csv_data = """name,age,city,email
Анна Иванова,28,Москва,anna@example.com
Петр Сидоров,35,Санкт-Петербург,petr@example.com"""

    src.write_text(csv_data, encoding="utf-8")

    csv_to_json(str(src), str(dst))

    with dst.open("r", encoding="utf-8") as f:
        data = json.load(f)

    # Проверка
    assert isinstance(data, list)
    assert len(data) == 2
    assert isinstance(data[0], dict)
    assert isinstance(data[1], dict)


# Бро вот еще тесты и тд

"""Пустой файл"""


def test_csv_to_json_empty_file(tmp_path: Path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"

    csv_data = ""

    src.write_text(csv_data, encoding="utf-8")

    with pytest.raises(ValueError, match="Пустой файл"):
        csv_to_json(str(src), str(dst))


"""Несуществующий файл"""


def test_csv_to_json_empty_file(tmp_path: Path):
    src = tmp_path / "nothing.csv"
    dst = tmp_path / "people.json"

    with pytest.raises(FileNotFoundError, match="Файл не найден"):
        csv_to_json(str(src), str(dst))


"""Не тот формат файла"""


def test_csv_to_json_type(tmp_path: Path):
    src = tmp_path / "input.txt"
    dst = tmp_path / "people.json"

    txt_data = """name,age,city,email
Анна Иванова,28,Москва,anna@example.com
Петр Сидоров,35,Санкт-Петербург,petr@example.com"""

    src.write_text(txt_data, encoding="utf-8")

    with pytest.raises(ValueError, match="Неверный тип файла"):
        csv_to_json(str(src), str(dst))

```
![2](/images/lab07/02.png)

### Задание С: black
![3](/images/lab07/03.png)
#### Все файлы приведены к читаемому виду


# ЛР8
## Тестовые данные
### список
```
[
    Student("Иванов Иван Иванович", "2007-01-15", "БИВТ-25-1", 4.5),
    Student("Петрова Анна Сергеевна", "2007-03-22", "БИВТ-25-2", 4.8),
    Student("Сидоров Алексей Петрович", "2007-05-10", "БИВТ-25-3", 3.9),
    Student("Козлова Мария Владимировна", "2007-07-28", "БИВТ-25-4", 4.2)
]
```
### файл students_input.json
```
[
  {
    "Студент": "Иванов Иван Иванович",
    "Группа": "БИВТ-25-1",
    "Дата рождения": "2007-01-15",
    "Средний балл": 4.5
  },
  {
    "Студент": "Петрова Анна Сергеевна",
    "Группа": "БИВТ-25-2",
    "Дата рождения": "2007-03-22",
    "Средний балл": 4.8
  },
  {
    "Студент": "Сидоров Алексей Петрович",
    "Группа": "БИВТ-25-3",
    "Дата рождения": "2007-05-10",
    "Средний балл": 3.9
  },
  {
    "Студент": "Козлова Мария Владимировна",
    "Группа": "БИВТ-25-4",
    "Дата рождения": "2007-07-28",
    "Средний балл": 4.2
  }
]
```

## Задание A
```python
from dataclasses import dataclass
from datetime import datetime, date


@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        # Валидация формата даты
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Неверная запись времени")

        # Валидация диапазона GPA
        if not (0 <= self.gpa <= 5):
            raise ValueError("GPA должен находиться между 0 и 5")

    def age(self) -> int:
        """Возвращает количество полных лет"""
        birth_day = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        if birth_day > today:
            raise ValueError("Студент еще не родился")
        if today.month < birth_day.month or (
            today.month == birth_day.month and today.day < birth_day.day
        ):
            return today.year - birth_day.year - 1
        return today.year - birth_day.year

    def to_dict(self) -> dict:
        return {
            "Студент": self.fio,
            "Группа": self.group,
            "Дата рождения": self.birthdate,
            "Средний балл": self.gpa,
        }

    @classmethod # Метод создаёт новый объект из существующих данных
    def from_dict(cls, d: dict):
        # Создание объекта класса Student из словаря
        return cls(
            fio=d['Студент'], group=d["Группа"], birthdate=d["Дата рождения"], gpa=d["Средний балл"]
        )

    def __str__(self):
        return (f"Студент: {self.fio};\n"
                f"Группа: {self.group};\n"
                f"Дата рождения: {self.birthdate};\n"
                f"Средний балл: {self.gpa}.")
```

### запуск 
```python
if __name__ == "__main__":
    student = Student("Иванов Иван Иванович", "2007-01-15", "БИВТ-25-1", 4.5)
    print(student)
    print( "=" * 140)

    # age
    print(f"Возраст: {student.age()}")
    
    # to_dict
    student_dict = student.to_dict()
    print(f"Сериализованный: {student_dict}")
    
    # from_dict
    restored_student = Student.from_dict(student_dict)
    print(f"Десериализованный: {restored_student}")
```
![4](/images/lab08/01.png)

## Задание B
```python
import json
from pathlib import Path
from models import Student


def students_to_json(students: list[Student], path: str):
    data = [s.to_dict() for s in students]
    path = Path(path)
    with open(path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)


def students_from_json(path: str):
    path = Path(path)
    with open(path, "r", encoding="utf-8") as json_file:
        try:
            students = json.load(json_file)
        except (
            json.JSONDecodeError
        ):  # Выходит, когда файл невозможно загрузить в формате JSON
            raise ValueError("Пустой JSON или неподдерживаемая структура")

    if not students:  # Явная проверка существования данных
        raise ValueError("Пустой файл")

    if not isinstance(students, list):
        raise ValueError("Файл не JSON формата: не список словарей")

    if not all(isinstance(row, dict) for row in students):
        raise ValueError("Файл не JSON формата: в списке не словари")

    stud_list = []

    for data in students:
        student = Student.from_dict(data)
        stud_list.append(student)
    return stud_list
```

### тест 
```
stud = [
    Student("Иванов Иван Иванович", "2007-01-15", "БИВТ-25-1", 4.5),
    Student("Петрова Анна Сергеевна", "2007-03-22", "БИВТ-25-2", 4.8),
    Student("Сидоров Алексей Петрович", "2007-05-10", "БИВТ-25-3", 3.9),
    Student("Козлова Мария Владимировна", "2007-07-28", "БИВТ-25-4", 4.2),
]


students_to_json(stud, "data/out/students_output.json")
print(students_from_json("data/samples/students_input.json"))
```
![5](/images/lab08/02.png)