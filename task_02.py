"""
Задание 2: Самый частый символ.

Условие:
Введите строку и найдите символ, который встречается чаще всего. Пробелы не учитывайте.
Если лидеров несколько, выведите тот, который встретился раньше.

Пример:
Ввод: программирование
Вывод: р — 3
"""

import sys


def setup_console_encoding() -> None:
    """Настройка UTF-8 для корректного вывода в терминале Windows."""
    if sys.stdout.encoding.lower() != "utf-8":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except AttributeError:
            pass


def find_most_frequent_char(text: str) -> tuple[str, int] | None:
    """
    Находит символ с наибольшей частотой появления, игнорируя пробелы.
    При равенстве частот возвращает тот символ, который встретился раньше.
    """
    counts: dict[str, int] = {}
    for char in text:
        if not char.isspace():
            counts[char] = counts.get(char, 0) + 1

    if not counts:
        return None

    # max() в Python при равенстве значений оставляет первый встретившийся ключ
    best_char = max(counts, key=lambda c: counts[c])
    return best_char, counts[best_char]


def format_most_frequent_char(result: tuple[str, int] | None) -> str:
    """Форматирует результат поиска частого символа."""
    if result is None:
        return "Символы (кроме пробелов) не найдены."
    char, count = result
    return f"{char} — {count}"


def main() -> None:
    """Точка входа: интерактивный ввод данных."""
    setup_console_encoding()
    print("=== Задание 2: Самый частый символ ===")
    user_input = input("Введите строку: ")

    if not user_input.strip():
        print("Введена пустая строка. Используется тестовый пример:")
        user_input = "программирование"
        print(f"Пример: {user_input}")

    result = find_most_frequent_char(user_input)
    print("Вывод:")
    print(format_most_frequent_char(result))


if __name__ == "__main__":
    main()
