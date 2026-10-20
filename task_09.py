"""
Задание 9: Проверка анаграмм.

Условие:
Введите две строки и определите, являются ли они анаграммами.
Не учитывайте пробелы, знаки препинания и регистр букв.

Пример:
Ввод: Апельсин; Спаниель
Вывод: Это анаграммы
"""

import sys


def setup_console_encoding() -> None:
    """Настройка UTF-8 для корректного вывода в терминале Windows."""
    if sys.stdout.encoding.lower() != "utf-8":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except AttributeError:
            pass


def are_anagrams(first_str: str, second_str: str) -> bool:
    """
    Проверяет, являются ли две строки анаграммами.
    Фильтрует только буквы, приводит их к нижнему регистру и сравнивает.
    """
    letters1 = sorted([char.lower() for char in first_str if char.isalpha()])
    letters2 = sorted([char.lower() for char in second_str if char.isalpha()])

    if not letters1 and not letters2:
        return False

    return letters1 == letters2


def check_anagram_strings(first_str: str, second_str: str) -> str:
    """Возвращает текстовый вердикт проверки на анаграмму."""
    if are_anagrams(first_str, second_str):
        return "Это анаграммы"
    return "Это не анаграммы"


def main() -> None:
    """Точка входа: интерактивный ввод данных."""
    setup_console_encoding()
    print("=== Задание 9: Проверка анаграмм ===")
    first_input = input("Введите первую строку (или обе через ';'): ").strip()

    if not first_input:
        print("Введена пустая строка. Используется тестовый пример:")
        first_input = "Апельсин"
        second_input = "Спаниель"
        print(f"Пример: {first_input}; {second_input}")
    elif ";" in first_input:
        parts = first_input.split(";", 1)
        first_input = parts[0].strip()
        second_input = parts[1].strip()
    else:
        second_input = input("Введите вторую строку: ").strip()

    verdict = check_anagram_strings(first_input, second_input)
    print("Вывод:")
    print(verdict)


if __name__ == "__main__":
    main()
