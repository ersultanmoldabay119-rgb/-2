"""
Задание 4: Удаление соседних повторов.

Условие:
Введите предложение, в котором некоторые слова могут повторяться подряд. Удалите
соседние повторы без учёта регистра, сохранив первое написание слова.

Пример:
Ввод: Мы мы изучаем Python python каждый день
Вывод: Мы изучаем Python каждый день
"""

import sys


def setup_console_encoding() -> None:
    """Настройка UTF-8 для корректного вывода в терминале Windows."""
    if sys.stdout.encoding.lower() != "utf-8":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except AttributeError:
            pass


def remove_adjacent_duplicates(text: str) -> str:
    """
    Удаляет подряд идущие одинаковые слова без учёта регистра.
    Сохраняет исходное написание (регистр) первого вхождения.
    """
    words = text.split()
    result: list[str] = []

    for word in words:
        # Если список пуст или текущее слово отличается от предыдущего без учета регистра
        if not result or word.lower() != result[-1].lower():
            result.append(word)

    return " ".join(result)


def main() -> None:
    """Точка входа: интерактивный ввод данных."""
    setup_console_encoding()
    print("=== Задание 4: Удаление соседних повторов ===")
    user_input = input("Введите предложение: ")

    if not user_input.strip():
        print("Введена пустая строка. Используется тестовый пример:")
        user_input = "Мы мы изучаем Python python каждый день"
        print(f"Пример: {user_input}")

    cleaned = remove_adjacent_duplicates(user_input)
    print("Вывод:")
    print(cleaned)


if __name__ == "__main__":
    main()
