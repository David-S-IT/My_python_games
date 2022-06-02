# Внимание!!! Загрузите библиотеку pyttsx3 !!!
# Внимание!!! Загрузите библиотеку pyttsx3 !!!
# Внимание!!! Загрузите библиотеку pyttsx3 !!!
# Внимание!!! Загрузите библиотеку pyttsx3 !!!
# Внимание!!! Загрузите библиотеку pyttsx3 !!!


import time, random, pyttsx3
engine = pyttsx3.init()
key = random.randint(1000, 9999)
mech = False
tip_mecha = "Никакой"
poptka = 3
engine = pyttsx3.init()

def speak(what):
    print(what)
    speak_engine.say( what )
    speak_engine.runAndWait()
    speak_engine.stop()
speak_engine = pyttsx3.init()


def neo_print(value, base_delay=0.04):
    for char in value:
        print(char, end='', flush=True)
        time.sleep(base_delay + random.randint(1, 100) * base_delay / 100)
    print()


def poptka_print(eulav, base_delay=0.04):
    global poptka
    if poptka == 2:
        engine.say('У вас есть ещё - две {}'.format(eulav))
        print('У вас есть ещё - 2 {}'.format(eulav))
        engine.runAndWait()
        poptka = 2
    elif poptka == 1:
        poptka = "одна"
        engine.say('У вас есть ещё - одна {}'.format(eulav))
        print('У вас есть ещё - 1 {}'.format(eulav))
        engine.runAndWait()
        poptka = 1

    else:
        speak('У вас есть ещё - {} {}'.format(poptka, eulav))
    # value = 'У вас есть ещё - '
    # for char in value, poptka, ' ':
    #     print(char, end='', flush=True)
    #     time.sleep(base_delay + random.randint(1, 100) * base_delay / 100)
    # value = eulav
    # for char in value:
    #     print(char, end='', flush=True)
    #     time.sleep(base_delay + random.randint(1, 100) * base_delay / 100)


def poptka_end():
    speak('Вы истратили все свои попытки(')
    time.sleep(1)
    speak('Вы вышли в комнату с испытаниями.')
    print()
    isputanya()


def key_password():
    global key
    speak('Вы встретили панель на которой нужно набрать код от кодового замка, введите его или выйдите обратно в коридор.')
    print()
    ch = input('''Введите пароль - <Предпологаемый пароль>
Выйдите из комнаты - 1
''')
    ch = int(ch)
    if ch == 1:
        living_room()
    elif key == ch:
        speak('Поздравляю вы ввели правильный пароль! Теперь вы получили мешок с 1 000 000 000 $ !')
        time.sleep(1)
        speak('И вы были отправлены домой с 1 000 000 000 $ !!!')
        time.sleep(1)
        print()
        speak('''Игра окончена, спасибо за игру!''')
        input()
    else:
        speak('К сожалению вы ввели неправильный пароль.')
        print()
        key_password()


def living_room():
    print()
    speak('Ваша задача - это найти ключ от двери, в которой лежат подарки.')
    print()
    speak('Вы можете взять подсказку, попробовать подобрать пароль или проходить испытания, чтобы получать различные бонусы!')
    ch = input('''Подобрать пароль - 1
Пройти испытания - 2
Взять подсказку - 3
''')
    if ch == '1':
        key_password()
    elif ch == '2':
        isputanya()
    elif ch == '3':
        podskazka()
    else:
        speak('Введите, пожалуйста, цифру ещё раз.')
        print()
        living_room()


def podskazka():
    neo_print('В одной из комнат', 0.09)
    time.sleep(1)
    neo_print('у одного существа', 0.09)
    time.sleep(2)
    neo_print('есть ключ к двери!', 0.02)
    time.sleep(1)
    speak("Нажмите Enter")
    input()
    living_room()


def isputanya():
    speak("Выберите комнату в которую пойдёте:")
    ch = input('''1
2
3
Выйти в коридор - 4
''')
    if ch == '4':
        living_room()
    elif ch == '1':
        is1()
    elif ch == '2':
        is2()
    elif ch == '3':
        is3()
    else:
        speak('Введите, пожалуйста, цифру ещё раз.')
        print()


def is1():
    global mech, key, tip_mecha
    speak("В этой комнате оказался монстр - Минотавр.")
    time.sleep(1)
    if mech == True:
        speak("У вас есть {} меч".format(tip_mecha))
        time.sleep(2)
        speak('Вы начали бой!')
        time.sleep(3)

        if tip_mecha == "деревянный":
            speak("К сожалению вы проиграли Минотавру, потому что у деревянного меча маленький урон и он быстро ломается.")
            mech = False
            tip_mecha = "Никакой"
        elif tip_mecha == "железный":
            speak('''К сожалению вы проиграли Минотавру, потому что железный меч у вас сломался раньше времени.
(Руками вы его не смогли отлупасить) )''')
            mech = False
            tip_mecha = "Никакой"
        elif tip_mecha == "алмазный":
            speak("И вы смогли одолеть Минотавра!")
            time.sleep(1)
            speak("С него выпала какая-то бирка, на которой написано {}.".format(key))
            speak("Что бы эти 4 цифры могли значить?")
    else:
        speak("Но к сожалению у вас нету меча, чтобы его победить.")
        time.sleep(1)
    input("Нажмите Enter, чтобы выйти в комнату с испытаниями")
    print()
    isputanya()


