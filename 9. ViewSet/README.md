# ViewSet

- Django REST framework allows you to combine the logic for a set of related views in a single class, called a ViewSet.

- There are two main advantages of using a ViewSet over using a View class.

  - Repeated logic can be combined into a single class.

  - By using routers, we no longer need to deal with wiring up the URL conf ourselves.

## ViewSet Class

- A ViewSet class is simply a type of class-based View, that does not provide any method handlers such as get() or post(), and instead provides actions such as list() and create().

  - list()- Get All Records.
  - retrieve() - Get Single Record
  - create()- Create/Insert Record
  - update()- Update Record Completely
  - partial_update()- Update Record Partially
  - destroy()- Delete Record

```python
from rest_framework import viewsets
class Student ViewSet(viewsets.ViewSet):
  def list(self, request):
  def create(self, request):
  def retrieve(self, request, pk=None):
  def update(self, request, pk=None):
  def partial_update(self, request, pk=None):
  def destroy(self, request, pk=None):
    ........

```

- During dispatch, the following attributes are available on the ViewSet:

  - basename - the base to use for the URL names that are created.
  - action - the name of the current action (c.g., list, create).
  - detail- boolean indicating if the current action is configured for a list or detail view.
  - suffix - the display suffix for the viewset type-mirrors the detail attribute.
  - name - the display name for the viewset. This argument is mutually exclusive to suffix.
  - description - the display description for the individual view of a viewset.

## ViewSet-URL Config

```python
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter() # Creating Default Router Object

router.register('studentapi', views.StudentViewSet, basename='student') # Register StudentViewSet with Routers

urlpatterns = [
  path('',include(router.urls)),
]
# The API URLs are now determine automatically by the router.
```

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
