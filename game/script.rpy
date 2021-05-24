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
    "В этой игре вы можете выбрать имя главного героя"
    #выбор имени
    python:
        name=renpy.input("Введите имя или нажмите Enter, чтобы пропустить")
        name=name.strip() or "Саад"
    #начало сюжета
    scene guk
    show gus
    "Теперь тебя зовут [name]"
    g "Привет, [name]!"
    main "Привет!"

    g "Ты запустил образовательную игру \"Fake Student\""
    g "Если что, открыть меню можно клавишей \"esc\" или правой кнопкой мыши."
    g "Попробуй выйти в меню. Там ты увидишь, что в этой игре можно сохраняться."
    g "Если захочешь вернуться на предыдущий слайд, можно покрутить колесико мыши"

    show gus at left 
    with Dissolve(.5)
    g "Хоба"
    g "Разработчики перевели игру на несолько языков"
    g "Ты можешь поменять язык в настройках"

    #Здесь, по плану, начинается пролог игры. 
    

    
    #код карты
    screen map():
            imagemap:
                ground "images/map.jpg"
                idle "images/map.jpg"
                hotspot (330, 510, 110, 100) action Jump("guk")
                hotspot (504, 540, 60, 60) action Jump("ineu")
                hotspot (207, 630, 60, 60) action Jump("label_3")
                hotspot (177, 900, 60, 60) action Jump("stroika") 
                hotspot (520, 325, 60, 60) action Jump("teplofuck")
                hotspot (840, 627, 60, 60) action Jump("label_6")
                hotspot (1458, 770, 60, 60) action Jump("label_7") 
                hotspot (1477, 400, 70, 70) action Jump("label_8")
                hotspot (1182, 120, 70, 70) action Jump("dormitory")

    label map:
        # вызов карты
        call screen map
    #Места, в которые можно перейти
    label guk:
        scene guk
        g "Добро пожаловать в ГУК!"
        jump imagemap_done
    label ineu:
        scene ineu
        g "Ты в ИНЭУ"
        jump imagemap_done 
    label label_3:#todo левое крыло гука
        scene guk
        g "sadsa"
        jump imagemap_done 
    label stroika:
        scene stroika
        g "Стройка"
        jump imagemap_done
    label teplofuck:
        scene teplofuck
        g "Теплофак❤"
        jump imagemap_done 
    label label_6:#todo ФТИ
        scene guk
        g "sadsa"
        jump imagemap_done
    label label_7:#todo Радик
        scene guk
        g "sadsa"
        jump imagemap_done
    label label_8:#todo Физ-ра
        scene guk
        g "sadsa"
        jump imagemap_done   
    label dormitory:
        scene dormitory
        g "Родная общага"
        jump imagemap_done 
    label imagemap_done:
        return     
return
        


   

    

   
 
