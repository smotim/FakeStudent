# Вы можете расположить сценарий своей игры в этом файле.
# Определение персонажей игры.
define g = Character('Гусь', color="#c8fff8")
define s = Character('Староста', color="#c6fcc8")
define p = Character('Паша', color="#c7fbc8")
define i = Character('Игорь', color="#c8fff8")
image gus = im.Scale("gus.png", 480, 700)
define main = Character("[name]")
 
#image map = im.Scale("map.jpg")
#image map buttons = im.Scale("map_buttons.jpg")


# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.



# Игра начинается здесь:
label start:
    python:
        name=renpy.input("Пока мы не начали, не расскажете как вас зовут?\n(Имя по-умолчанию - Саад")
        name=name.strip() or "Саад"
    scene tegeran

    show gus

    g "Привет, [name]!"
    main "wtf"

    g "Ты запустил образовательную игру \"Fake Student\""

    show gus at left
    g "If you press the \'esc\' button, you can go to \'settings\' and change the interface language"
    g "Now you can choose the language of the story. "
    g "Russian characters who speak Russian will always speak Russian. Your choice will 
    change the language in which I speak and the main character thinks."

    menu:

        "Карта":
            jump imagemap_example

        "The main character will think in English":
            jump choice1_english

        "البطل المهم سوف يفكر باللغة العربية\n work in progress":
            jump choice1_arabic

    label imagemap_example:

    # Call the imagemap_example screen.
    call screen imagemap

    label choice1_russian:

        g "Хорошо. К сожалению русская версия находится в разработке. Несколько раз нажмите
         \"Назад\" внизу экрана и выберите английский язык, если хотите продолжить "

        jump choice1_done

    label choice1_english:

        g "Great!"

        jump choice1_done

    label choice1_arabic:

        g "Good. Unfortunately, the Arabic version is in development. Tap repeatedly
         \"Back\" at the bottom of the screen and select English if you want to continue"

        jump choice1_done

    label choice1_done:

        scene chudesnyi

        g "Нам пора изучить падежи! Хочешь ли ты перечитать \nтеорию или сразу приступить к примерам?"

        menu:

            "Можете, пожалуйста, напомнить мне теорию?":
                jump choice2_yes

            "Я помню теорию!":
                jump choice2_no

        label choice2_yes:

            $ menu_flag = True

            g "Не бойся, 2B нас спасёт."

            jump choice2_teoriya

        label choice2_no:

            $ menu_flag = False            

            g "Нам пора идти в вуз, у старосты есть какие-то новости."

            scene lekcionnaya

            jump choice2_praktik

        label choice2_teoriya:
        
            jump choice2_done

        label choice2_praktik:

            show pasha at right 

            p "Давай пойдём сегодня на АЛЯСКУ?"

            

            menu:

                "А что такое АЛЯСКА?":
                    jump praktik_a

                "Да, давай, там удобнее всего!":
                    jump praktik_b

                "Ну не знаю... Я всегда думал, что там хуже слышно преподавателя.":
                    jump praktik_c    

            label praktik_a:

                show pasha at right

                p "АЛЯСКОЙ на студенческом сленге называют места в аудитории, которые расположены дальше всего от преподавателей"

                hide pasha
 
                jump choice2_done

            label praktik_b:

                s "О чём ты? Взгляни какой ясный денёчек!"

                jump choice2_done

            label praktik_c:

                show igor at right    

                i "ня"

                hide igor

                jump choice2_done

        label choice2_done:

            show igor at right

            show gus

            g "А теперь давай проверим, как хорошо ты понимаешь то, чем ты пользуешься!"

            show pasha:
                xalign 0.3
                yalign 1.0
 
            p "Неееет..."

            hide pasha

            hide igor

            hide gus

            show pasha at right 

            p "Почему тебе не нравятся ЗАДНИЕ РЯДЫ АУДИТОРИИ?"

            menu:

                "Я не хочу сидеть НАВЕРХУ...":
                    jump praktik_a

                "Это же КОНЕЦ АУДИТОРИИ, мне будет плохо видно.":
                    jump praktik_b

                "Всё хорошо, ПОСЛЕДНИЕ РЯДЫ – это круто!":
                    jump praktik_c        
 
        return    


   

    

   
 
