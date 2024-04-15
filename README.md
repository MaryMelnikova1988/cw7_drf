# cw_drf_atomic_habits

### Задание

Контекст
В 2018 году Джеймс Клир написал книгу «Атомные привычки», которая посвящена приобретению новых полезных привычек и искоренению старых плохих привычек. Заказчик прочитал книгу, впечатлился и обратился к вам с запросом реализовать трекер полезных привычек.

В рамках учебного курсового проекта реализуйте бэкенд-часть SPA веб-приложения.

### Критерии приемки курсовой работы

1. Настроили CORS.
2. Настроили интеграцию с Телеграмом.
3. Реализовали пагинацию.
4. Использовали переменные окружения.
5. Все необходимые модели описаны или переопределены.
6. Все необходимые эндпоинты реализовали.
7. Настроили все необходимые валидаторы.
8. Описанные права доступа заложены.
9. Настроили отложенную задачу через Celery.
10. Проект покрыли тестами как минимум на 80%.
11. Код оформили в соответствии с лучшими практиками.
12. Имеется список зависимостей.
13. Результат проверки Flake8 равен 100%, при исключении миграций.
14. Решение выложили на GitHub.

### Описание задач

1. Добавьте необходимые модели привычек.
2. Реализуйте эндпоинты для работы с фронтендом.
3. Создайте приложение для работы с Telegram и рассылками напоминаний.

#### Модели

В книге хороший пример привычки описывается как конкретное действие, которое можно уложить в одно предложение:

я буду [ДЕЙСТВИЕ] в [ВРЕМЯ] в [МЕСТО]

За каждую полезную привычку необходимо себя вознаграждать или сразу после делать приятную привычку. Но при этом привычка не должна расходовать на выполнение больше двух минут. Исходя из этого получаем первую модель — «Привычка».

##### Привычка:

1. Пользователь — создатель привычки.
2. Место — место, в котором необходимо выполнять привычку.
3. Время — время, когда необходимо выполнять привычку.
4. Действие — действие, которое представляет собой привычка.
5. Признак приятной привычки — привычка, которую можно привязать к выполнению полезной привычки.
6. Связанная привычка — привычка, которая связана с другой привычкой, важно указывать для полезных привычек, но не для приятных.
7. Периодичность (по умолчанию ежедневная) — периодичность выполнения привычки для напоминания в днях.
8. Вознаграждение — чем пользователь должен себя вознаградить после выполнения.
9. Время на выполнение — время, которое предположительно потратит пользователь на выполнение привычки.
10. Признак публичности — привычки можно публиковать в общий доступ, чтобы другие пользователи могли брать в пример чужие привычки.

Обратите внимание, что в проекте у вас может быть больше, чем одна описанная здесь модель.

Чем отличается полезная привычка от приятной и связанной?
* Полезная привычка — это само действие, которое пользователь будет совершать и получать за его выполнение определенное вознаграждение (приятная привычка или любое другое вознаграждение).

* Приятная привычка — это способ вознаградить себя за выполнение полезной привычки. Приятная привычка указывается в качестве связанной для полезной привычки (в поле «Связанная привычка»).

Например: в качестве полезной привычки вы будете выходить на прогулку вокруг квартала сразу же после ужина. Вашим вознаграждением за это будет приятная привычка — принять ванну с пеной. То есть такая полезная привычка будет иметь связанную привычку.

Рассмотрим другой пример: полезная привычка — «я буду не опаздывать на еженедельную встречу с друзьями в ресторан». В качестве вознаграждения вы заказываете себе десерт. В таком случае полезная привычка имеет вознаграждение, но не приятную привычку.

Признак приятной привычки — булево поле, которые указывает на то, что привычка является приятной, а не полезной.

##### Валидаторы

1. Исключить одновременный выбор связанной привычки и указания вознаграждения.
2. В модели не должно быть заполнено одновременно и поле вознаграждения, и поле связанной привычки. Можно заполнить только одно из двух полей.
3. Время выполнения должно быть не больше 120 секунд.
4. В связанные привычки могут попадать только привычки с признаком приятной привычки.
5. У приятной привычки не может быть вознаграждения или связанной привычки.
6. Нельзя выполнять привычку реже, чем 1 раз в 7 дней.
7. Нельзя не выполнять привычку более 7 дней.
Например, привычка может повторяться раз в неделю, но не раз в 2 недели. За одну неделю необходимо выполнить привычку хотя бы один раз.

#### Пагинация

Для вывода списка привычек реализовать пагинацию с выводом по 5 привычек на страницу.

#### Права доступа

Каждый пользователь имеет доступ только к своим привычкам по механизму CRUD.
Пользователь может видеть список публичных привычек без возможности их как-то редактировать или удалять.

#### Эндпоинты

1. Регистрация.
2. Авторизация.
3. Список привычек текущего пользователя с пагинацией.
4. Список публичных привычек.
5. Создание привычки.
6. Редактирование привычки.
7. Удаление привычки.
8. Интеграция
Для полноценной работы сервиса необходимо реализовать работу с отложенными задачами для напоминания о том, в какое время какие привычки необходимо выполнять.

* Для этого потребуется интегрировать сервис с мессенджером Телеграм, который будет заниматься рассылкой уведомлений.


Инструкция по интеграции с Телеграмом

Вспомнить, как работать с API Телеграма, можно в разделе «Подготовка к практике» в уроке Celery.

#### Безопасность

Для проекта необходимо настроить CORS, чтобы фронтенд мог подключаться к проекту на развернутом сервере.

#### Документация

Для реализации экранов силами фронтенд-разработчиков необходимо настроить вывод документации. При необходимости эндпоинты, на которые документация не будет сгенерирована автоматически, описать вручную.