<h1> Description </h1>

Uses Django 2.2.10 and Django REST Framework 3.11.0

Very simple DRF CRUD template with a very simple API. Creates and runs a server with Django and Django REST framework.

<h1> Installation </h1>

Requires python >= 3

`git clone https://github.com/davidluque1/DRF-SIMPLE-CRUD.git`
`python3 -m venv venv`
`. venv bin/activate`
`pip install -r requirements.txt`

Go to https://miniwebtool.com/django-secret-key-generator/

Generate a key. Then go to templateProject/templateProject/settings.py and set the SECRET_KEY variable.

Now, run:

`python manage.py migrate --run-syncdb`

`python manage.py createsuperuser`

`python manage.py runserver`


The server should start, and you should be able to make any of the requests listed in the Endpoints section below:


<h1> Endpoints </h1>

(id) = 1, 2, 3... (default Django Models primary key)


<h3>Get:</h3> localhost:8000/api/graphics-cards/(id)/
	
	
	
	
	
<h3>Get all:</h3> localhost:8000/api/graphics-cards/





<h3>Post:</h3> localhost:8000/graphics-cards/

body:
```json
      {
        "manufacturer": "nvidia",
        "model": "gtx-1080",
        "minimumWatts": 500.0
      }
```
	
	
	
	
<h3>Put:</h3> localhost:8000/api/graphics-cards/(id)/

body: 
```json
    
      {
        "manufacturer": "nvidia",
        "model": "gtx-1080",
        "minimumWatts": 500.0
      }
```




<h3>Delete:</h3> localhost:8000/graphics-cards/(id)/


		


