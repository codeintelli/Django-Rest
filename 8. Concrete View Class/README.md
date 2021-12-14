# Concrete View Class

- The following classes are the concrete generic views.
- If you're using generic views this is normally the level you'll be working at unless you need heavily customized behaviour.
- The view classes can be imported from rest_framework.generics.

  - ListAPIView
  - CreateAPIView
  - RetrieveAPI View
  - UpdateAPIView
  - DestroyAPIView
  - ListCreateAPIView
  - RetrieveUpdateAPIView
  - RetrieveDestroyAPIView
  - RetrieveUpdateDestroyAPIView

  ## ListAPI View

  - It is used for read-only endpoints to represent a collection of model instances. It provides a get method handler.
    Extends: GenericAPI View, ListModelMixin

  ```python
  from rest_framework.generics import ListAPIView
  class Student_details(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
  ```

  ## CreateAPIView

  - It is used for create-only endpoints. It provides a post method handler.
  - Extends: GenericAPI View, CreateModelMixin

  ```python
  from rest_framework.generics import CreateAPIView
  class Student_details(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
  ```

  ## RetrieveAPIView

  - It is used for read-only endpoints to represent a single model instance. It provides a get method handler.
  - Extends: GenericAPI View, RetrieveModelMixin

  ```python
  from rest_framework.generics import RetrieveAPIView
  class Student_details(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
  ```

  ## UpdateAPIView

  - It is used for update-only endpoints for a single model instance. It provides put and patch method handlers.

  - Extends: GenericAPI View, UpdateModelMixin

  ```python
  from rest_framework.generics import UpdateAPIView
  class Student_details(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
  ```

  ## DistroyAPIView

  - It is used for delete-only endpoints for a single model instance. It provides a delete method handlers.

  - Extends: GenericAPI View, DestroyModelMixin

  ```python
  from rest_framework.generics import DestroyAPIView
  class Student_details(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
  ```

  ## ListCreateAPIView

  - It is used for read-write endpoints to represent a collection of model instances. It provides a get and post method handlers.

  - Extends: GenericAPI View, ListModelMixin, CreateModelMixin

  ```python
  from rest_framework.generics import ListCreateAPIView
  class Student_details(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
  ```

  ## RetrieveUpdateAPIView

  - It is used for read or update endpoints to represent a single model instance. It provides a get, put and post method handlers.

  - Extends: GenericAPI View, RetrieveModelMixin, UpdateModelMixin

  ```python
  from rest_framework.generics import RetrieveUpdateAPIView
  class Student_details(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
  ```

  ## RetrieveDestroyAPIView

  - It is used for read or delete endpoints to represent a single model instance. It provides a get and delete method handlers.

  - Extends: GenericAPI View, RetrieveModelMixin, DestroyModelMixin

  ```python
  from rest_framework.generics import RetrieveDestroyAPIView
  class Student_details(RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
  ```

  ## RetrieveUpdateDestroyAPIView

  - It is used for read-write-delete endpoints to represent a single model instance. provides get, put, patch and delete method handlers.

  - Extends: GenericAPI View, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin

  ```python
  from rest_framework.generics import RetrieveUpdateDestroyAPIView
  class Student_details(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
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
- [Django Generic API View](https://github.com/CodeIntelli/Django-Rest/tree/main/7.%20Generic%20%20API%20View)
