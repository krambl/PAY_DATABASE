databasa = [['ex_ample', [['example', 0], ['example', 0], ['example', 0], ['example', 0], ['example', 0]]],
                ['12_2019', [['gas', 0], ['energy', 0], ['hphone', 0], ['house_pay', 0], ['internet', 0]]],
                ['6_2019', [['gas', 0], ['energy', 0], ['hphone', 0], ['house_pay', 0], ['internet', 0]]],
                ['7_2019', [['gas', 0], ['energy', 0], ['hphone', 0], ['house_pay', 0], ['internet', 0]]]
                ]

def pokazi():
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

        print(' ' + str(dat_pokaz) + '  ' + pok(gaz_pokaz) + '  ' +  pok(en_pokaz) + '  ' + pok(
            ph_pokaz) + '  ' + pok(kv_pokaz) + '  ' + pok(in_pokaz))

pokazi()

