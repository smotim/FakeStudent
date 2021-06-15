# Вы можете расположить сценарий своей игры в этом файле.
# Определение персонажей игры.
define g = Character('Гусь', color="#c8fff8")
define s = Character('[name]', color="#c6fcc8")
image gus = im.Scale("gus.png", 480, 700)
define main = Character("[name]")
image history_teacher = im.Scale("history_teacher.png", 244, 866)
define hist = Character('Елена Игоревна', color="#c8fff8")
image model = ("modelka.png")
 
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
    menu:
        "Зайти в ГУК":
            jump story_11
    label story_11:
        scene secret_base
        show history_teacher at right
        "???" "Проходите, присаживайтесь... Всем здравствуйте! Я Елена Игоревна, ваш преподаватель истории."
        hist "Теперь взгляните на доску. Как думаете, что тут изображено?"
        show letopis at left
        "смотрит на вас"
        hist "Молодой человек"
        show history_teacher at center
        hist "Молодой человек на {color=#025}Аляске{/color}?" #(Аляска – сленг)"
        "кажется нужно как-то отреагировать"
        label .choice1:
            menu: 
                "Но тут же летопись, а не парень":
                    hist "Ой, наверное вы не поняли? {color=#025}Аляска{/color} – последние ряды аудитории. То есть, я таким образом обратилась к тебе"
                    $ renpy.notify("Слово \"Аляска\" добавлено в словарь")#В словарь
                    main "Спасибо, что объяснили! Мне кажется, это летопись."
                "-Промолчать-":
                    show model at right
                    "какая-то девушка" "Эй! Это к тебе обратились."
                    main "Мне кажется, это летопись."
                "Это летопись?":
                    ""
            hist "Верно! Это страница из Лаврентьевской летописи. Едва ли современный человек без подготовки сможет прочитать что-нибудь"
        show history_teacher at left
        hist "Теперь попробуйте самостоятельно узнать в каком году была создана эта летопись."
        "*Кто-то с заднего ряда*" "Сейчас {color=#025}загуглим{/color}"
        show screen browser
        $ renpy.notify("Нажми на строку поиска, чтобы выйти в Интернет") 
        "Ты решаешь тоже посмотреть в интеренете и открываешь свой ноутбук"
        ### возможно плашку с объяснением браузера
        jump .story12
        
        
    label googling:
        hide screen browser
        "Похоже этой летописи почти 700 лет"#тут кстати два синонима подряд
        $sosed_message=True
        $ renpy.notify("✉Новое уведомление от Вконтакте")
        "Кажется мне пришло какое-то сообщение"
        #play sound "sound/ring.mp3" - очень громко
        "Пара уже закончилась, посмотрю потом"
    
    label .story_12:
        show screen map
        "Нужно вернуться в {color=#025}общагу{/color}"
        $ renpy.notify("Общежитие = кнопка №8")
    
    #браузер и кнопки на его главной странице
    label browser:
        show screen browser
        "Это экран браузера, здесь можно переходить на сайты, нажимая на значки под строкой поиска"
    label brs:
        scene browser_brs
        "Место, куда преподаватели выставляют оценки"
        return
    label vk:
        show screen browser_vk
        if sosed_message:
            show screen sosed_new_vk
        show screen vk_mc_name
        "Место для общения с одногруппниками"
    label plan:
        scene browser_plan
        "Здесь можно посмотреть список предметов"
    label scheduele:
        scene browser_scheduele
        "Расписание занятий"
    label teams:
        scene browser_teams
        "Расписание занятий"
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
        show screen map
    #Места, в которые можно перейти
    label guk:
        scene guk
        g "Добро пожаловать в ГУК!"
        jump map_done
    label ineu:
        scene ineu
        g "Ты в ИНЭУ"
        jump map_done 
    #label label_3:#todo левое крыло гука
        #scene guk
        #g "sadsa"
        #jump imagemap_done 
    label stroika:
        scene stroika
        g "Стройка"
        jump map_done
    label teplofuck:
        scene teplofuck
        g "Теплофак❤"
        jump map_done 
    label fizteh:
        scene fizteh
        g "Welcome"
        jump map_done
    label chempion:
        scene chempion
        g "*Эта локация одобрена разработчиками*"
        jump map_done
    label label_8:#todo Физ-ра
        scene guk
        g "sadsa"
        jump map_done   
    label dormitory:
        scene dormitory
        show screen dormitory_label
        "Внимание, конец игры!"
        return
    label inmt:
        scene inmt
        g "Кеша"
        jump map_done 
    label map_done:
        return     
return
        
label dict:
    call screen dictionary
label lapt:
    call screen browser

   

    

   
 
