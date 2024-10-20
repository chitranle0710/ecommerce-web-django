# Django project with sqlite

## overview
This project is a web application built using django, a high-level python web framework. it utilizes sqlite as the database for data storage and demonstrates the capabilities of django in creating a simple, scalable web application.

<img width="1680" alt="Ảnh màn hình 2024-10-20 lúc 15 42 46" src="https://github.com/user-attachments/assets/cfb64251-880a-4935-ac7b-2021a8f6f0ad">

<img width="1680" alt="Ảnh màn hình 2024-10-20 lúc 15 43 47" src="https://github.com/user-attachments/assets/8a8b38f3-ce5a-4988-b68e-e5a58586f2dc">

<img width="1680" alt="Ảnh màn hình 2024-10-20 lúc 15 53 04" src="https://github.com/user-attachments/assets/74d5d1b2-33d7-424e-8fb2-06578cae9506">

<img width="1680" alt="Ảnh màn hình 2024-10-20 lúc 15 53 14" src="https://github.com/user-attachments/assets/a2271f0a-8834-430e-b441-626844ab275a">

<img width="1680" alt="Ảnh màn hình 2024-10-20 lúc 15 53 33" src="https://github.com/user-attachments/assets/e8bbe7c1-8382-49a9-9eb2-4cd21956a802">


## Table of contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Running the application](#running-the-application)
- [Contributing](#contributing)
- [License](#license)

## Features
- Simple and intuitive user interface
- Crud (create, read, update, delete) functionality
- Sqlite database for easy setup and management
- Virtual environment to isolate project dependencies

## Requirements
- Python 3.x
- Django 3.x or higher
- Sqlite (comes pre-installed with python)

## Installation

1. **clone the repository**:
   ```bash
   git clone https://github.com/chitranle0710/ecommerce-web-django.git
2. **Create a virtual environment:
   `python -m venv virt`
3. **Activate the virtual environment**:
   On Windows: `virt\Scripts\activate`
   On MacOS: `source virt/bin/activate`
4. **Install the required packages**:
   `pip install django`
5. **Usage**
Run migrations to set up the database: `python manage.py migrate`
Create a superuser for the admin interface: `python manage.py createsuperuser`
Run the development server: `python manage.py runserver`

6. **Access**
Access the application: Open your web browser and navigate to http://127.0.0.1:8000/.

Access the admin interface: Navigate to http://127.0.0.1:8000/admin/ and log in using the superuser credentials you created earlier.



