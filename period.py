import json

# Загружает в программу базу
with open('db/text.json', 'r') as texta:
    databasa = json.load(texta)

# Сохраняет данные в базе
def keep():
    with open('db/text.json', 'w') as text:
        close = json.dump(databasa, text)

# Приветствие при открытии программы
def hello_hello():
    print('                  = ДОБРО ПОЖАЛОВАТЬ! =                        ')
    print('Информационный терминал на основе функционального программирования PYTHON')
    print('--------------------------------------------------------------------------')

# Сообщение для выбора операции
def please_choise():
    print('Для осуществления операции выберите ее номер')
    print('1 - внести новую запись')
    print('2 - откорректировать запись')
    print('3 - удалить запись')
    print('4 - получить отчет')
    print('0 - для выхода и закрытия приложения')

# Сообщение для выбора услуги
def please_choise_servis():
    print('Введите 1 - газоснабжение')
    print('Введите 2 - электроэнергия')
    print('Введите 3 - домашний телефон')
    print('Введите 4 - коммунальные услуги')
    print('Введите 5 - интернет')

# Сообщение об отсутствии информации в базе
def no_info():
    print('В базе нет информации по данному периоду')

# Очистка консоли
def clean_console():
    print('\n'*40)

# Назначение постоянных значений для услуг
gas = 1
energy = 2
hphone = 3
house_pay = 4
internet = 5


hello_hello()
please_choise()
choice = int(input('Сделайте свой выбор: '))

