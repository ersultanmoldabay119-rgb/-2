"""
Главное меню практической работы: 'Задания по строкам в Python'.
Позволяет запускать любое из 12 заданий интерактивно или запустить полный набор тестов.
"""

import sys
import task_01
import task_02
import task_03
import task_04
import task_05
import task_06
import task_07
import task_08
import task_09
import task_10
import task_11
import task_12
import test_all


def setup_console_encoding() -> None:
    """Настройка UTF-8 для корректного вывода в терминале Windows."""
    if sys.stdout.encoding.lower() != "utf-8":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except AttributeError:
            pass


TASKS = {
    "1": ("Подсчёт частоты слов", task_01.main),
    "2": ("Самый частый символ", task_02.main),
    "3": ("Нормализация предложения", task_03.main),
    "4": ("Удаление соседних повторов", task_04.main),
    "5": ("Проверка адреса электронной почты", task_05.main),
    "6": ("Шифр Цезаря", task_06.main),
    "7": ("Сумма чисел в тексте", task_07.main),
    "8": ("Чередование регистра", task_08.main),
    "9": ("Проверка анаграмм", task_09.main),
    "10": ("Форматирование номера телефона", task_10.main),
    "11": ("Общий префикс слов", task_11.main),
    "12": ("Статистика текста", task_12.main),
}


def print_menu() -> None:
    print("\n" + "=" * 55)
    print("      ПРАКТИЧЕСКАЯ РАБОТА: ЗАДАНИЯ ПО СТРОКАМ")
    print("=" * 55)
    for key, (title, _) in TASKS.items():
        print(f" [{key:>2}] {title}")
    print("-" * 55)
    print(" [ T] Запустить полное тестирование (все тесты)")
    print(" [ 0] Выход")
    print("=" * 55)


def main() -> None:
    setup_console_encoding()
    while True:
        print_menu()
        choice = input("Выберите номер задания: ").strip().lower()

        if choice == "0":
            print("\nВыход из программы. До свидания!")
            break

        if choice in ("t", "т"):
            print()
            test_all.run_all_tests()
            input("\nНажмите Enter, чтобы вернуться в меню...")
            continue

        if choice in TASKS:
            title, task_func = TASKS[choice]
            print(f"\n--- Запуск: {title} ---\n")
            try:
                task_func()
            except Exception as error:
                print(f"Ошибка при выполнении: {error}")
            input("\nНажмите Enter, чтобы вернуться в меню...")
        else:
            print("Неверный ввод. Пожалуйста, введите число от 1 до 12, 'T' или '0'.")


if __name__ == "__main__":
    main()
