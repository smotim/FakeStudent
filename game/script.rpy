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

    g "Кстати, ты сегодня взял студик?"
    menu:
        "Да":
            $start_flag=False
        "Нет":
            $start_flag=False
        "А что это":
            g "Странно, что ты не знаешь. Студиком называют \"студенческий билет\". Это пропуск, по которому студенты заходят в институт."
            $start_flag=True
            $ renpy.notify("Новое слово добавлено в словарь")
    
    show screen dictionaryButton(start_flag)

    #Здесь, по плану, начинается пролог игры. 
    #TODO здесь скрыть экран
    s "Здравствуйте, Денис Борисович!"
    s "Я плохо учился в школе, не смог никуда поступить."
    scene secret base
    
    show saad 
    with Dissolve(.6)
    s "Из-за этого пришлось искать работу."
    s "Нигде не задерживался на долго"
    
    #код карты
    
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
        
label dict:
    call screen dictionary

   

    

   
 
