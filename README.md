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
или свяжитесь со мной(https://t.me/nematulloh_uktamov), чтобы я добавил ваш номер телефона в свою учетную запись Twilio((oн отправляет смс на ваш номер телефона)).
B) После отправки номера телефона вы увидите 4-значный код, напечатанный в терминале, над которым вы работаете.
5. Примените миграции: `python manage.py makemigrations && python manage.py migrate`
6. Создайте суперпользователя: `python manage.py createsuperuser`
7. Запустите приложение: `python manage.py runserver`

## Использование

1. Перейдите по адресу **/verify-phone/** и введите свой номер телефона, чтобы получить верификационный код.
2. Перейдите на страницу **/verify-code/** и введите полученный код.
3. После успешной верификации перейдите на **/my-page/**, чтобы просмотреть страницу профиля пользователя.
4. При необходимости используйте **/verify-friend-invite/** для связывания пригласительных кодов друзей.




# referral_system

# API for Phone Number Verification

This Django application provides an **API** for phone number verification, friend invitation codes, and user profile pages.

**Explaining the API: If you want, you can try using JSON and APIView on your own. 
But if you prefer not to, the project is already prepared. It includes an HTML display. 
You can directly proceed to the 'Getting Started and Usage' section to start using it. 
This section contains instructions for using the ready-made project. 
I've also deployed it on PythonAnywhere (https://codebroh.pythonanywhere.com/verify-phone/). You can visit and use it. 
However, before using it, please contact me (https://t.me/nematulloh_uktamov) so that I can add your phone number to Twilio (it sends SMS to your phone number). 
Alternatively, follow the instructions in the README to see the confirmation code in the terminal during execution.**

## Endpoints

### Phone Number Verification

#### Request

- **POST /verify-phone/**
  - Send your phone number to initiate the verification process.
  - Request Body: **JSON**
    ```json
    {
        "phone_number": "your_phone_number"
    }
    ```
  - Response: Redirect to **/verify-code/**

#### Code Verification

- **GET /verify-code/**
  - Display the form to enter the verification code.
  - Request Body: None
  - Response: **HTML** form

- **POST /verify-code/**
  - Verify the entered verification code.
  - Request Body: **JSON**
    ```json
    {
        "verification_code": "entered_code"
    }
    ```
  - Response: Redirect to **/my-page/** upon successful verification or display an error message.

### User Profile Page

- **GET /my-page/**
  - Display the user profile page after successful verification.
  - Request Body: None
  - Response: **HTML** page with user data and friend invitation codes.

#### Verify Friend Invitation Code

- **POST /verify-friend-invite/**
  - Verify a friend's invitation code and associate it with the user.
  - Request Body: Form data
    ```json
    {
        "friend_invite_code": "friend_code"
    }
    ```
  - Response: Redirect to **/my-page/** upon successful verification or display an error message.

## Getting Started

1. Clone this repository.
2. Create a Django virtual environment and install the required dependencies (twilio, pyotp, decouple, djangorestframework).
3. A) Update the Twilio settings in your views.py file.
   Log in, create a twilio account, and copy the SID, token, and your twilio number.
   Or, contact me (https://t.me/nematulloh_uktamov) to add your phone number to my Twilio account (it sends SMS to your phone number).
   B) After sending the phone number, you will see a 4-digit code printed in the terminal that you're working with.
5. Apply migrations: `python manage.py makemigrations && python manage.py migrate`
6. Create a superuser: `python manage.py createsuperuser`
7. Run the application: `python manage.py runserver`

## Usage

1. Visit **/verify-phone/** and enter your phone number to receive a verification code.
2. Go to **/verify-code/** and enter the received code.
3. After successful verification, go to **/my-page/** to view the user profile page.
4. Use **/verify-friend-invite/** if needed to associate friend invitation codes.


