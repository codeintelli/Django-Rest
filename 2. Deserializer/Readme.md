# DeSerialization Django REST Framework

- Serializers are also responsible for deserialization which means it allows parsed data to be converted back into complex types, after validating the incoming data.

  ## BytesIO()

  - A stream implementation using an in-memory bytes buffer. It inherits BufferedIOBase. The buffer is discarded when the close() method is called.

  ```python
  import io
  stream = io.BytesIO(json_data)
  ```

  ## JSONParser()

  - This is used to parse json data to python native data type.

  ```python
  from rest_framework.parsers import JSONParser
  parsed_data = JSONParser().parse(stream)
  ```

- Serializer Methods

  - serializer.is_valid()
  - serializer.validate_data()
  - serializer.errors()

### Creating Serializer Object

```python
serializer = StudentSerializer(data=parsed_data)
```

### Create Data

```python
from rest_framework import serializer
class StudentSerializer(serializers.Serializer):
    name= serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self,validate_data):
        return Student.objects.create(**validate_data)
```

## Setup

**For install in your system you just need to**

- install virtual env package

```sh
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

- For Checking Rest API Uncomment the Comment in myapi file

```sh
python myapi.py
```

## Also Check REST FULL API

- [Django Function Based API Basic](https://github.com/CodeIntelli/DJANGO-RESTFULL-API_FBV)
- [Django Class Based API Basic](https://github.com/CodeIntelli/DJANGO-RESTFULL-API_CBV)
- [Django Function Based API Using DRF](https://github.com/CodeIntelli/Django-Rest/tree/main/5.%20Function%20Based%20API%20View)
- [Django Class Based API Using DRF](https://github.com/CodeIntelli/Django-Rest/tree/main/6.%20Class%20Based%20API%20View)
- [Django Generic API View](https://github.com/CodeIntelli/Django-Rest/tree/main/7.%20Generic%20%20API%20View)
