
from user import choose_mode, change_person, delete_person, search_person
from filling_dictionary import filling


def running():
    person, mode = choose_mode()
    if mode == 'запись':
        filling(person)
    elif mode == 'поиск':
        search_person()
    elif mode == 'изменение':
        change_person()
    elif mode == 'удаление':
        delete_person()
    else:
        pass