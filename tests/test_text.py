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
