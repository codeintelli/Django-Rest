# TokenAuthentication

- This authentication scheme uses a simple token-based HTTP authentication scheme. Token authentication is appropriate for client-server setups such as native desktop and mobile clients.

- To use the tokenAuthentication scheme you will need to configure the authentication classes to include TokenAuthentication and additional include rest_framework.authtoken in your INSTALLED_APPS setting:

```python

INSTALLED_APPS = [
  ...
  'rest_framework.authtoken',
]

```

- if successfully authenticated, TokenAuthentication provides the following credentials.

- request.user will be a django user instance.

- request.auth will be a rest_framework.authtoken.models.Token instance.

- Unauthenticated responses that are denied permission will result in an HTTP 401 Unauthorized response with an appropriate WWW-Authenticate header. For example:

> WWW-Authenticate:Token

- The http command line tool may be useful for testing token authenticated APIs. For example:

> http://127.0.0.1:8000/studentapi/'Authorization:Token9944b09199c62bcf9418ad846dd0ebbfc6ee4b'

> If you use TokenAuthentication in production you must ensure that your API is only available over http.

## Generate Token

- Using Admin application
- Using Django manage.py command

  - python manage.py drf_create_token <username>: This command will return API Token for the given user or creates a Token if token dosen't exist for user.

- By exposing an API endpoint.
- Using signals

## How Client can Ask/Create Token

- when using TokenAuthentication you may want to provide a mechanism for client obtain a token given the username and password.

- REST framework provides a built-in view to provide this behavior. To use it, add the obtain_auth_token view to your URLconf:

```python
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
  path('gettoken/',obtain_auth_token)
]
```

- The obtain_auth_token view will return a JSON response when valid username and password field are posted to the view using from data or JSON:

> http POST https://localhost:8000/gettoken/username="name"password="pass"{'token':'9944b09199c62bcf9418ad846dd0ebbfc6ee4b'}

# httpie

- HTTPie (pronounced aitch-tee-tee—pie) is a command line HTTP client. its goal is to make CLl interaction with web services as human-friendly as possible, It
  provides a simply http command that allow for sending arbitrary HTTP requests using u simple and natural syntax, and displays colorized output, HTTPie can be used for testing. debugging. and generally Interacting with HTTP servers.

Syntax:-

```sh
 http[flags][METHOD]URL[ITEM[ITEM]]
```

## How To Install

> pip install httpie

## Use httpie

GET Request

> http://localhost:8000/studentapi

GET Request With Auth

> http://127.0.0.1:8000/studentapi/'Authorization:Token9944b09199c62bcf9418ad846dd0ebbfc6ee4b'

POST Request /Submitting Form

> http://127.0.0.1:8000/studentapi/name="jay"roll"104"city="aaa"'Authorization:Token9944b09199c62bcf9418ad846dd0ebbfc6ee4b'

PUT Request

> http://127.0.0.1:8000/studentapi/4/name="jay"roll"104"city="aaa"'Authorization:Token9944b09199c62bcf9418ad846dd0ebbfc6ee4b'

DELETE Request

> http://127.0.0.1:8000/studentapi/4/'Authorization:Token9944b09199c62bcf9418ad846dd0ebbfc6ee4b'

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
