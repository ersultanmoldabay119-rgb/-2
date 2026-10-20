"""
Задание 8: Чередование регистра.

Условие:
Введите строку. Измените регистр букв так, чтобы первая буква стала прописной,
вторая — строчной, третья — прописной и так далее.
Пробелы и знаки препинания не должны влиять на чередование.

Пример:
Ввод: python — это интересно!
Вывод: PyThOn — ЭтО иНтЕрЕсНо!
"""

import sys


def setup_console_encoding() -> None:
    """Настройка UTF-8 для корректного вывода в терминале Windows."""
    if sys.stdout.encoding.lower() != "utf-8":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except AttributeError:
            pass


def alternate_case(text: str) -> str:
    """
    Чередует регистр букв: 1-я прописная, 2-я строчная, 3-я прописная и т.д.
    Символы, не являющиеся буквами, сохраняются и не сбивают счётчик.
    """
    result = []
    letter_count = 0

    for char in text:
        if char.isalpha():
            if letter_count % 2 == 0:
                result.append(char.upper())
            else:
                result.append(char.lower())
            letter_count += 1
        else:
            result.append(char)

    return "".join(result)


def main() -> None:
    """Точка входа: интерактивный ввод данных."""
    setup_console_encoding()
    print("=== Задание 8: Чередование регистра ===")
    user_input = input("Введите строку: ")

    if not user_input.strip():
        print("Введена пустая строка. Используется тестовый пример:")
        user_input = "python — это интересно!"
        print(f"Пример: {user_input}")

    result = alternate_case(user_input)
    print("Вывод:")
    print(result)


if __name__ == "__main__":
    main()
