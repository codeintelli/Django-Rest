# Serializer And Serialization

## Python JSON:-

- Python json has a built in package called json which is used to work with json data.
- Basically it provides us two functions

  - Dumps(data):- this is used to convert python obj into json string

  ```python
  import json
  python_data = {‘name’:’sonam’,’roll’:101}
  json_data = json.dumps(python_data)
  print(Json_data)
  # {"name":"sonam","roll":"101"}
  ```

  - Loads(data):- this is used to parse json string

  ```python
  import json
  Json_data = {"name":"sonam","roll":’’101’’}
  parsedData = json.loads(json_data)
  print(parsedData)
  {'name':'sonam','roll':'101'}
  ```

# Serializers:-

- In Django REST framework serializer are responsible for converting complex data such as querysets and model instances to native python datatypes(called serialization) that can be easily rendered into JSON,XML or other content types which is understandable by Frontend.

- Serializers in Django REST Framework are responsible for converting objects into data types understandable by javascript and front-end frameworks. Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data. The serializers in REST framework work very similarly to Django’s Form and ModelForm classes. The two major serializers that are most popularly used are ModelSerializer and HyperLinkedModelSerialzer.

- Serializers are also responsible for deserialization which means It allows parsed data to be converted back into complex types after validating the incoming data.
