# Graduate-work

# Веб-текстовый квест на Django "Покоритель подземелья".
==================================================================================
## Разработать простое веб-приложение с использованием Django и SQLite, для создания произвольно генерируемого приключения на основе информации из базы данных.

### Urban University, курс "Разработчик Python", студент Потанин А. В. 

### Содержание

1. Задачи дипломной работы
2. Описание дипломной работы
3. Реализация дипломной работы


## 1. Задачи дипломной работы:
   Предлагается сделать веб приложение на базе фреймворка Django, которое позволит пользователям пройти небольшое текстовое приключение, с случайно генерируемой картой событий. А так же предоставить пользователю вносить дополнение в базу данных без использования админской части

## 2. Описание дипломной работы:
  В качестве темы дипломной работы я выбрал создание веб-квеста, так как это интересная тема позволяющая при последующем развитии создать полноценный продукт-приложение:
  
## 3. Требования к функционалу вебприложения Список задач (To-Do List).

 1. Создание игрока и карты приключения;
  2. Возможность полностью пройти сгенерированое приключение;
  3. Выбрать класс и соответствующие снарежение игрока;
  4. Возможность вносить новые сущности в базу данных

## 4. Структура сайта.
   
  4.1. Стартовая страница, на данной странице игрок вводит имя героя и длину игровой сессии (кол-во комнат будет в игровой карте, по умолчанию 10, минимально возможный размер 7, максимальный 20). Список создается на основе таблицы игроков и классов
   ![](https://github.com/Lienar/Final4/blob/main/Pic/Enter.png)  Рисунок 1 Стартовая страница(Страница выбора игрока)
  4.2. Страница создания персонажа, на данной странице игрок может задать имя персонажи и его класс на базе указания его Id. Список предложенных классов формируется на основе таблицы классов игрока(Player_class)
   ![](https://github.com/Lienar/Final4/blob/main/Pic/Enter.png)  Рисунок 2 Пример  экрана создания персонажа
  4.3. Страница персонажа, на данной странице игрок может посмотреть созданного персонажа с описанием его базового здоровья, класса и базового инвентаря. Список инвентаря формируется на базе таблицы инвентарь игрока и листа предметов 
   ![](https://github.com/stels24/-Help/blob/main/Страница%20регистрации.png) Рисунок 3 Пример страницы персонажа
  4.4. Страница пустой локации, на данной странице игрок видит описательный текст пустой(технической) локации, данные локации предназначены для передачи сюжета и описания окружающего мира.
    ![](https://github.com/stels24/-Help/blob/main/Страница%20регистрации.png) Рисунок 4 Пример пустой(технической страницы)
  4.5. Страница локации с загадкой, на данной странице игрок получает загадку и должен ввести ответ на неё. В случае правильного ответа появляется ссылка на движение дальше, в случае неправильного данной ссылки нет
   ![](https://github.com/stels24/-Help/blob/main/Страница%20регистрации.png) Рисунок 5 Пример локации с загадкой
  4.6. Страница локации с ловушкой, в данной локации игроку на пути попадается ловушка, которая может сработь (шанс указывается при создание) или не сработать, в случае срабатывания персонажу сообщается о полученных повреждения, в противном случае выдается сообщение, что ловушки удалось избежать
   ![](https://github.com/stels24/-Help/blob/main/Страница%20регистрации.png) Рисунок 6 Локация с ловушкой
  4.7. Страница встречи с врагом, в данной локации игроку встречает врага, бой происходит путем выбора предмета из инвентаря. Враг выбирает свои способности случайным образом, в случае низкого здоровья (меньше 50%) пытается лечиться(если способность не в перезарядке)
   ![](https://github.com/stels24/-Help/blob/main/Страница%20регистрации.png) Рисунок 7 Экран боя(все способности активны)
   ![](https://github.com/stels24/-Help/blob/main/Страница%20регистрации.png) Рисунок 8 Экран боя(одна из  способностей на перезарядке)
  4.8. Страница проигрыша, здесь игрок может выбрать пройти новое приключение тем же героем или начать с новым героем
   ![](https://github.com/stels24/-Help/blob/main/Страница%20регистрации.png) Рисунок 9 Страница Gameover
  4.9. Страница победы, на данный момент имеет тот же набор возможностей, что и страница проигрыша
   ![](https://github.com/stels24/-Help/blob/main/Страница%20регистрации.png) Рисунок 10 Страница победы
  4.10.Страница меню редакторов, на данной странице пользователь может выбрать какой элемент он хочет редактировать (добавить)
  ![](https://github.com/stels24/-Help/blob/main/Страница%20регистрации.png) Рисунок 11 Элемент страницы меню редакторов
  4.11.Страница редактора, пример страницы одного из редакторов. Общая схема страниц одинаковая. В верхней части расположены поля для ввода параметров нового объекта, ниже информация, которая может пригодиться для создания.
  ![](https://github.com/stels24/-Help/blob/main/Страница%20регистрации.png) Рисунок 12 Пример страницы одного из редакторов
