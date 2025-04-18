# TO-DO-Application

## Description
TO-DO-Application is a web-based task management application built with Django framework. It helps users organize and track their daily tasks efficiently.

## Technologies
- Python 3.12.3
- Django
- HTML/CSS
- SQLite (Django default database)

## Dependencies
- click
- django
- ipython
- jinja2
- pyyaml
- requests
- selenium
- six
- tornado

## Installation and Setup

1. Clone the repository:
 bash git clone

2. Create and activate virtual environment:
bash python -m venv venv source venv/bin/activate # for Linux/Mac

3. Install dependencies:
bash pipenv lock

4. Run migrations:
bash python manage.py migrate

5. Start development server:
```bash
python manage.py runserver
```
The application will be available at: `http://localhost:8000`

## Features
- Create, edit and delete tasks
- Mark tasks as completed
- Task categorization
- Priority settings
- Task search functionality

## Project Structure
TO-DO-Application/
├── manage.py
├── requirements.txt
├── todo/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
└── todo_project/
    ├── settings.py
    ├── urls.py
    └── wsgi.py