def is2():
    global mech, tip_mecha
    speak('''Вы заходите во вторую комнату и видите 3 сундука, и надпись:
В каждом сундуке есть какой-то меч (деревянный, железный или алмазный) или вообще ничего нет)
Выберите сундук, введите его номер - 1, 2 или 3
Выйти в комнату с испытаниями - 4''')
    ch = input()
    if ch == '4':
        isputanya()

    elif ch == '1':
        m = random.randint(0, 3)
        if m == 1:
            mech = True
            speak('В этом сундуке был деревянный меч!')
            if tip_mecha == 'Никакой':
                tip_mecha = "деревянный"

            else:
                dsaf = 'dsaf'

        elif m == 2:
            mech = True
            speak('В этом сундуке был железный меч!')
            if tip_mecha == 'Никакой' or tip_mecha == 'деревянный':
                tip_mecha = "железный"
            else:
                dsaf = 'dsaf'

        elif m == 3:
            mech = True
            speak('В этом сундуке был алмазный меч!')
            tip_mecha = "алмазный"
        else:
            speak('Тут ничего нет)')
        speak('Вы вышли в комнату с испытаниями')
        isputanya()
    elif ch == '2':
        m = random.randint(0, 3)
        if m == 1:
            mech = True
            speak('В этом сундуке был деревянный меч!')
            if tip_mecha == 'Никакой':
                tip_mecha = "деревянный"

            else:
                dsaf = 'dsaf'

        elif m == 2:
            mech = True
            speak('В этом сундуке был железный меч!')
            if tip_mecha == 'Никакой' or tip_mecha == 'деревянный':
                tip_mecha = "железный"
            else:
                dsaf = 'dsaf'

        elif m == 3:
            mech = True
            speak('В этом сундуке был алмазный меч!')
            tip_mecha = "алмазный"
        else:
            speak('Тут ничего нет)')
        speak('Вы вышли в комнату с испытаниями')
        isputanya()
    elif ch == '3':
        m = random.randint(0, 3)
        if m == 1:
            mech = True
            speak('В этом сундуке был деревянный меч!')
            if tip_mecha == 'Никакой':
                tip_mecha = "деревянный"

            else:
                dsaf = 'dsaf'

        elif m == 2:
            mech = True
            speak('В этом сундуке был железный меч!')
            if tip_mecha == 'Никакой' or tip_mecha == 'деревянный':
                tip_mecha = "железный"
            else:
                dsaf = 'dsaf'

        elif m == 3:
            mech = True
            speak('В этом сундуке был алмазный меч!')
            tip_mecha = "алмазный"
        else:
            speak('Тут ничего нет)')
        speak('Вы вышли в комнату с испытаниями')
        isputanya()


    else:
        speak('Введите, пожалуйста, цифру ещё раз.')
        print()
        is2()


def is3():
    global poptka, mech, tip_mecha
    if poptka > 0:
        speak('Какой операционной системой пользуются хакеры?')
        speak('Введи цифру правильного ответа')
        if poptka == 1:
            poptka_print('попытка')
        else:
            poptka_print('попытки')
        print()
        ch = input('''Windows - 1
MacOS - 2
linux - 3
''')
        if ch == "3":
            is3_2()


        else:
            speak("Неправильно!")
            poptka -= 1
            if poptka == 0:
                poptka_end()
            elif poptka == 1:
                poptka_print('попытка')
            else:
                poptka_print('попытки')
            print()
            is3()

    else:
        poptka_end()


def is3_2():
    global poptka, mech, tip_mecha
    speak('Правильно! Но какой linux? Ubuntu или Kali?')
    ch = input('''Linux ubuntu - 1
Kali linux - 2
''')

    if ch == '2':
        speak("Правильно! Хакеры используют Kali linux!")
        speak('Вы получаете алмазный меч!')
        mech = True
        tip_mecha = "алмазный"
        speak("Вы вышли в комнату с испытаниями")
        isputanya()
    else:
        speak("Неправильно!")
        poptka -= 1
        if poptka == 0:
            poptka_end()
        elif poptka == 1:
            poptka_print('попытка')
        else:
            poptka_print('попытки')
        print()
        is3_2()


def start():
    ch = input('''Уйти не проходя испытаний - 1
Пройти все испытания - 2
''')
    if ch == '1':
        speak("Вы оказались у себя дома.")
        input()
    elif ch == '2':
        speak("Вы сделали правильный выбор!")
        living_room()
    else:
        speak("Введите пожалуйста цифру ещё раз.")
        print()
        start()
speak("Вы оказались у деда мороза в доме, и он предлагает вам пройти его испытания, и если вы их проходите, то он отпускает вас с подарками.")
speak("Но так же он сказал, что вы можете уйти не проходя никаких испытаний, но тогда подарков он вам не даст.")
start()

# Внимание!!! Загрузите библиотеку pyttsx3 !!!
# Внимание!!! Загрузите библиотеку pyttsx3 !!!
# Внимание!!! Загрузите библиотеку pyttsx3 !!!
# Внимание!!! Загрузите библиотеку pyttsx3 !!!
# Внимание!!! Загрузите библиотеку pyttsx3 !!!