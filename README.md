# Dr. Matheus Bomfim - Django Website

This is a complete Django version of the institutional website for Dr. Matheus Bomfim.
It is intentionally simple so you can unzip it and start working with Python immediately.

## Stack

- Python
- Django
- HTML templates with Jinja-like Django templating
- CSS
- Static media files

## Project structure

- `manage.py`: Django entry point
- `config/`: project settings and URLs
- `website/`: app with views, templates, static files, and tests

## First run on Windows PowerShell

```powershell
cd D:\dev\matheus_bomfim_django
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

## Useful commands

### Run tests

```powershell
python manage.py test
```

### Create a superuser later

```powershell
python manage.py createsuperuser
```

### Collect static files later for production

```powershell
python manage.py collectstatic
```

## Notes

- The site uses the images and video already provided for this project.
- The footer includes developer attribution for HelpUS.
- The site is mobile responsive.
- The database is SQLite for simplicity.
