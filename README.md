# referral_system

# API для верификации номера телефона

Данное Django-приложение предоставляет **API** для верификации номера телефона, пригласительных кодов друзей и страниц профилей пользователей.

**Объясняю API. Если хотите, можете попробовать сами использовать JSON и APIView. 
Но если этого не хотите, то проект уже готов. В нем уже есть HTML-отображение. 
Можете сразу переходить к разделу 'Начало работы и Использование', чтобы начать пользоваться. 
В этом разделе содержатся инструкции для использования уже готового проекта. 
И я также развернул его на PythonAnywhere(https://codebroh.pythonanywhere.com/verify-phone/). Вы можете пойти и использовать его. 
Но перед этим свяжитесь со мной(https://t.me/nematulloh_uktamov), чтобы я мог добавить ваш номер телефона в Twilio(oн отправляет смс на ваш номер телефона). 
В противном случае следуйте инструкциям в README, 
чтобы увидеть код подтверждения в терминале во время выполнения.**
## Конечные точки

### Верификация номера телефона

#### Запрос

- **POST /verify-phone/**
  - Отправьте номер телефона для начала процесса верификации.
  - Тело запроса: **JSON**
    ```json
    {
        "phone_number": "ваш_номер_телефона"
    }
    ```
  - Ответ: Перенаправление на **/verify-code/**

#### Верификация кода

- **GET /verify-code/**
  - Отображение формы для ввода верификационного кода.
  - Тело запроса: Отсутствует
  - Ответ: **HTML**-форма

- **POST /verify-code/**
  - Проверка введенного верификационного кода.
  - Тело запроса: **JSON**
    ```json
    {
        "verification_code": "введенный_код"
    }
    ```
  - Ответ: Перенаправление на **/my-page/** при успешной верификации или отображение сообщения об ошибке.

### Страница профиля пользователя

- **GET /my-page/**
  - Отображение страницы профиля пользователя после успешной верификации.
  - Тело запроса: Отсутствует
  - Ответ: **HTML**-страница с данными пользователя и пригласительными кодами друзей.

#### Верификация кода приглашения друга

- **POST /verify-friend-invite/**
  - Проверка кода приглашения друга и связывание его с пользователем.
  - Тело запроса: Данные формы
    ```json
    {
        "friend_invite_code=": "код_друга"
    }
    ```
  - Ответ: Перенаправление на **/my-page/** при успешной верификации или отображение сообщения об ошибке.

## Начало работы

1. Клонируйте этот репозиторий.
2. Создайте виртуальное окружение Django и установите необходимые зависимости(twilio, pyotp, decouple, djangorestframework).
3. A) Обновите настройки Twilio в вашем файле views.py.
Войдите в систему, создайте учетную запись twilio и скопируйте sid, токен и свой номер twilio 
или свяжитесь со мной(https://t.me/nematulloh_uktamov), чтобы я добавил ваш номер телефона в свою учетную запись twilio.
B) После отправки номера телефона вы увидите 4-значный код, напечатанный в терминале, над которым вы работаете.
5. Примените миграции: `python manage.py makemigrations && python manage.py migrate`
6. Создайте суперпользователя: `python manage.py createsuperuser`
7. Запустите приложение: `python manage.py runserver`

## Использование

1. Перейдите по адресу **/verify-phone/** и введите свой номер телефона, чтобы получить верификационный код.
2. Перейдите на страницу **/verify-code/** и введите полученный код.
3. После успешной верификации перейдите на **/my-page/**, чтобы просмотреть страницу профиля пользователя.
4. При необходимости используйте **/verify-friend-invite/** для связывания пригласительных кодов друзей.





---

Не переводите команды кода для точного понимания и использования. Соответственно адаптируйте **README** под конкретные детали и требования вашего проекта. Хорошо документированный **README** поможет другим пользователям понять, как использовать ваше **API**, и сделает ваш проект более коллаборативным.
