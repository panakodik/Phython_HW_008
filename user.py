def choose_mode():
    mode = input('Выберите режим для работы со справочником: запись, поиск, изменение или удаление: ')
    if mode == 'запись':
        person = fill_person()
    elif mode == 'поиск':
        search_person()
    elif mode == 'изменение':
        change_person()
    elif mode == 'удаление':
        delete_person()
    else:
        print('Такого режима не существует!')
        choose_mode()
    return person, mode


def fill_person():
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    second_name = input('Введите отчество: ')
    phone = input('Введите телефон: ')
    return surname, name, second_name, phone


def change_person():
    name_to_change = input('Введите имя или фамилию человека, данные которого хотите изменить: ')
    with open('D:\GB\Разработчик-тестирование\Знакомство с Python\Python_008_HW\example_new.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    found = False
    with open('D:\GB\Разработчик-тестирование\Знакомство с Python\Python_008_HW\example_new.txt', 'w', encoding='utf-8') as file:
        for line in lines:
            if name_to_change in line:
                print('Найден человек:', line.strip())
                new_data = fill_person()
                file.write('\n'.join(new_data) + '\n')
                found = True
            else:
                file.write(line)

    if not found:
        print('Человек не найден в справочнике.')


def delete_person():
    name_to_delete = input('Введите имя или фамилию человека, которого хотите удалить: ')
    with open('D:\GB\Разработчик-тестирование\Знакомство с Python\Python_008_HW\example_new.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    found = False
    with open('D:\GB\Разработчик-тестирование\Знакомство с Python\Python_008_HW\example_new.txt', 'w', encoding='utf-8') as file:
        for line in lines:
            if name_to_delete in line:
                print('Удален человек:', line.strip())
                found = True
            else:
                file.write(line)

    if not found:
        print('Человек не найден в справочнике.')



def search_person():
    name_to_search = input('Введите имя или фамилию человека, которого хотите найти: ')
    with open('D:\GB\Разработчик-тестирование\Знакомство с Python\Python_008_HW\example_new.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    found = False
    for line in lines:
        if name_to_search in line:
            print('Найден человек:', line.strip())
            found = True

    if not found:
        print('Человек не найден в справочнике.')