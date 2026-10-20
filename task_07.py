"""
Задание 7: Сумма чисел в тексте.

Условие:
Введите строку, содержащую слова и целые положительные числа. Найдите все
последовательности цифр и вычислите сумму найденных чисел.

Пример:
Ввод: В группе 18 студентов, из них 7 отличников
Вывод: 25
"""

import sys


def setup_console_encoding() -> None:
    """Настройка UTF-8 для корректного вывода в терминале Windows."""
    if sys.stdout.encoding.lower() != "utf-8":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except AttributeError:
            pass


def sum_numbers_in_text(text: str) -> int:
    """
    Находит все последовательности цифр в строке и вычисляет их сумму.
    Числа накапливаются посимвольно в буфере.
    """
    total_sum = 0
    current_digits = ""

    for char in text:
        if char.isdigit():
            current_digits += char
        else:
            if current_digits:
                total_sum += int(current_digits)
                current_digits = ""

    # Добавляем последнее число, если строка завершилась цифрой
    if current_digits:
        total_sum += int(current_digits)

    return total_sum


def main() -> None:
    """Точка входа: интерактивный ввод данных."""
    setup_console_encoding()
    print("=== Задание 7: Сумма чисел в тексте ===")
    user_input = input("Введите строку: ")

    if not user_input.strip():
        print("Введена пустая строка. Используется тестовый пример:")
        user_input = "В группе 18 студентов, из них 7 отличников"
        print(f"Пример: {user_input}")

    result = sum_numbers_in_text(user_input)
    print("Вывод:")
    print(result)


if __name__ == "__main__":
    main()
