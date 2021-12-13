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




### Object Level Validation(For Multiple Field)

- when we need to do validation that requires access to multiple fields we do object level validation by adding a method called validate() to serializer subclass.

- it raises a serializers. ValidationError if necessary or just return the validated values.

- Syntax

```sh
def validate(self, value)
```

- Example

```python
   from rest_framework import serializers
      class StudentSerializer(serializers.Serializer):
          name = serializers.CharField(max_length=100)
          roll = serializers.IntegerField()
          city = serializers.CharField(max_length=100)
      def validate(self,data):
          nm = data.get('name')
          ct = data.get('city')
          if nm.lower() == 'rohit' and ct.lower() != 'ranchi':
              raise serializers.ValidationError('City must be ranchi')
          return data
```
> Note: Where, data is a dictionary of field values.


### Validator

- Most of the time you are dealing with validation in REST Framework you will simply be relying on the default field validation or writing explicit validation methods on serializer or field classes.

- However, sometimes you will want to place your validation logic into resuable components so that it can easily be reused throughout your codebase. This can be achieved by using validator functions and validator classes.

- REST framework the validation is performed entirely on the serializer class. this is advantageous for the following reasons:

    - It introduces a proper separation of concenrns, making your code behaviour more obvious.

    - It is easy to switch between using shortcut ModelSerializer classes and using explicit serializer classes. Any validation behaviour being used for ModelSerializer is simple to replicate.

    - Printing the repr() of a serializer instance will show you exactly what validation rules is applies. There's no extra hidden validation behaviour being called on the model instance. 

    - when you are using ModelSerializer all of this is handled automatically for you. If you want to drop down to using Serializer classes instead, then you need to define the validation rules explicitly.


- Example

```python
   from rest_framework import serializers

   def start_with_s(value):
       if value['0'].lower() != 's':
           raise serializer.ValidationError('Name Should Start with S')
      class StudentSerializer(serializers.Serializer):
          name = serializers.CharField(max_length=100,validators = [start_with_s])
          roll = serializers.IntegerField()
          city = serializers.CharField(max_length=100)
      def validate_roll(self,value):
          if value >= 200:
              raise serializers.ValidationError('seat full')
          return value
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
