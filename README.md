# FakeStudent
Образовательная визуальная новелла для изучения русского студенческого сленга и синонимов
## Для запуска необходим [Ren'Py](https://www.renpy.org "скачать с официального сайта")  версии 7.4.4 и выше

[![npm version][npm-src]][npm-href]
[![Install size][packagephobia-src]][packagephobia-href]
[![License][license-src]][license-href]

#### Команда Slang:

##### [Смолин Тимофей](https://vk.com/smotim "Страница ВКонтакте")

##### [Двинянинова Мария](https://vk.com/katzuki "Страница ВКонтакте")

##### [Васкевич Юрий](https://vk.com/rejected "Страница ВКонтакте")

##### [Осман Саадаллах](https://vk.com/saad033 "Страница ВКонтакте")

### На что обращать внимание при оценке проекта на движке Ren'Py?
 
* Большая часть кода игры расположена в папке <code>game</code> в файлах *.rpy* (открываются любым текстовым редактором)
* В файле [gui.rpy](https://github.com/smotim/FakeStudent/tree/main/game/gui.rpy "открыть файл") прописано разрешение, в котором запускается игра, а также все связанные с ним вещи (размеры шрифтов, координаты объектов на экране). Большую часть сгенерировал движок, мы здесь меняли только некоторые значения.
* Файл [options.rpy](https://github.com/smotim/FakeStudent/blob/main/game/options.rpy "открыть файл") тоже, по большей части, сгенерирован движком. В нем хранится название игры, номер версии, путь для создания сохранений и т.д.
* Файл [screens.rpy](https://github.com/smotim/FakeStudent/tree/main/game/screens.rpy "открыть файл") содержит логику элементов игры, не связанных с сюжетом (экраны меню и настроек, экран диалога, на котором игрок видит реплики персонажей). В этом файле мы добавляли наши "экраны", вроде словарика главного героя. Также нам пришлось внести небольшие изменения в код меню настроек, чтобы добавить переключение языка игры.
* Сюжет, а также все процессы происходящие на экране во время игры описаны в файле [script.rpy](https://github.com/smotim/FakeStudent/blob/main/game/script.rpy "открыть файл"). Практически весь этот файл написан нами с нуля.
* Папка <code>game/tl</code> содержит файлы переводов. В них просто прописано соответствие строчек на яызке проекта (русский) строчкам на языках перевода. Файлы генерируются автоматически, перевод мы вписываем самостоятельно. (поменять язык в самой игре можно через "настройки")
* Папка <code>game/gui</code> содержит сгенерированные Ренпаем элементы интерфейса и нашу картинку для главного меню.
* В папка <code>game/images</code> находятся все изображения, используемые нами в сюжете игры (фоны, персонажи, карта). Персонажей мы рисовали сами, фоны - это фотографии с фильтром "аппликация". 

### Зачем мы делаем этот проект?
#### Иностранные студенты в России часто испытывают трудности в общении. Проведя опросы среди иностранных студентов ИРИТ-РТФ, мы выявили две сложные темы русского языка, которые слабо раскрыты в учебниках: <code>сленг</code> и <code>синонимы</code>. 

![Какая тема в русском языке для вас самая сложная_](https://user-images.githubusercontent.com/57951811/119371718-0e0ec300-bcd0-11eb-93fc-93e6dea088a2.png)

В деканате мы узнали из каких стран приезжают студенты. На диаграмме яркими цветами выделены страны, в которых разговаривают на <code>арабском языке</code>.

![Иностранные студенты ИРИТ-РТФ](https://user-images.githubusercontent.com/57951811/119371407-d4d65300-bccf-11eb-84b0-f5a9ca5970d2.png)

Мы предположили, что на проблему в общении (и понимании речи преподавателей) можно повлиять в игровой форме. Для этого мы решили создать игру про иностранного шпиона, засланного под прикрытием студента Уральского Федерального Университета. Перед заданием главный герой (имя вводит игрок) не успел хорошо выучить русский, поэтому сленговые слова и синонимы будет узнавать на практике, рискуя быть разоблаченным.

![Снимок экрана 2021-05-24 205343](https://user-images.githubusercontent.com/57951811/119375456-444e4180-bcd4-11eb-8a78-1e480676341f.png)

Карта студгородка из нашей игры (При нажатии на пронумерованные кружки происходит переход на другую локацию)






### P.S:

**Возможно вас интересует будет ли в нашей игре мат? Нет, не будет. Иностранцам можем оставить [ссылку](http://www.russki-mat.net/e/mat_slovar.htm "ВНИМАНИЕ! 18+") для самостоятельного изучения.**

