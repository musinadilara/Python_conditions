year = int(input('Введите год(целое неотрицательное число), который хотите перевести: '))

match year % 12:
    case 0:
        jap_year = 'обезьяны'
    case 1:
        jap_year = 'петуха'
    case 2:
        jap_year = 'собаки'
    case 3:
        jap_year = 'свиньи'
    case 4:
        jap_year = 'крысы'
    case 5:
        jap_year = 'коровы'
    case 6:
        jap_year = 'тигра'
    case 7:
        jap_year = 'зайца'
    case 8:
        jap_year = 'дракона'
    case 9:
        jap_year = 'змеи'
    case 10:
        jap_year = 'лошади'
    case 11:
        jap_year = 'овцы'
print('В старояпонском календаре этот год является годом', jap_year+'.')

