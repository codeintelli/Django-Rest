# Custom Permissions

- To implement a custom permission, override BasePermission and Implement either, or both, of following methods:

  - has_permission(self, request, view)
  - has_object_permission(self, request, view, obj)

> The methods should return True if the request should be granted access and False otherwise.

customPermission.py

```python
class Mypermission(BasePermission):
  def has_permission(self, request, view)
```

# Permissions

- Third party Packages:-

  - DRF - Access Policy
  - Composed Permissions
  - REST Condition
  - DRY Rest Permissions
  - Django Rest Framework Roles
  - Django REST Framework API Key
  - Django Rest Framework Role Filters
  - Django Rest Framework PSQ

## Setup

> Note: For better view in VS Code Install Better Comments Extension

**For install in your system you just need to**

- install virtual env package

```python
pip install virtualenv
```

- Create Virtual Env

```sh
python3 -m venv env_name
```

- clone this repo

- Install requirements

```sh
pip install -r requirements.txt
```

- Make Migration & Migrate

```sh
py manage.py makemigrations

py manage.py migrate
```

- Runserver

```sh
py manage.py runserver PORT_NO_IF_NEEDED
```

## Also Check REST FULL API

- [Django Function Based API Basic](https://github.com/CodeIntelli/DJANGO-RESTFULL-API_FBV)
- [Django Class Based API Basic](https://github.com/CodeIntelli/DJANGO-RESTFULL-API_CBV)
- [Django Function Based API Using DRF](https://github.com/CodeIntelli/Django-Rest/tree/main/5.%20Function%20Based%20API%20View)
- [Django Class Based API Using DRF](https://github.com/CodeIntelli/Django-Rest/tree/main/6.%20Class%20Based%20API%20View)
