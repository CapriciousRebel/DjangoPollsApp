(These notes are for personal reference, however, feel free to use them :)

## Python project Setup

### Setup when the repo is cloned(Do While):

- Create Virtual Env: `python3 -m venv venv`
- Activate Virtual Env: `source venv/bin/activate`
- Update pip: `pip install --upgrade pip`
- Install dependencies: `pip install -r requirements.txt`

### Initial Setup(Do Once):

- Create a Virtual Environment: `python3 -m venv venv`
- Initialize the Virtual Environment: `source venv/bin/activate`
- Update pip: `pip install --upgrade pip`
- Install django in venv: `pip install django`
- Install psycopg2 in venv: `pip install psycopg2`

### Dependencies management

- Create requirements.txt: `touch requirements.txt`
- Freeze the dependencies: `pip freeze > requirements.txt`

## Django Project Setup

### Setup when project is ready(Do While):

- Run development server: `python manage.py runserver <ip address>:<port number>`
- Make migrations: `python manage.py makemigrations <app name>`
- Migrate: `python manage.py migrate`

### Initial Setup(Do Once):

- Create the project: `django-admin startproject <project name>`
- Create the app: `python manage.py startapp <app name>`
- Create a superuser(Admin): `python manage.py createsuperuser`

### Django jargons:

1. Architecture:
Django has a MTV(Models - Templates - Views) architecture, which is like(Not really) the MVC(Models - Views - Controllers) architecture where, [Models = Models, Templates = Views, Views = Controllers]
<br>
<pre>
                    (Server-Side)                                             (client-side)
+---------------------------------------------------+                       +-----------+ 
|                              +----+    +-------+  |                       |           | 
|                              |    | <--|urls.py| <---[HTTP Request]-----  |           |
| +--------+     +-----+       |    |    +-------+  |                       |           |
| |Database| <-> |Model|  <->  |    | -----------------[HTTP Response]--->  |           | 
| +--------+     +-----+       |View|               |                       |  Browser  |
|                              |    |               |                       |           |
|              +---------+     |    |               |                       |           |
|              |Templates| <-> |    |               |                       |           |
|              +---------+     +----+               |                       |           |
+---------------------------------------------------+                       +-----------+
</pre>

<pre>

+---------+                               +----------------+      +----------------+      +--------+
|         |                               |  (url router)  |      |  (url router)  |      |        |
|         |-----[url: /app/something]---> | mysite/urls.py |----->|   app/urls.py  |----> |  View  | 
| Browser |                               +----------------+      +----------------+      |        |
|         |                                                                               |        |
|         | <-------------------------[Template]----------------------------------------- |        |
+---------+                                                                               +--------+
</pre>

- In polls/urls.py

```
path('<int:question_id>/', views.detail, name='detail'),

<int:question_id> captures the question id, and passes it to the detail() function which is a view.
It calls detail(request=<HttpRequest object>, question_id=<question_id>)
```
