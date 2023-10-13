# Flask API

Using Flask to build a Restful API Server with Swagger document.
Integration with Flask-SQLalchemy extensions.

### Extension:
- Restful: [Swagger](http://127.0.0.1:8000/api/)
  
- Web fare_histogram: [fare_histogram](http://127.0.0.1:8000/fare_histogram)

- SQL ORM: [Flask-SQLalchemy](http://flask-sqlalchemy.pocoo.org/2.1/)

## Installation

Install with pip:

```
$ pip install -r requirements.txt
```

## Flask Application Structure 
```
.
|──app.py
|──swagger.yml
| |────templates/
| | |────home.html
| | |────fare-histogram.html

```


## Flask Configuration

##Flask settings
DEBUG = True  # True/False
TESTING = False

##SWAGGER settings
SWAGGER_DOC_URL = '/api'


```

## Run Flask
### Run flask for develop
```
$ python app.py
```

Swagger document page:  `http://127.0.0.1:8000/api`

### Run flask for production


### Run with Docker

```
$ docker build -t flask-example .

$ docker run -p 5000:5000 --name flask-example flask-example 
 

## Reference

Offical Website

- [Flask](http://flask.pocoo.org/)
- [Flask Extension](http://flask.pocoo.org/extensions/)
