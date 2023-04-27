import text_fields as txt

def main_menu() -> int:
    print(""""Главное меню:
    1. Открыть файл
    2. Сохранить файл
    3. Показать все контакты
    4. Создать контакт
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход""")
    while True:
        choice = input("Выбери пункт меню: ")
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)
        else:
            print("Введите число от 1 до 8")

def print_info(message: str):
    print("\n" + "-"*len(message))
    print(message)
    print("-"*len(message) + "\n")

def show_contacts(book: list[dict], message: str):
    if book:
        print("\n" + "-" * 63)
        for n, contact in enumerate(book, 1):
            print(f"{n:>3}. {contact.get('name'):<20}"
                  f"{contact.get('phone'):<20}"
                  f"{contact.get('comment'):<20}")
        print("-" * 63 + "\n")
    else:
        print(message)


def new_contact() -> dict:
    print()
    name = input(txt.new_name)
    phone = input(txt.new_phone)
    comment = input(txt.new_comment)
    print()
    return {"name": name, "phone": phone, "comment": comment}


def confirm(message: str) -> bool:
    print()
    answer = input(message + " y/n -> ")
    if answer.lower() == "y":
        return True
    else:
        return False
