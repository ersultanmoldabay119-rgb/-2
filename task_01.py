"""
Задание 1: Подсчёт частоты слов.

Условие:
Введите предложение. Определите, сколько раз встречается каждое слово.
Регистр букв и знаки препинания не учитывайте.
Выведите слова и количество их повторений.

Пример:
Ввод: Python удобен, Python понятен и python популярен.
Вывод: python — 3; удобен — 1; понятен — 1; и — 1; популярен — 1
"""

import sys


def setup_console_encoding() -> None:
    """Настройка UTF-8 для корректного вывода в терминале Windows."""
    if sys.stdout.encoding.lower() != "utf-8":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except AttributeError:
            pass


def count_word_frequencies(text: str) -> dict[str, int]:
    """
    Подсчитывает частоту слов в предложении.
    Игнорирует регистр букв и знаки препинания.
    Сохраняет порядок первого появления слов.
    """
    # Заменяем все не буквенно-цифровые символы на пробелы
    cleaned_chars = [char if char.isalnum() else " " for char in text.lower()]
    cleaned_text = "".join(cleaned_chars)
    words = cleaned_text.split()

    frequencies: dict[str, int] = {}
    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1

    return frequencies


def format_frequencies(frequencies: dict[str, int]) -> str:
    """Форматирует словарь частот в строку требуемого вида."""
    if not frequencies:
        return "Слова не найдены."
    return "; ".join(f"{word} — {count}" for word, count in frequencies.items())


def main() -> None:
    """Точка входа: интерактивный ввод данных."""
    setup_console_encoding()
    print("=== Задание 1: Подсчёт частоты слов ===")
    user_input = input("Введите предложение: ").strip()

    if not user_input:
        print("Введена пустая строка. Используется тестовый пример:")
        user_input = "Python удобен, Python понятен и python популярен."
        print(f"Пример: {user_input}")

    freq = count_word_frequencies(user_input)
    print("Вывод:")
    print(format_frequencies(freq))


if __name__ == "__main__":
    main()
