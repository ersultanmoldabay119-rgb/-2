"""
Задание 6: Шифр Цезаря.

Условие:
Введите строку из латинских букв и целое число сдвига. Замените каждую букву буквой,
расположенной на указанное количество позиций дальше в алфавите. После Z переходите к A.
Сохраняйте регистр.

Пример:
Ввод: Python, сдвиг: 3
Вывод: Sbwkrq
"""

import sys


def setup_console_encoding() -> None:
    """Настройка UTF-8 для корректного вывода в терминале Windows."""
    if sys.stdout.encoding.lower() != "utf-8":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except AttributeError:
            pass


def caesar_cipher(text: str, shift: int) -> str:
    """
    Шифрует латинские буквы строки шифром Цезаря с циклическим переходом (A-Z, a-z).
    Сдвиг может быть любым целым числом (включая отрицательные числа).
    Сохраняет регистр букв и прочие символы без изменений.
    """
    shift = shift % 26
    result = []

    for char in text:
        if "a" <= char <= "z":
            base = ord("a")
            new_char = chr(base + (ord(char) - base + shift) % 26)
            result.append(new_char)
        elif "A" <= char <= "Z":
            base = ord("A")
            new_char = chr(base + (ord(char) - base + shift) % 26)
            result.append(new_char)
        else:
            result.append(char)

    return "".join(result)


def main() -> None:
    """Точка входа: интерактивный ввод данных."""
    setup_console_encoding()
    print("=== Задание 6: Шифр Цезаря ===")
    user_text = input("Введите строку (латиница): ")

    if not user_text:
        print("Введена пустая строка. Используется пример: 'Python', сдвиг 3")
        user_text = "Python"
        shift = 3
    else:
        shift_str = input("Введите целое число сдвига: ").strip()
        try:
            shift = int(shift_str) if shift_str else 3
        except ValueError:
            print("Некорректное число сдвига. Установлено значение по умолчанию: 3")
            shift = 3

    encrypted = caesar_cipher(user_text, shift)
    print("Вывод:")
    print(encrypted)


if __name__ == "__main__":
    main()
