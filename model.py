phone_book = []
start_phone_book = []
PATH = "phone_book.txt"


def get_pb():
    global phone_book
    return phone_book


def load_file():
    global phone_book, start_phone_book
    with open(PATH, "r", encoding="UTF-8") as file:
        data = file.readlines()
    for contact in data:
        contact = contact.strip().split(":")
        phone_book.append({"name": contact[0], "phone": contact[1], "comment": contact[2]})
    start_phone_book = phone_book.copy()




def save_file():
    global phone_book
    data = []
    for contact in phone_book:
        data.append(":".join([value for value in contact.values()]))
    data = "\n".join(data)
    with open(PATH, 'w', encoding="UTF-8") as file:
        file.write(data)

def add_contact(contact: dict):
    global phone_book
    phone_book.append(contact)


def exit_pb() -> bool:
    global phone_book, start_phone_book
    if phone_book == start_phone_book:
        return False
    else:
        return True
