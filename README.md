# Django Practice

A collection of independent Django projects used to practice Django fundamentals, ORM relationships, templates, forms, authentication, Django REST Framework, and class-based views.

## Projects

| Project | Topic |
| --- | --- |
| `api_pr1` | Django REST Framework models for product categories and products |
| `ipl` | Django app routing and practice views for IPL-style team pages |
| `project12` | Template rendering and basic Django views |
| `project18` | Topic, webpage, and access-record models with database relationships |
| `project19` | One-to-one relationship between countries and capitals |
| `project20` | Department, employee, and salary-grade models with ORM queries |
| `project21` | Django forms and webpage/user data handling |
| `project23` | User registration, login, logout, profiles, password changes, and password reset |
| `project27` | Function-based and class-based views, including CRUD views |
| `swiggy` | Multiple Django apps for food and Instamart-style pages |

The remaining numbered folders (`project1`, `project2`, `project9`, and so on) are additional small practice exercises.

## Built With

- Python 3.10
- Django 5.2
- Django REST Framework
- SQLite
- HTML, CSS, and JavaScript
- Pillow

Database drivers such as MySQL, PostgreSQL, and PyMySQL are included in the existing virtual environment for database practice.

## Getting Started

### 1. Clone the repository

```powershell
git clone https://github.com/rajesh1835/Django-Practice.git
cd Django-Practice
```

### 2. Create a virtual environment

```powershell
py -3.10 -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install django djangorestframework pillow
```

Install other database packages only when working with a specific database:

```powershell
python -m pip install mysqlclient psycopg2 pymysql
```

### 3. Run a project

Each project is a separate Django project. Change into its directory and run the development server:

```powershell
cd project27
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

For another project, return to the repository root and choose that project folder:

```powershell
cd ..
cd project23
python manage.py migrate
python manage.py runserver
```

For projects that already have a superuser, use the Django admin at:

```text
http://127.0.0.1:8000/admin/
```

Create a superuser when needed:

```powershell
python manage.py createsuperuser
```

## Environment Notes

- SQLite databases are ignored by Git and may need to be created locally with `python manage.py migrate`.
- The `venv/`, `.env`, `media/`, `staticfiles/`, and `__pycache__/` directories are excluded by `.gitignore`.
- Some projects may require project-specific static files, media settings, database credentials, or email settings.
- Stop the development server with `Ctrl+C`.

## Useful Django Commands

```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
python manage.py createsuperuser
python manage.py test
python manage.py shell
```

## Repository Layout

```text
Django-Practice/
|-- api_pr1/
|-- ipl/
|-- project1/ ... project27/
|-- swiggy/
|-- venv/
|-- .gitignore
`-- README.md
```
