# Django
## Commands
- `django-admin startproject <project_name>` - create the project with all configuration files required to initialize
- `python3 manage.py runserver`

**Note:** `djago-admin` is called to create a project, but after that the project itself is executed by calling the `manage.py` file instead.

## Files
- [manage.py](manage.py) - store and execute overall configurations 
- [init.py](init.py) - store initial configurations
- [wsgi.py](wsgi.py) - web service responsible for taking the project to prodution
- [asgi.py](asgi.py) - web service responsible for taking the project to prodution
- [urls.py](urls.py) - define applications paths and routes 
- [settings.py](settings.py) - stores all project main configurations

**Note:** Once the project server starts running a `db.sqlite3` file is generate to initialize the database.