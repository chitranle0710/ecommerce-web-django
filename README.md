# django project with sqlite

## overview
this project is a web application built using django, a high-level python web framework. it utilizes sqlite as the database for data storage and demonstrates the capabilities of django in creating a simple, scalable web application.

## table of contents
- [features](#features)
- [requirements](#requirements)
- [installation](#installation)
- [usage](#usage)
- [running the application](#running-the-application)
- [contributing](#contributing)
- [license](#license)

## features
- simple and intuitive user interface
- crud (create, read, update, delete) functionality
- sqlite database for easy setup and management
- virtual environment to isolate project dependencies

## requirements
- python 3.x
- django 3.x or higher
- sqlite (comes pre-installed with python)

## installation

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



