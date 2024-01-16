# CRUD Team People API
## Installing
#### Python3 must be already installed

_Set up the environment_

```
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
```
_Set up requirements_

`pip install -r requirements.txt`

_Make migrations_

Use this commands to make migrations:

`python manage.py makemigrations`

And apply them:

`python manage.py migrate`

_Set up database_

Use following command to load data from database 

`python manage.py loaddata data.json`

_Use following command to run server_

`python manage.py runserver`

### Log in admin
You can create your own superuser using following command:

`python manage.py createsuperuser`

With your credentials you can go to:
`127.0.0.1:8000/admin/`

## Features
* 2 models: Team and People with Many-to-Many relation
* Available CRUD operations for both models on detailed pages by indexes
* Available pagination which is set by 10 objects on list pages of both models
