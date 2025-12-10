import csv
from pathlib import Path
from typing import Iterable, Sequence


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Открыть файл на чтение в указанной кодировке и вернуть содержимое как одну строку.
    Обрабатывать ошибки: если файл не найден — поднимать FileNotFoundError (пусть падает),
    если кодировка не подходит — поднимать UnicodeDecodeError (пусть падает).
    """
    p = Path(path)
    if not p.exists():  # Явная проверка существования файла
        raise FileNotFoundError("нет файла")
    return p.read_text(encoding=encoding)


def write_csv(
    rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None
) -> None:
    """
    Создать/перезаписать CSV с разделителем , .
    Если передан header, записать его первой строкой.
    Проверить, что каждая строка в rows имеет одинаковую длину (иначе ValueError).
    """
    p = Path(path)
    rows = list(rows)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        if rows:
            for r in rows:
                if len(r) != len(rows[0]):
                    raise ValueError("строки не одинаковой длины")
        for r in rows:
            w.writerow(r)


def ensure_parent_dir(path: str | Path) -> None:
    """
    Создает родительские директории, если их нет.
    Args:
        path: путь к файлу или директории
    """
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
