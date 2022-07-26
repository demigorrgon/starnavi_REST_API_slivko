# Social network REST API test task by Valentyn Slivko for Python dev position
Tech stack used: 
- `Django Rest Framework`, 
- `PostgreSQL`,
-  `pytest`

Additional Django extensions: 
- `djangorestframework-simplejwt` - adds 'plug-and-play' JWT token support to the project
- `drf-spectacular` - auto Swagger schema/docs generation

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Firing up the project
### With docker-compose:
```docker-compose up --build``` from root directory

### With poetry:
```
    poetry env use python3.10
    poetry shell
    python3 manage.py migrate
    python3 manage.py runserver
```

### pip:
```
    pip install -r requirements.txt
    python3 -m venv venv
    source venv/bin/activate
    python3 manage.py migrate
    python3 manage.py runserver
```
To run tests outside of CI 
```
    pip install -r requirements_dev.txt
    <venv setup>
    pytest
```

### Postman collection available in `starnavi_test_project_slivko.postman_collection.json`