def game():
    import random

    sports = ["Футбол", "Баскетбол", "Волейбол", "Хоккей", "Теннис", "Гольф", "Бокс", "Бег", "Плавание", "Лыжи", "Сноуборд", "Гимнастика", "Йога", "Бодибилдинг", "Атлетика", "Единоборства", "Кроссфит", "Паркур", "Велоспорт", "Скалолазание"]
    education = ["Школа", "Университет", "Колледж", "Институт", "Академия", "Курс", "Лекция", "Семинар", "Диплом", "Бакалавр", "Магистр", "Доктор", "Преподаватель", "Студент", "Учебник", "Экзамен", "Зачет", "Исследование"]
    nature = ["Лес", "Река", "Озеро", "Горы", "Пустыня", "Поляна", "Холмы", "Каньон", "Болото", "Парк", "Заповедник", "Джунгли", "Саванна", "Океан", "Море", "Рифы", "Водопад", "Грот", "Пещера"]
    art = ["Живопись", "Скульптура", "Графика", "Архитектура", "Фотография", "Иллюстрация", "Кино", "Музыка", "Театр", "Литература", "Танец", "Дизайн", "Мода", "Ювелирное искусство"]
    programming = ['переменная', 'цикл', 'условие', 'функция', 'класс', 'объект', 'метод', 'модуль', 'библиотека', 'алгоритм', 'структура данных', 'интерфейс', 'разработчик', 'кодирование', 'отладка', 'тестирование']
    rest = ['пляж', 'море', 'солнце', 'отпуск', 'гамак', 'бассейн', 'шезлонг', 'отель', 'туризм', 'релакс', 'спа', 'велосипед', 'горы', 'природа', 'пикник', 'барбекю', 'кемпинг', 'рыбалка']
    human = ['человек', 'люди', 'женщина', 'мужчина', 'дети', 'семья', 'родители', 'бабушка', 'дедушка', 'друзья', 'коллеги', 'соседи', 'знакомые', 'партнеры', 'враги', 'конкуренты', 'незнакомцы']


    def match_ru(word):
        letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        cnt = 0
        for i in word:
            if i.lower() in letters:
                cnt += 1
        if cnt == len(word):
            return True
        return False
    def get_word(word_list_):
        return random.choice(word_list_).upper()


    # функция получения текущего состояния
    def display_hangman(tries):
        stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
            '''
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |     / \\
                       -
                    ''',
            # голова, торс, обе руки, одна нога
            '''
                      --------
                       |      |
                       |      O
                       |     \|/
                       |      |
                       |     / 
                       -
                    ''',
            # голова, торс, обе руки
            '''
                       --------
                       |      |
                       |      O
                       |     \|/
                       |      |
                       |      
                       -
                    ''',
            # голова, торс и одна рука
            '''
                       --------
                       |      |
                       |      O
                       |     \|
                       |      |
                       |     
                       -
                    ''',
            # голова и торс
            '''
                       --------
                       |      |
                       |      O
                       |      |
                       |      |
                       |     
                       -
                    ''',
            # голова
            '''
                       --------
                       |      |
                       |      O
                       |    
                       |      
                       |     
                       -
                    ''',
            # начальное состояние
            '''
                       --------
                       |      |
                       |      
                       |    
                       |      
                       |     
                       -
                    '''
        ]
        return stages[tries]

    def start():
        topic = random.randint(0,6)
        if topic == 0:
            play(get_word(sports), topic, sports)
        elif topic == 1:
            play(get_word(education), topic, education)
        elif topic == 2:
            play(get_word(nature), topic, nature)
        elif topic == 3:
            play(get_word(art), topic, art)
        elif topic == 4:
            play(get_word(programming), topic, programming)
        elif topic == 5:
            play(get_word(rest), topic, rest)
        else:
            play(get_word(human), topic, human)


    def play(word, topic,word_list):
        word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
        guessed = False
        hints = False
        guessed_letters = []  # список уже названных букв
        guessed_words = []  # список уже названных слов
        tries = 6  # количество попыток
        print('Давайте играть в угадайку слов!')
        print(display_hangman(tries))
        print(f'Количество попыток: {tries}')
        print(word_completion)
        if len(word) > 6:
            while True:
                restart = input('Хотите подсказки? (Введите "да" или "нет"): ').strip().lower()
                if restart == 'да':
                    if topic == 0:
                        print('Значение данного слова связано со спортом')
                    elif topic == 1:
                        print('Значение данного слова связано с образованием')
                    elif topic == 2:
                        print('Значение данного слова связано с природой')
                    elif topic == 3:
                        print('Значение данного слова связано с искусством')
                    elif topic == 4:
                        print('Значение данного слова связано с программированием')
                    elif topic == 5:
                        print('Значение данного слова связано с отдыхом')
                    else:
                        print('Значение данного слова связано с человеком')
                    while True:
                        restart = input(
                            'Хотите, чтобы вам показали первую и последнюю буквы в слове? (Введите "да" или "нет"): ').strip().lower()
                        if restart == 'да':
                            word_completion = word[0].upper() + '_' * (len(word) - 2) + word[-1].upper()
                            print(word_completion)
                            break
                        elif restart == 'нет':
                            break
                        else:
                            print('Я не понимаю. Введите "да" или "нет"')
                            continue
                    hints = True
                    break
                elif restart == 'нет':
                    hints = True
                    break
                else:
                    print('Я не понимаю. Введите "да" или "нет"')
                    continue
        while tries:
            if not hints:
                while True:
                    restart = input('Хотите подсказку? (Введите "да" или "нет"): ').strip().lower()
                    if restart == 'да':
                        if topic == 0:
                            print('Значение данного слова связано со спортом')
                        elif topic == 1:
                            print('Значение данного слова связано с образованием')
                        elif topic == 2:
                            print('Значение данного слова связано с природой')
                        elif topic == 3:
                            print('Значение данного слова связано с искусством')
                        elif topic == 4:
                            print('Значение данного слова связано с программированием')
                        elif topic == 5:
                            print('Значение данного слова связано с отдыхом')
                        else:
                            print('Значение данного слова связано с человеком')
                        hints = True
                        break
                    elif restart == 'нет':
                        hints = True
                        break
                    else:
                        print('Я не понимаю. Введите "да" или "нет"')
                        continue
            while True:
                letter_word = input('Введите букву или слово целиком: ').upper().strip()
                if not letter_word.isalpha():
                    print('Я не понимаю')
                    continue
                elif 1 < len(letter_word) != len(word):
                    print(f'Данное слово имеет {len(word)} букв!')
                elif letter_word.count(word_completion) == letter_word.count(word) and letter_word.upper().count(word) > 1:
                    print(word_completion, word)
                    print(letter_word.upper().count(word_completion), letter_word.upper().count(word))
                    print('Данная буква уже есть в слове нужное количество раз')
                    continue
                elif letter_word in guessed_letters and letter_word in word:
                    print('Данная буква уже есть в слове')
                    continue
                elif letter_word in guessed_letters and not letter_word in word:
                    print('Вы уже вводили данную букву, её нет в слове')
                    continue
                elif not match_ru(letter_word):
                    print('Слово на русском языке! ')
                    continue
                else:
                    break
            if len(letter_word) == 1:
                guessed_letters.append(letter_word)
                if letter_word in word:
                    print('Отличная работа, буква', letter_word, 'присутствует в слове!')
                    word1 = word
                    while letter_word in word1:
                        word_completion = word_completion[:word1.index(letter_word)] + letter_word + \
                                          word_completion[word1.index(letter_word) + 1:]
                        word1 = word1[:word1.index(letter_word)] + '0' + word1[word1.index(letter_word) + 1:]
                    if '_' not in word_completion:
                        guessed = True
                        print(word_completion)
                        break
                else:
                    print('Буквы', letter_word, 'нет в слове.')
                    tries -= 1
                    print(display_hangman(tries))
            else:
                if letter_word != word:
                    print('Вы не угадали слово.')
                    tries -= 1
                    print(display_hangman(tries))
                else:
                    guessed = True
                    print(word.upper())
                    break
            print(word_completion)

        if word in word_list:
            word_list.pop(word_list.index(word))
        if word_completion == word:
            guessed = True
        if not guessed:
            print('Вы не угадали слово. Загаданным словом было ' + word + '. В следующий раз у вас обязательно всё '
                                                                          'получится!')
            continue_game()
        else:
            print('Поздравляем, вы угадали слово! Вы победили!')
            continue_game()

    def continue_game():
        while True:
            restart = input('Сыграете ещё? (Введите "да" или "нет"): ').strip()
            if restart.lower() == 'да':
               start()
            elif restart.lower() == 'нет':
                print("                 *******   **     **    ********")
                print("                *******     **   **    ********")
                print("               **   **       ** **    ***       ")
                print("              ******          ***    ********")
                print("             ******           **    ********")
                print("            **   **          **    ***     ")
                print("           ********         **    ********")
                print("          ********         **    ********")
                break
            else:
                print('Я не понимаю. Введите "да" или "нет"')
                continue

    start()


game()
