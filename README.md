# Django-CRM

Basic CRM System made up with Django. 

Features:

➡️ Frontend - HTML and Bootstrap
➡️ Backend - Django and MySQL Django-CRM

## Features

- **Frontend**: HTML and Bootstrap
- **Backend**: Django and MySQL

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Installation

### Prerequisites

- Python 3.12.3
- Django
- MySQL

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/django-crm.git
   cd django-crm
   ```
   
2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    venv/Scripts/activate  # Only for Windows
    ```
    
3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
    
4. **Configure the database**:
    - Update the DATABASES setting in settings.py with your MySQL configuration.

5. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```
    
6. **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```
    
7. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

### Usage

- Access the application at localhost.
- Login with the superuser credentials created during installation.
- Add, update, and manage customer records.

### Contributing

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes.
4. Commit your changes (git commit -m 'Add some feature').
5. Push to the branch (git push origin feature-branch).
6. Open a pull request.
