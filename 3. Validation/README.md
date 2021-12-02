# Validation in Django REST Framework

> Besically there are three types of validation present in django

1. Field Level Validation
2. Object Level Validation
3. Validator

### Field Level Validation

- We can specify custom field-level validation by adding **_validate_fieldname_** methods to your serializer subclass.

- These are similar to the **_clean_fieldname_** methods on django forms

- **_validate_fieldname_** methods should return the validated value of raise a serializers. Validation Error

- Syntax

```sh
def validate_fieldname(self, value)
```

- Example

```python
   from rest_framework import serializers
      class StudentSerializer(serializers.Serializer):
          name = serializers.CharField(max_length=100)
          roll = serializers.IntegerField()
          city = serializers.CharField(max_length=100)
      def validate_roll(self,value):
          if value >= 200:
              raise serializers.ValidationError('seat full')
          return value
```

> Note: Where value is the field value that requires validations/

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

- The clone this repo

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
