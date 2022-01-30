menu = """
1 - Добавить запись
2 - Удалить запись
3 - Поиск
4 - Сортировка
5 - Выход
"""


class Notebook:
    def menu(self):
        print(f"\n Записная книжка\n Меню:{menu}")
        while True:
            try:
                choice = int(input("Введите номер пункта меню"))
                if choice == 1:
                    self.add()
                elif choice == 2:
                    self.delete()
                elif choice == 3:
                    self.search()
                elif choice == 4:
                    self.sort()
                elif choice == 5:
                    self.exit()
                else:
                    print("Такого пункта в меню нет")
                    continue
                break
            except ValueError:
                print("Вы ввели не правильно")
                continue

    @staticmethod
    def _list(list_notes):
        # преобразуем в список со списками
        list_lst_notes = []
        for i in list_notes:
            list_lst_notes.append(i.split(','))
        # убираем лишнии символы
        signs = ["'", '{', '}', ':', ',', '\n']
        for i in range(len(list_lst_notes)):
            for j in range(len(list_lst_notes[i])):
                for e in range(len(list_lst_notes[i][j])):
                    for s in range(len(signs)):
                        if list_lst_notes[i][j][e] == signs[s]:
                            list_lst_notes[i][j] = list_lst_notes[i][
                                j].replace(signs[s], ' ')
        # создаем список со списками из списков
        for i in range(len(list_lst_notes)):
            for j in range(len(list_lst_notes[i])):
                list_lst_notes[i][j] = list_lst_notes[i][j].split()
        # преобразуем элементы(списки со списками) списка в словари
        # получаем список из словарей
        list_dict_notes = []
        for i in range(len(list_lst_notes)):
            note_dict = {list_lst_notes[i][j][0]: list_lst_notes[i][j][-1]
                         for j in range(len(list_lst_notes[i]))}
            list_dict_notes.append(note_dict)
        return list_dict_notes

    def add(self):
        print("Добавляем запись\nПоля помеченные * обязательны к заполнению")
        while True:
            name = input("*Введите Имя: ")
            if name == "":
                print("Это поле не может быть пустым")
                continue
            else:
                break

        while True:
            surname = input("*Введите Фамилию: ")
            if surname == "":
                print("Это поле не может быть пустым")
                continue
            else:
                break

        while True:
            number = input("*Введите Номер Телефона: ")
            if number == "":
                print("Это поле не может быть пустым")
                continue
            else:
                break

        address = input("Введите Адрес: ")
        if address == "":
            address = "None"

        birthday = input("Введите Дату Рождения: ")
        if birthday == "":
            birthday = "None"

        my_noted = {
            "Имя": name,
            "Фамилия": surname,
            "Номер телефона": number,
            "Адрес": address,
            "Дата Рождения": birthday}

        with open("notebook.txt", 'a', encoding='utf-8') as f:
            f.write(f"{str(my_noted)}\n")
        print("Запись сохранена")
        self.menu()

    def delete(self):
        while True:
            with open("notebook.txt", 'r+', encoding='utf-8') as f:
                file_notes = f.read()
            if file_notes == "":
                print("Нет записей")
            else:
                with open("notebook.txt", 'r', encoding='utf-8') as f:
                    print("Записи:")
                    count = 0
                    notes_lst = []
                    for line in f:
                        print(f"{count}:\n{line}")
                        notes_lst.append(line)
                        count += 1

                while True:
                    try:
                        num_del = input("Введите номер для удаления")
                        num_del = int(num_del)
                        notes_lst.remove(notes_lst[num_del])

                        with open("notebook.txt", 'w', encoding='utf-8') as f:
                            for i in notes_lst:
                                f.write(i)
                        print("Запись удалена")
                        break
                    except (ValueError, IndexError):
                        print("Такого номера записи нет")
                        break
            self.menu()

    def search(self):
        while True:
            choice = """
1. Поиск по имени
2. Поиск по телефону
            """
            print(choice)
            with open("notebook.txt", 'r+', encoding="utf-8") as f:
                list_n = self._list(f.readlines())
            while True:
                try:
                    num = int(input("Введите число: "))
                    if num == 1:
                        print("Поиск по имени")
                        name = input("Введите имя: ")
                        list_f = []
                        for i in range(len(list_n)):
                            if name == list_n[i]["Имя"]:
                                list_f.append(list_n[i])
                        if len(list_f) > 0:
                            print("записи: ")
                            for i in list_f:
                                print(i)
                        else:
                            print("Ничего не найдено")
                        break
                    elif num == 2:
                        print("Поиск по номеру телефона")
                        number = input("Введите номер ""телефона: ")
                        list_f = []
                        for i in range(len(list_n)):
                            if number == list_n[i]["Номер телефона"]:
                                list_f.append(list_n[i])
                        if len(list_f) > 0:
                            print("Записи: ")
                            for i in list_f:
                                print(i)
                        else:
                            print("Ничего не найдено")
                        break
                    else:
                        print("Такого поиска нет")
                        continue
                except ValueError:
                    print("Вы ввели не число")
                    continue
            self.menu()

    def sort(self):
        while True:
            choice = """
1 - Сортировка по имени
2 - Сортировка по фамилии
            """
            print(choice)
            with open("notebook.txt", 'r+', encoding="utf-8") as f:
                list_of_dict_notes = self._list(f.readlines())
            with open("notebook.txt", 'r', encoding='utf-8') as f:
                if f.read() == '':
                    print("Нет записей")
                else:
                    while True:
                        try:
                            sort_by = int(input("Введите число:"))
                            if sort_by == 1:
                                sorted_list_of_dict = sorted(
                                    list_of_dict_notes, key=lambda k: k['Имя'])
                                with open('notebook.txt', 'w',
                                          encoding='utf-8')\
                                        as f1:
                                    for i in sorted_list_of_dict:
                                        f1.write(f'{str(i)}\n')
                                    print("Отсортировано по имени")
                                    break
                            elif sort_by == 2:
                                sorted_list_of_dict = sorted(list_of_dict_notes,
                                                             key=lambda k:
                                                             k['Фамилия'])
                                with open('notebook.txt', 'w',
                                          encoding='utf-8')\
                                        as f2:
                                    for i in sorted_list_of_dict:
                                        f2.write(f'{str(i)}\n')
                                    print("Отсортировано по фамилии")
                                    break
                            else:
                                print("Такой сортировки нет")
                                continue

                        except ValueError:
                            print("Вы ввели не число ")
                            continue
            break
        self.menu()

    @staticmethod
    def exit():
        print("Выход из книжки")
        exit()


my_notebook = Notebook()
my_notebook.menu()
