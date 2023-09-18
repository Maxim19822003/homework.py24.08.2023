import os


def print_result(record):
    # last_name, first_name, phone_number, description = record
    print("Фамилия:", record["Фамилия"])
    print("Имя:", record["Имя"])
    print("Телефон:", record["Телефон"])
    print("Описание:", record["Описание"])
    print()


def read_txt(filename):
    if os.path.exists(filename):
        phone_book = []
        with open(filename, 'r', encoding='utf-8') as phb:
            for line in phb:
                parts = line.strip().split(',')
                if len(parts) == 4:
                    last_name, first_name, phone_number, description = parts
                    phone_book.append({
                        "Фамилия": last_name,
                        "Имя": first_name,
                        "Телефон": phone_number,
                        "Описание": description
                    })
                else:
                    print(f"Ошибка в формате строки: {line}")
        return phone_book
    else:
        print(f"Файл '{filename}' не найден.")
        return []


phone_book = read_txt(
    r'C:\Users\maxim\OneDrive\Рабочий стол\Семинары\Python\Classwork_PySeminar\task_04.09.2023.py\phon.txt')

# поиск по фамилии


def find_by_lastname(phone_book, last_name):
    found_records = []
    for record in phone_book:
        if record["Фамилия"] == last_name:
            found_records.append(record)
    return found_records

# изменение номера по фамилии


def change_number(phone_book, last_name, new_number):
    for record in phone_book:
        if record["Фамилия"] == last_name:
            record["Телефон"] = new_number
            return f"Номер телефона для {last_name} изменен на {new_number}."
    return f"Абонент с фамилией {last_name} не найден."

# удаление записей по фамилии


def delete_by_lastname(phone_book, last_name):
    deleted_records = []
    new_phone_book = []
    for record in phone_book:
        if record[0] == last_name:
            deleted_records.append(record)
        else:
            new_phone_book.append(record)
    if deleted_records:
        return f'Записи для абонента {last_name} удалены'
    else:
        return f'Абонент с фамилией {last_name} не найден.'

# поиск записей по номеру


def find_by_number(phone_book, phone_number):
    found_records = []
    for record in phone_book:
        if record[2] == phone_number:
            found_records.append(record)
    return found_records

# добавление новой записи


def add_user(phone_book, user_data):
    parts = user_data.split(',')
    if len(parts) == 4:
        last_name, first_name, phone_number, description = parts
        phone_book.append({
            "Фамилия": last_name,
            "Имя": first_name,
            "Телефон": phone_number,
            "Описание": description
        })
        write_txt(
            r'C:\Users\maxim\OneDrive\Рабочий стол\Семинары\Python\Classwork_PySeminar\task_04.09.2023.py\phon.txt', phone_book)
        return f"Абонент {last_name} добавлен в справочник."
    else:
        return "Ошибка в формате данных. Ожидалось 4 поля: Фамилия, Имя, Телефон, Описание."


def show_menu():
    print('1. Распечатать справочник',
          '2. Найти телефон по фамилии',
          '3. Изменить номер телефона',
          '4. Удалить запись',
          '5. Найти абонента по номеру телефона',
          '6. Добавить абонента в справочник',
          '7. Закончить работу', sep='\n')
    choice = int(input())
    return choice


def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt(
        r'C:\Users\maxim\OneDrive\Рабочий стол\Семинары\Python\Classwork_PySeminar\task_04.09.2023.py\phon.txt')
    while (choice != 7):
        if choice == 1:
            list(map(print_result, phone_book))
        elif choice == 2:
            last_name = input('lastname ')
            print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
            last_name = input('lastname ')
            new_number = input('new number ')
            print(change_number(phone_book, last_name, new_number))
        elif choice == 4:
            lastname = input('lastname ')
            print(delete_by_lastname(phone_book, lastname))
        elif choice == 5:
            number = input('number ')
            print(find_by_number(phone_book, number))
        elif choice == 6:
            user_data = input('new data ')
            result = add_user(phone_book, user_data)  # Присвоить результат
            print(result)  # Вывести сообщение о добавлении
            write_txt(
                r'C:\Users\maxim\OneDrive\Рабочий стол\Семинары\Python\Classwork_PySeminar\task_04.09.2023.py\phon.txt', phone_book)
        choice = show_menu()


def write_txt(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as phout:
        for record in phone_book:
            s = ','.join(record.values())
            phout.write(f'{s}\n')

work_with_phonebook()
