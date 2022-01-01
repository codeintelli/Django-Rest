# SessionAuthentication

- This authentication scheme uses Django's default session backend for authentication. Session authentication is appropriate for AJAX clients that are running in the same session context as your website.

- lf successfully authenticated. SessionAuthentication provides the Following credentials

- request.user will be a Django User instance.
- request.auth will be None

- unauthenticated responses that are denied permission will be result in an HTTP 403 Forbidden response.

- If you're using an AJAX style API with SessionAuthentication you will need to make sure you include a valid CSRF token for any "unsafe" HTTP method calls, such as PUT, PATCH, POST OR DELETE requests.

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

  ### IsAuthenticatedOrReadOnly

  - The IsAuthenticatedOrReadOnly will allow authenticated users to perform any request, Requests for unauthorized users will only be permitted if the request method is one of the "safe" methods; GET. HEAD or OPTIONS.

  - This permission is suitable if you want to your API to allow read permissions to anonymous users and only write permission to authenticated user.

  ### DjangoModelPermissions

  - This permission class ties into Django's standard django.contrib.auth model permissions. This permission must only be applied to views that have a queryset property set. Authorization will only be granted if the user authenticated and has the relevant model permissions assigned.

    - POST requests require the user to have the add permission on the model.

    - PUT and PATCH requests requires the user to have the change permission on the model.

    - DELETE requests require the user to have the delete permission on the model.

  - The default behaviour can also be overridden to support custom model permissions. For Example, you might want to include a view model permission for GET request.

  - To use custom model permission override DjangoModelPermissions and set the perms_map property.

  ### DjangoModelPermissionsOrAnonReadOnly

  - Similar to DjangoModelPermissions, but also allows unauthenticated users to have read-only access to the API.

# In Browsable API We can enable Login Using builtin login url

- ```python
  import rest_framework
  path('auth/',include('rest_framework.urls', namespace='rest_framework'))
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
