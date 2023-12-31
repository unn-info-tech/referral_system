# Referral System

## Introduction

The Referral System is a Django Rest Framework-based APIs for phone number verification, friend invitation codes, and user profiles.


## Features

- **Phone Number Verification**: Initiate and verify phone numbers.
- **Friend Invitation Codes**: Verify friend invitation codes and link them to user profiles.
- **User Profiles**: Display user profiles with associated data and friend invitation codes.

## Used Technologies for Backend:
- **Python**: Programming language used for backend development.
- **Django Framework**: Backend framework for API development.
- **Twilio API**: Integrated for SMS functionality.
- **Python Libraries**: pyotp, decouple, djangorestframework.

## Used Technologies for Frontend:

- **HTML/CSS**: Frontend development for web interfaces.

## Gained Experience and Skills

- **API Development**: Creating RESTful APIs using Django and Django REST framework.
- **Integration with Twilio**: Incorporating Twilio API for SMS functionalities.
- **Frontend Design**: Implementing HTML/CSS for web interfaces.


## Getting Started

1. Clone this repository.
2. Create a Django virtual environment and install the required dependencies (twilio, pyotp, decouple, djangorestframework).
3. Update the Twilio settings in your views.py file. You can obtain the necessary credentials from Twilio or get assistance to link your phone number to the Twilio account.
4. After setting up Twilio, execute the necessary commands to apply migrations and create a superuser.
5. Run the application using the command: `python manage.py runserver`

## Usage

1. Visit /verify-phone/ and enter your phone number to receive a verification code.
2. Go to /verify-code/ and enter the received code.
3. After successful verification, access /my-page/ to view the user profile page.
4. Use /verify-friend-invite/ to associate friend invitation codes if needed.   

## Endpoints

### Phone Number Verification

#### POST /verify-phone/
- Sends the phone number to initiate the verification process.
- Request Body: JSON
    ```json
    {
        "phone_number": "your_phone_number"
    }
    ```
- Response: Redirects to /verify-code/

#### GET /verify-code/
- Displays the form to enter the verification code.
- Request Body: None
- Response: HTML form

#### POST /verify-code/
- Verifies the entered verification code.
- Request Body: JSON
    ```json
    {
        "verification_code": "entered_code"
    }
    ```
- Response: Redirects to /my-page/ upon successful verification or displays an error message.

### User Profile Page

#### GET /my-page/
- Displays the user profile page after successful verification.
- Request Body: None
- Response: HTML page with user data and friend invitation codes.

#### POST /verify-friend-invite/
- Verifies a friend's invitation code and associates it with the user.
- Request Body: Form data
    ```json
    {
        "friend_invite_code": "friend_code"
    }
    ```
- Response: Redirects to /my-page/ upon successful verification or displays an error message.



For more information and usage, refer to the relevant endpoints and their descriptions.

