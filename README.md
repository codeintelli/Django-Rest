# Django REST Framework


![](https://res.cloudinary.com/practicaldev/image/fetch/s--MfVqWnwL--/c_imagga_scale,f_auto,fl_progressive,h_900,q_auto,w_1600/https://thepracticaldev.s3.amazonaws.com/i/pgwkazyf2b5q8kqzxzda.jpg)

Django REST framework is a powerful and flexible toolkit for building Web APIs.

Some reasons you might want to use REST framework:

- The Web browsable API is a huge usability win for your developers.
- Authentication policies including packages for OAuth1a and OAuth2.
- Serialization that supports both ORM and non-ORM data sources.
- Customizable all the way down - just use regular function-based views if you don't need the more powerful features.
- Extensive documentation, and great community support.
- Used and trusted by internationally recognised companies including Mozilla, Red Hat, Heroku, and Eventbrite.


## Folder Structure

Enter into the folder and view Readme from that you can find all information about specific module 

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
- Clone this repo

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

