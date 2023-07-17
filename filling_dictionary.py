def filling(person):
    with open('D:\GB\Разработчик-тестирование\Знакомство с Python\Python_008_HW\example_new.txt', 'a', encoding='utf-8') as file:
        for el in person:
            file.write(el + '\n')
        file.write('\n')

