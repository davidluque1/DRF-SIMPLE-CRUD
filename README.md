<h1> Description </h1>

Very simple DRF CRUD template for a very simple API.

<h1> Installation </h1>

Requires python >= 3

`git clone https://github.com/davidluque1/DRF-SIMPLE-CRUD.git`

`pip install -r requirements.txt`

Go to https://miniwebtool.com/django-secret-key-generator/

Generate a key. Then go to templateProject/templateProject/settings.py and set the SECRET_KEY variable.

`python manage.py createsuperuser`
`python manage.py runserver`

The server should start, and you should be able to make any of the requests listed below:

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


		


