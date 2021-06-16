# Вы можете расположить сценарий своей игры в этом файле.
# Определение персонажей игры.
define g = Character('Гусь', color="#c8fff8")
define s = Character('[name]', color="#c6fcc8")
image gus = im.Scale("gus.png", 480, 700)
define main = Character("[name]")
image history_teacher = im.Scale("history_teacher.png", 244, 866)
define hist = Character('Елена Игоревна', color="#c8fff8")
image model = ("modelka.png")
define volodya = Character('Володя', color="#c8fff8") 
 
#image map = im.Scale("map.jpg")
#image map buttons = im.Scale("map_buttons.jpg")


# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.



# Игра начинается здесь:
label start:
    #объявление переменных для словарика
    $studik=False
    $alaska=False
    $zabil=False
    $bomb=False
    $skovorodka=False
 
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
label tutorial:
    show screen dictionaryButton
    g "В этой игре в любой момент доступен словарик, он только что появился у тебя на экране в правом верхнем углу."
    g "В этот словарик главный герой ([name]) записывает новые слова, которые узнает. Можешь проверить, сейчас там пусто"
    g "Теперь я задам тебе вопрос, а ты должен ответить \"Я не знаю что такое студик\""
    menu:
        "Да":
            g"Мы же договорились! Давай-ка еще раз попробуем"
            jump tutorial
        "Я не знаю что такое студик":
            $renpy.notify("Слово \"студик\" добавлено в словарь")
            $studik=True
            g "Молодец! Видел уведомление в правом верхнем углу? Теперь проверь словарик еще раз"
            show screen browser_button
            "появилась новая кнопка. Работает?"
            g "Ой, кажется ты опаздываешь на историю!"

    menu:
        "Зайти в ГУК":
            jump story_11
    label story_11:
        scene secret_base
        show history_teacher at right
        "???" "Проходите, присаживайтесь... Всем здравствуйте! Я Елена Игоревна, ваш преподаватель истории."
        hist "Теперь взгляните на доску. Как думаете, что тут изображено?"
        show letopis:
            xalign 0.2
            yalign 0.5
 #НЕПРАВИЛЬНО
        "смотрит на меня"
        hist "Молодой человек"
        show history_teacher at center
        hist "Молодой человек на {color=#025}Аляске{/color}?" #(Аляска – сленг)"
        "кажется нужно как-то отреагировать"
        label .choice1:
            menu: 
                "Но тут же летопись, а не парень":
                    hist "Ой, наверное вы не поняли? {color=#025}Аляска{/color} – последние ряды аудитории. То есть, я таким образом обратилась к тебе"
                    $ renpy.notify("Слово \"Аляска\" добавлено в словарь")#В словарь
                    $alaska=True
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
        $ renpy.notify("Нажми на строку поиска, чтобы выйти в Интернет")
        show screen browser 
        "Ты решаешь тоже посмотреть в интеренете и открываешь свой ноутбук"
        ### возможно плашку с объяснением браузера

        
        
    label googling:
        hide screen browser
        "Похоже этой летописи почти 700 лет"#тут кстати два синонима подряд
        $sosed_message=True
        $ renpy.notify("✉Новое уведомление от Вконтакте")
        "Кажется мне пришло какое-то сообщение"
        #play sound "sound/ring.mp3" - очень громко
        "Пара уже закончилась, посмотрю потом"
        show screen map
        "Нужно вернуться в {color=#025}общагу{/color}"
        $ renpy.notify("Общежитие = кнопка №8")
    
    label story_12:

        ####Код Юры
        hide screen map
        show screen dormitory_label
        hide screen dormitory_label
        scene dormitory
        menu:
            "Войти в общежитие":
                jump story_13

    label story_13:
        hide dormitory
        scene dorm_room
        show neighbour at left
        volodya "привет! Ну как пара?"
        s "привет, а почему я тебя не видел сегодня?"
        volodya "я забил на пару"#сленг
        menu:
            "Кого ты забил на пару? Праздник какой-то?":
                jump story_14
            "Почему?":
                jump story_15
    label story_14:
        volodya "Это значит, что я пару прогулял, а не барашка забил."
        $renpy.notify("Слово \"Забил\" добавлено в словарь")
        $zabil=True
        s " А, прости..."
        volodya "Всё норм"

    label story_15:
        volodya "Просто история для меня – джунгли, думаю бомбы к экзамену подготовить..."
        menu:
            "Какая история в джунглях? Какие ещё бомбы?":
                jump story_16
            "Всё так плохо?":
                jump story_17

    label story_16:
        volodya "Не понимаю я предмет, шпоргалки подготовить хочу..."
        $renpy.notify("Слово \"Бомбы\" добавлено в словарь")
        $bomb=True
        s "Ясно!"

    label story_17:
        menu:
            "Мне тоже нужно подготовить бомбы":
                jump story_18
            "Какой же сложный русский язык!":
                jump story_18
    label story_18:
        volodya "Мне нужно на сковородку, пойдёшь со мной?"
        $renpy.notify("Слово \"Сковородка\" добавлено в словарь")
        $skovorodka=True
        s "Нет, я хочу отдохнуть"
    
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
        hide screen map
        scene guk
        g "Добро пожаловать в ГУК!"
        call map_done from _call_map_done
    label ineu:
        hide screen map
        scene ineu
        g "Ты в ИНЭУ"
        jump map_done 
    label stroika:
        hide screen map
        scene stroika
        g "Стройка"
        jump map_done
    label teplofuck:
        hide screen map
        scene teplofuck
        g "Теплофак❤"
        jump map_done 
    label fizteh:
        hide screen map
        scene fizteh
        g "Welcome"
        jump map_done
    label chempion:
        hide screen map
        scene chempion
        g "*Эта локация одобрена разработчиками*"
        jump map_done
    label label_8:#todo Физ-ра
        hide screen map
        scene guk
        g "sadsa"
        jump map_done   
    label dormitory:
        hide screen map
        scene dormitory
        jump story_12
        
        "Внимание, конец игры!"
        jump map_done
        return
    label inmt:
        hide screen map
        scene inmt
        g "Кеша"
        jump map_done 
    label map_done:
        return     
return
        
label dict:
    call screen dictionary
    return
label lapt:
    call screen browser
    "конец игры"
    "конец"
   

    

   
 
