# Why use Authentication & Permission?

- Currently our API doesn't have any restrictions on who can edit or delete Data. We’d like to have some more advanced behavior in order to make sure that:

- Data is always associated with a creator,

- Only authenticated users may create Data.

- Only the creator of a Data may update or delete it.

- Unauthenticated requests should have run readonly access.

# Authentication

- Authentication is the mechanism of associating an incoming request with a set of identifying credentials, such as the user the request came from, or the token that it was signed with. The permission and throttling policies can then use those credentials to determine if the request should be permitted.

- Authentication is always run at the very start of the View, before the permission and throttling checks occur, and before any other code is allowed to proceed.

- REST framework provides a number of authentication schemes out of the box, and also allows you to implement custom schemes.
  - BasicAuthentication
  - SessionAuthentication
  - tokenAuthentication
  - RemoteUserAuthentication
  - Custom authentication

## BasicAuthentication

- This Authentication scheme uses HTTP Basic Authentication, signed against a user's
  username and password.

- Basic authentication is generally only appropriate for testing.

- If successfully authenticated, BasicAuthentication provides the following credentials.

  - request.user will be a Django User instance.
  - request.auth will be None.

- Unauthenticated responses that are denied permission will result in an HTTP 401 Unauthorized response with an appropriate WWW-Authenticate header. For Example:

```python
WWW-Authenticate:Basic realm="api"
```

> Note: If you use BasicAuthentication in production you must ensure that your API is only available over https. You should also ensure that your API clients will always re-request the username and password at login and will never store those details to persistent storage.

# Permission

- Permissions are used to grant or deny access for different classes of users to different parts of the APl.

- Permission checks are always run at the very start of the View, before any other code is allowed to proceed.

- Permission checks will typically use the authentication information in the request.user and request.auth properties to determine if the incoming request should be permitted.

## Permission Class

- Permissions in REST framework are always defined as a list of permission classes.

  - AllowAny
  - IsAuthenticated
  - IsAdminUser
  - IsAuthenticatedOrReadOnly
  - DjangoModelPermissions
  - DjangoModelPermissionsOrAnonReadOnly
  - DjangoObjectPermission
  - Custom Permission

  ### AllowAny

  - The AllowAny permission class will allow unrestricted access, regardless of if the request was authenticated or unauthenticated,

  - This permission is not strictly required, since you can achieve the same result by using an empty list or tuple for the permissions setting, but you may find it useful to specify this class because it makes the intention explicit.

  ### IsAuthenticated

  - The IsAuthenticated permission class will deny permission to any unauthenticated user. and allow permission otherwise

  - This permission is suitable if you want your API to only be accessible to registered users.

  ### IsAdminUser

  - The IsAdminUser permission class will deny permission to any user, unless user.is_staff is True in which case permission will be allowed.

  - This permission is suitable if you want your API to only be accessible to a subset of trusted administrators.

## Integrating Authentication Globally and locally

```python
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class Stud_ModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class DataModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class St_ModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


```

- if we have more then one classes and we want to add same authentication in all classes then we can easily add it using above way it means locally we can add classes but if we want to add global authentication then we need to add below code to settings.py

```python
REST_FRAMEWORK = {
  'DEFAULT_AUTHENTICATION_CLASSES':['rest_framework.authentication.BasicAuthentication']
  'DEFAULT_PERMISSION_CLASSES':['rest_framework.permissions.IsAuthenticated']
}
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
