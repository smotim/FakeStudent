# Вы можете расположить сценарий своей игры в этом файле.
# Определение персонажей игры.
define g = Character('Гусь', color="#c8fff8")
define s = Character('[name]', color="#c6fcc8")
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
    "Теперь тебя зовут [name]"
    show gus
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
    #TODO здесь скрыть экран
    s "Я плохо учился в школе, не смог никуда поступить."
    scene secret base
    
    show saad 
    with Dissolve(.6)
    s "Из-за этого пришлось искать работу."
    s "Нигде не задерживался на долго"
    
    #код карты
    screen map():
            imagemap:
                ground "images/map.jpg"
                idle "images/map.jpg"
                hotspot (330, 510, 110, 100) action Jump("guk")#на карте номер 1
                hotspot (504, 540, 60, 60) action Jump("ineu")#на карте номер 2
                #hotspot (207, 630, 60, 60) action Jump("label_3")
                hotspot (177, 900, 60, 60) action Jump("stroika")#на карте номер 4 
                hotspot (520, 325, 60, 60) action Jump("teplofuck")#на карте номер 5
                hotspot (840, 627, 60, 60) action Jump("fizteh")#на карте номер 6
                hotspot (1458, 770, 60, 60) action Jump("chempion")#на карте номер 7 
                hotspot (1477, 400, 70, 70) action Jump("label_8")#на карте номер 8
                hotspot (1182, 120, 70, 70) action Jump("dormitory")#на карте номер 9
                hotspot (1264, 848, 134, 96) action Jump("inmt")#пока без номера

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
    #label label_3:#todo левое крыло гука
        #scene guk
        #g "sadsa"
        #jump imagemap_done 
    label stroika:
        scene stroika
        g "Стройка"
        jump imagemap_done
    label teplofuck:
        scene teplofuck
        g "Теплофак❤"
        jump imagemap_done 
    label fizteh:
        scene fizteh
        g "Welcome"
        jump imagemap_done
    label chempion:
        scene chempion
        g "*Эта локация одобрена разработчиками*"
        jump imagemap_done
    label label_8:#todo Физ-ра
        scene guk
        g "sadsa"
        jump imagemap_done   
    label dormitory:
        scene dormitory
        g "Родная общага"
    label inmt:
        scene inmt
        g "Кеша"
        jump imagemap_done 
    label imagemap_done:
        return     
return
        


   

    

   
 
