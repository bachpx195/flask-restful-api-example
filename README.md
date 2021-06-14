# flask-restful-api-example

Book: https://learning.oreilly.com/library/view/building-rest-apis/9781484250228/A479840_1_En_1_Chapter.html 

 
### Chap 1: Beginning with Flask

Setup

- Check ENV path

```bash
which python
```
- Start app

```bash
FLASK_APP=app.py flask run 
```


### Chap 2: Database Modeling in Flask

- `Flask-SQLAlchemy` is an extension for flask which adds support for SQLAlchemy to the application. SQLAlchemy is a Python toolkit and *Object Relational Mapper* that provides access to the SQL database using Python. SQLAlchemy comes with enterprise-level persistence patterns and efficient and high performing database access

- `PyMySQL` SQLAlchemy uses MySQL-Python as the default DBAPI for connecting with MySQL. `PyMySQL` to enable MySQL connection with Flask-SQLAlchemy

- `flask-marshmallow` In order to serve JSON response from our API using the data returned by SQLAlchemy, we need another library called marshmallow which is an add-on to SQLAlchemy to serialize SQLAlchemy-returned data objects to JSON.

- Error: https://stackoverflow.com/questions/57984649/marshmallow-object-has-no-attribute-modelschema
