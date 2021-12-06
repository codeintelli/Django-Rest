# ModelSerializer Class in Django REST Framework

- The ModelSerializer class provides a shortcut that lets you automatically create a serializer class with field that correspond to the model field.

- The ModelSerializer class is same as a regular serializer class, expect that:
  - It will automatically generate a set of field for you, based on the model.
  - It will automatically generate validators for the serializer class such as unique together validators.
  - It includes simple default implementations of create() and update()

### Create ModelSerializer class

- Create a separate serializers.py file to write all serializers

- Example

```python
   from rest_framework import serializers
      class StudentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Student
            fields = ['id','name','roll','city']

        fields = '__all__'
        exclude = ['roll']
```


### Validation in ModelSerializer Class

- Here if we want to put argument or put any specific validation in our model and we can choose name for example so we need to write name explicitly and put validation on it.

- read only means they can't be updated once they have inserted in database

- Example

```python
   from rest_framework import serializers
      class StudentSerializer(serializers.ModelSerializer):
        name = serializers.CharField(read_only=True)
        # for specific fields
        class Meta:
            model = Student
            fields = ['id','name','roll','city']
```

## or

```python
   from rest_framework import serializers
      class StudentSerializer(serializers.ModelSerializer):

        class Meta:
            model = Student
            fields = ['id','name','roll','city']
            read_only_fields = ['name','roll']
            # for multiple fields
```

- Now we can also give more then one validation to any specific fields

```python
   from rest_framework import serializers
      class StudentSerializer(serializers.ModelSerializer):

        class Meta:
            model = Student
            fields = ['id','name','roll','city']
            extra_kwargs = {'name':{'read_only':True,'required':True}}
```

- Now, can we use Field level validation, Object level validation, validator in ModelSerializer Class?

  - yes we can use these validation in our ModelSerializers.

  - Example:- (Field Level Validation)

    ```python
    from rest_framework import serializers
        class StudentSerializer(serializers.ModelSerializer):

            class Meta:
                model = Student
                fields = ['id','name','roll','city']
            def validate_roll(self,value):
                if value >= 200:
                    raise serializers.ValidationError('seat full')
                return value
    ```

    - you just need to put function as we put in [Validation](https://github.com/CodeIntelli/Django-Rest/tree/main/3.%20Validation)

    - Example:- (Object Level Validation)

    ```python
    from rest_framework import serializers
        class StudentSerializer(serializers.ModelSerializer):

            class Meta:
                model = Student
                fields = ['id','name','roll','city']

            def validate(self,data):
                nm = data.get('name')
                ct = data.get('city')
                if nm.lower() == 'rohit' and ct.lower() != 'ranchi':
                    raise serializers.ValidationError('City must be ranchi')
                return data
    ```

    - Example:- (Validator)

    ```python
    from rest_framework import serializers

    class StudentSerializer(serializers.ModelSerializer):
        def start_with_s(value):
            if value['0'].lower() != 's':
            raise serializer.ValidationError('Name Should Start with S')
        name = serializers.CharField(validators=[start_with_s])
        class Meta:
            model = Student
            fields = ['id','name','roll','city']
    ```

## Setup

> Note: For better view in VS Code Install Better Comments Extension

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

- [Django Function Based API](https://github.com/CodeIntelli/DJANGO-RESTFULL-API_FBV)
- [Django Class Based API](https://github.com/CodeIntelli/DJANGO-RESTFULL-API_CBV)
