"""
Задание 11: Общий префикс слов.

Условие:
Введите несколько слов через пробел. Найдите самую длинную общую начальную часть всех слов.
Если общей части нет, выведите сообщение 'Нет общего префикса'.

Пример:
Ввод: программа программист программирование
Вывод: программ
"""

import sys


def setup_console_encoding() -> None:
    """Настройка UTF-8 для корректного вывода в терминале Windows."""
    if sys.stdout.encoding.lower() != "utf-8":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except AttributeError:
            pass


def find_longest_common_prefix(words: list[str]) -> str:
    """
    Находит самый длинный общий префикс списка слов методом постепенного сокращения.
    Если общей части нет, возвращает 'Нет общего префикса'.
    """
    if not words:
        return "Нет общего префикса"

    prefix = words[0]

    for word in words[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return "Нет общего префикса"

    return prefix if prefix else "Нет общего префикса"


def main() -> None:
    """Точка входа: интерактивный ввод данных."""
    setup_console_encoding()
    print("=== Задание 11: Общий префикс слов ===")
    user_input = input("Введите слова через пробел: ").strip()

    if not user_input:
        print("Введена пустая строка. Используется тестовый пример:")
        user_input = "программа программист программирование"
        print(f"Пример: {user_input}")

    words = user_input.split()
    common_prefix = find_longest_common_prefix(words)
    print("Вывод:")
    print(common_prefix)


if __name__ == "__main__":
    main()
