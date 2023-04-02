# crud_app

This is a basic CRUD App written in Django 


This is how to use it. 

1. Install all the dependncies from requirements.txt 

``` cmd 
pip install -r requirements.txt 
````

2. Start Django serevr from crud_app folder 

``` cmd 
python.exe .\manage.py runserver
```
3. Navigate to http://127.0.0.1:8000/ in your browser to access the app 

## This is how to access REST API 

```markdown 

# GET a list of all products
curl http://localhost:8000/products/

# GET details of a specific product
curl http://localhost:8000/products/1/

# POST a new product
curl -X POST http://localhost:8000/products/ -d '{"name": "New Product", "description": "A new product", "price": 9.99}' -H "Content-Type: application/json"

# PUT (update) an existing product
curl -X PUT http://localhost:8000/products/1/ -d '{"name": "Updated Product", "description": "An updated product", "price": 14.99}' -H "Content-Type: application/json"

# DELETE an existing product
curl -X DELETE http://localhost:8000/products/1/

# paginated REST calls 

curl http://localhost:8000/products/\?page=1


```