"""
Задание 3: Нормализация предложения.

Условие:
Введите предложение с ошибками в регистре и лишними пробелами. Сделайте первую букву
прописной, остальные — строчными, удалите лишние пробелы и добавьте точку в конце, если её нет.

Пример:
Ввод: пРИВЕТ, МИР
Вывод: Привет, мир.
"""

import sys


def setup_console_encoding() -> None:
    """Настройка UTF-8 для корректного вывода в терминале Windows."""
    if sys.stdout.encoding.lower() != "utf-8":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except AttributeError:
            pass


def normalize_sentence(text: str) -> str:
    """
    Нормализует предложение:
    - Удаляет лишние пробелы между словами и по краям;
    - Делает первую букву прописной, остальные строчными;
    - Добавляет точку в конец предложения, если её нет.
    """
    words = text.split()
    if not words:
        return ""

    # Склеиваем слова с одиночными пробелами
    cleaned = " ".join(words)

    # Приводим к нижнему регистру, а затем делаем первую букву заглавной
    normalized = cleaned.lower().capitalize()

    # Проверяем наличие точки в конце
    if not normalized.endswith("."):
        normalized += "."

    return normalized


def main() -> None:
    """Точка входа: интерактивный ввод данных."""
    setup_console_encoding()
    print("=== Задание 3: Нормализация предложения ===")
    user_input = input("Введите предложение: ")

    if not user_input.strip():
        print("Введена пустая строка. Используется тестовый пример:")
        user_input = "пРИВЕТ, МИР"
        print(f"Пример: {user_input}")

    normalized = normalize_sentence(user_input)
    print("Вывод:")
    print(normalized)


if __name__ == "__main__":
    main()
