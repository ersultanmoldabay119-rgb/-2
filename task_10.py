"""
Задание 10: Форматирование номера телефона.

Условие:
Введите номер телефона в произвольном виде. Оставьте только цифры.
Если получено 11 цифр, выведите номер в формате +7 (XXX) XXX-XX-XX; начальную 8 замените на 7.

Пример:
Ввод: 8 701 234 56 78
Вывод: +7 (701) 234-56-78
"""

import sys


def setup_console_encoding() -> None:
    """Настройка UTF-8 для корректного вывода в терминале Windows."""
    if sys.stdout.encoding.lower() != "utf-8":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except AttributeError:
            pass


def format_phone_number(raw_phone: str) -> str:
    """
    Извлекает из строки цифры и форматирует 11-значный номер телефона.
    Заменяет начальную 8 на 7.
    Формат: +7 (XXX) XXX-XX-XX
    """
    digits = [char for char in raw_phone if char.isdigit()]

    if len(digits) != 11:
        return f"Ошибка: номер должен содержать ровно 11 цифр (получено {len(digits)})."

    # Замена первой 8 на 7
    if digits[0] == "8":
        digits[0] = "7"

    country_code = digits[0]
    operator_code = "".join(digits[1:4])
    part1 = "".join(digits[4:7])
    part2 = "".join(digits[7:9])
    part3 = "".join(digits[9:11])

    return f"+{country_code} ({operator_code}) {part1}-{part2}-{part3}"


def main() -> None:
    """Точка входа: интерактивный ввод данных."""
    setup_console_encoding()
    print("=== Задание 10: Форматирование номера телефона ===")
    user_input = input("Введите номер телефона: ")

    if not user_input.strip():
        print("Введена пустая строка. Используется тестовый пример:")
        user_input = "8 701 234 56 78"
        print(f"Пример: {user_input}")

    formatted = format_phone_number(user_input)
    print("Вывод:")
    print(formatted)


if __name__ == "__main__":
    main()
