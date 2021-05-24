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
    
    #выбор имени
    python:
        name=renpy.input("Пока мы не начали, не расскажете как вас зовут?\n(Имя по-умолчанию - Саад")
        name=name.strip() or "Саад"
    #начало сюжета
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

        "Я хочу играть на русском":
            jump choice1_russian

        "The main character will think in English":
            jump choice1_english

        "البطل المهم سوف يفكر باللغة العربية\n work in progress":
            jump choice1_arabic

    label choice1_russian:

        g "Хорошо. К сожалению русская версия находится в разработке. Несколько раз нажмите
         \"Назад\" внизу экрана и выберите английский язык, если хотите продолжить "

        jump map

    label choice1_english:

        g "Great!"

        jump map

    label choice1_arabic:

        g "Good. Unfortunately, the Arabic version is in development. Tap repeatedly
         \"Back\" at the bottom of the screen and select English if you want to continue"

        jump map
    #код карты
    label map:
        screen map:
                imagemap:
                    ground "images/map.jpg"
                    idle "images/map.jpg"
                    hotspot (330, 510, 110, 100) action Return("label_1") alt "label_1"
                    hotspot (504, 540, 60, 60) action Return("label_2") alt "label_2"
                    hotspot (207, 630, 60, 60) action Return("label_3") alt "label_3"
                    hotspot (177, 900, 60, 60) action Return("label_4") alt "label_4"
                    hotspot (520, 325, 60, 60) action Return("label_5") alt "label_5"
                    hotspot (840, 627, 60, 60) action Return("label_6") alt "label_6"
                    hotspot (1458, 770, 60, 60) action Return("label_7") alt "label_7"
                    hotspot (1477, 400, 70, 70) action Return("label_8") alt "label_8"
                    hotspot (1182, 120, 70, 70) action Return("label_9") alt "label_9"

        window hide None
        call screen map
    if Return == "label_1":
        jump label_1
    if Return == "label_2":
        jump label_2  
    if Return == "label_3":
        jump label_3
    if Return == "label_4":
        jump label_4
    if Return == "label_5":
        jump label_5            
    if Return == "label_9":
        jump label_9 
        
    label label_1:
        window hide None
        scene guk
        g "sadsa"
        jump imagemap_done
    label label_2:
        window hide None
        scene ineu
        g "sadsa"
        jump imagemap_done 
    label label_3:
        window hide None
        scene guk
        g "sadsa"
        jump imagemap_done 
    label label_4:
        window hide None
        scene stroika
        g "sadsa"
        jump imagemap_done
    label label_5:
        window hide None
        scene teplofuck
        g "sadsa"
        jump imagemap_done 
    label label_6:
        window hide None
        scene guk
        g "sadsa"
        jump imagemap_done
    label label_7:
        window hide None
        scene guk
        g "sadsa"
        jump imagemap_done
    label label_8:
        window hide None
        scene guk
        g "sadsa"
        jump imagemap_done   
    label label_9:
        window hide None
        scene hotel
        g "sdvsdvds"
        jump imagemap_done 
    label imagemap_done:
        return    
return
        


   

    

   
 
