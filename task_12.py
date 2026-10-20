"""
Задание 12: Статистика текста.

Условие:
Введите строку и подсчитайте количество слов, букв, цифр и знаков препинания.
Пробелы не относите ни к одной категории.

Пример:
Ввод: Python 3 — отличный язык!
Вывод: Слов: 4; букв: 18; цифр: 1; знаков препинания: 2
"""

import string
import sys
import unicodedata


def setup_console_encoding() -> None:
    """Настройка UTF-8 для корректного вывода в терминале Windows."""
    if sys.stdout.encoding.lower() != "utf-8":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except AttributeError:
            pass


def is_punctuation(char: str) -> bool:
    """
    Проверяет, является ли символ знаком препинания (ASCII + Unicode знаки препинания).
    """
    extended_punctuation = set(string.punctuation + "—–«»…“”„")
    return char in extended_punctuation or unicodedata.category(char).startswith("P")


def analyze_text(text: str) -> dict[str, int]:
    """
    Вычисляет статистику строки:
    - количество слов (токены, содержащие буквы или цифры);
    - количество букв;
    - количество цифр;
    - количество знаков препинания.
    Пробелы не учитываются ни в одной из категорий.
    """
    letter_count = 0
    digit_count = 0
    punct_count = 0

    for char in text:
        if char.isalpha():
            letter_count += 1
        elif char.isdigit():
            digit_count += 1
        elif is_punctuation(char):
            punct_count += 1

    # Словом считается токен, разделенный пробелами, в котором есть хотя бы одна буква или цифра
    tokens = text.split()
    word_count = sum(1 for token in tokens if any(c.isalnum() for c in token))

    return {
        "words": word_count,
        "letters": letter_count,
        "digits": digit_count,
        "punct": punct_count,
    }


def format_statistics(stats: dict[str, int]) -> str:
    """Форматирует статистику в требуемую условием строку."""
    return (
        f"Слов: {stats['words']}; букв: {stats['letters']}; "
        f"цифр: {stats['digits']}; знаков препинания: {stats['punct']}"
    )


def main() -> None:
    """Точка входа: интерактивный ввод данных."""
    setup_console_encoding()
    print("=== Задание 12: Статистика текста ===")
    user_input = input("Введите строку: ")

    if not user_input.strip():
        print("Введена пустая строка. Используется тестовый пример:")
        user_input = "Python 3 — отличный язык!"
        print(f"Пример: {user_input}")

    stats = analyze_text(user_input)
    print("Вывод:")
    print(format_statistics(stats))


if __name__ == "__main__":
    main()