while choice != 0:
    closse = 1

    # Вносит новую запись 'период' в базу, значения услуг = 0
    def into(mounth, year):
        cascad = [['gas', 0], ['energy', 0], ['hphone', 0], ['house_pay', 0], ['internet', 0]]
        data = str(str(mounth) + '_' + str(year))
        maskad = [data, cascad]
        for i in range(len(databasa)):
            if databasa[i][0] == data:
                break
        if databasa[i][0] == data:
            print('По данному периоду уже существует запись')
            print('Вы можете откорректировать ее или удалить')
        else:
            databasa.append(maskad)
            keep()

    # Изменяет значения услуги 'газ'
    def gas_korrect(data, new_info):
        for i in range(len(databasa)):
            if databasa[i][0] == data:
                databasa[i][1][0][1] = new_info
                break
        if databasa[i][0] != data:
            no_info()

    # Изменяет значения услуги 'энергия'
    def energy_korrect(data, new_info):
        for i in range(len(databasa)):
            if databasa[i][0] == data:
                databasa[i][1][1][1] = new_info
                break
        if databasa[i][0] != data:
            no_info()

    # Изменяет значения услуги 'домашний телефон'
    def hphone_korrect(data, new_info):
        for i in range(len(databasa)):
            if databasa[i][0] == data:
                databasa[i][1][2][1] = new_info
                break
        if databasa[i][0] != data:
            no_info()

    # Изменяет значения услуги 'коммунальные услуги'
    def house_pay_korrect(data, new_info):
        for i in range(len(databasa)):
            if databasa[i][0] == data:
                databasa[i][1][3][1] = new_info
                break
        if databasa[i][0] != data:
            no_info()

    # Изменяет значения услуги 'интернет'
    def internet_korrect(data, new_info):
        for i in range(len(databasa)):
            if databasa[i][0] == data:
                databasa[i][1][4][1] = new_info
                break
        if databasa[i][0] != data:
            no_info()

    # Удаление всех данных за заданный период
    def delete_all(mounth, year):
        data = str(str(mounth) + '_' + str(year))
        for i in range(len(databasa)):
            if databasa[i][0] == data:
                betta = databasa[i]
                print(betta)
                del_el = databasa.remove(betta)
                break

    # Удаление данных за указанную услугу (услуга = 0)
    def delete(data,num):
        for i in range(len(databasa)):
            if databasa[i][0] == data:
                betta = databasa[i][1][num]
                print(betta)
                databasa[i][1][num][1] = 0
                keep()

    # Выводит все данные базы в удобном для чтения формате
    def pokaz():
        print(' ________________________________________________________________')
        print('  Период |  Газ-ние | Элек-гия | Дом.тел. | Ком.усл. |  Интернет')
        print(' ----------------------------------------------------------------')
        for i in range(len(databasa)):
            def pok(i_pokaz):
                i_pokaz = str(i_pokaz)
                if len(i_pokaz) == 1:
                    i_pokaz = i_pokaz + '       |'
                if len(i_pokaz) == 2:
                    i_pokaz = i_pokaz + '      |'
                if len(i_pokaz) == 3:
                    i_pokaz = i_pokaz + '     |'
                if len(i_pokaz) == 4:
                    i_pokaz = i_pokaz + '    |'
                if len(i_pokaz) == 5:
                    i_pokaz = i_pokaz + '   |'
                return i_pokaz

            pokaz = databasa[i]

            dat_pokaz = pokaz[0]
            if len(dat_pokaz) == 6:
                dat_pokaz = dat_pokaz + '  |'
            if len(dat_pokaz) == 7:
                dat_pokaz = dat_pokaz + ' |'

            gaz_pokaz = str(pokaz[1][0][1])
            en_pokaz = pokaz[1][1][1]
            ph_pokaz = pokaz[1][2][1]
            kv_pokaz = pokaz[1][3][1]
            in_pokaz = pokaz[1][4][1]

            print(' ' + str(dat_pokaz) + '  ' + pok(gaz_pokaz) + '  ' + pok(en_pokaz) + '  ' + pok(
                ph_pokaz) + '  ' + pok(kv_pokaz) + '  ' + pok(in_pokaz))

    if choice == 1:
        while 1 == 1:
            if closse == 0:
                break
            clean_console()
            print('Введите данные даты')
            m_ounth = int(input('Месяц: '))
            if m_ounth >=1 and m_ounth <= 12 :
                y_ear = int(input('Год: '))
                if y_ear >=1900 and y_ear <=2100:
                    into(m_ounth, y_ear)
                    print('Запись за период' + ' ' + str(m_ounth) + ' ' + str(y_ear) + ' ' + 'успешно добавлена')
                    break
                else:print('Вы ввели недопустимый диапазон ( допустимый 1900 - 2100)')
            else:print('Вы ввели недопустимый формат ( допустимый: 1 - 12)')
            closse = input('Нажмите любую квлавишу, чтобы повторить или 0 для выхода')



    if choice == 2:
        clean_console()
        print('Выберете период за который необходимо произвести корректировку')
        m_ounth = int(input('Введите месяц: '))
        y_ear = int(input('Введите год: '))
        da_ta = str(m_ounth) + '_' + str(y_ear)
        print(da_ta)

        def ret():
            for i in range(len(databasa)):
                if databasa[i][0] == da_ta:
                    print(databasa[i][0])
                    break
            return i

        if databasa[ret()][0] == da_ta:
            print('Какие данные следует откореектировать?')
            please_choise_servis()
            name_korrekt = str(input('Следайте свой выбор: '))
            if name_korrekt == '1':
                new_zn = str(input('Введите новое значение: '))
                gas_korrect(da_ta, new_zn)
            if name_korrekt == '2':
                new_zn = str(input('Введите новое значение: '))
                energy_korrect(da_ta, new_zn)
            if name_korrekt == '3':
                new_zn = str(input('Введите новое значение: '))
                hphone_korrect(da_ta, new_zn)
            if name_korrekt == '4':
                new_zn = str(input('Введите новое значение: '))
                house_pay_korrect(da_ta, new_zn)
            if name_korrekt == '5':
                new_zn = str(input('Введите новое значение: '))
                internet_korrect(da_ta, new_zn)
        else:
            print('По данному периоду нет данных')
            print('Хотите ли создать запись о данном периоде?')
            vb = str(input('Введте 1 если да, любой символ если нет'))
            if vb == '1':
                into(m_ounth, y_ear)

    if choice == 3:
        clean_console()
        print('Выберете период за который необходимо произвести корректировку')
        m_ounth = str(int(input('Введите месяц: ')))
        y_ear = str(int(input('Введите год: ')))
        data = str(m_ounth) + '_' + str(y_ear)


        def psk():
            for i in range(len(databasa)):
                if databasa[i][0] == data:
                    return i


        if psk() != None:
            if databasa[psk()][0] == data:
                print('Если хотите удалить информацию за период выберете 1')
                print('Если хотите удалить информацию за конкретную услугу выберете 2')
                vib = int(input('Сделайте свой выбор'))
                if vib == 1:
                    delete_all(m_ounth, y_ear)
                if vib == 2:
                    print('Какие данные следует удалить?')
                    please_choise_servis()
                    name_delete = int(input('Пожалуйста сделайте ваш выбор'))
                    if name_delete == 1:
                        delete(data,0)
                    if name_delete == 2:
                        delete(data, 1)
                    if name_delete == 3:
                        delete(data, 2)
                    if name_delete == 4:
                        delete(data, 3)
                    if name_delete == 5:
                        delete(data, 4)

        else:
            print('Записи по данной дате нет')


    if choice == 4:
        clean_console()
        pokaz()


    input('Для продолжения нажмите любую клавишу')
    clean_console()
    please_choise()
    choice = int(input('Сделайте свой выбор: '))



