"""
Задание 5: Проверка адреса электронной почты.

Условие:
Введите адрес электронной почты. Считайте его корректным, если в нём один символ @,
до и после него есть текст, а часть после @ содержит точку не в начале и не в конце.

Пример:
Ввод: student@example.com
Вывод: Корректный адрес
"""

import sys


def setup_console_encoding() -> None:
    """Настройка UTF-8 для корректного вывода в терминале Windows."""
    if sys.stdout.encoding.lower() != "utf-8":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except AttributeError:
            pass


def is_valid_email(email: str) -> bool:
    """
    Проверяет корректность email по заданным правилам:
    1. Ровно один символ '@';
    2. До и после '@' есть непустой текст;
    3. Доменная часть содержит точку не в начале и не в конце.
    """
    email = email.strip()

    # Проверка 1: ровно один символ '@'
    if email.count("@") != 1:
        return False

    username, domain = email.split("@")

    # Проверка 2: непустое имя пользователя и домен
    if not username or not domain:
        return False

    # Проверка 3: точка в домене есть, но не первая и не последняя
    if "." not in domain:
        return False
    if domain.startswith(".") or domain.endswith("."):
        return False

    return True


def check_email_address(email: str) -> str:
    """Возвращает текстовый вердикт проверки."""
    if is_valid_email(email):
        return "Корректный адрес"
    return "Некорректный адрес"


def main() -> None:
    """Точка входа: интерактивный ввод данных."""
    setup_console_encoding()
    print("=== Задание 5: Проверка адреса электронной почты ===")
    user_input = input("Введите адрес электронной почты: ").strip()

    if not user_input:
        print("Введена пустая строка. Используется тестовый пример:")
        user_input = "student@example.com"
        print(f"Пример: {user_input}")

    verdict = check_email_address(user_input)
    print("Вывод:")
    print(verdict)


if __name__ == "__main__":
    main()
