

# CRUD app with Django

This is a simple CRUD (Create, Read, Update, Delete) web application built using the Django web framework. The app allows users to manage a list of products, including adding new products, editing existing products, deleting products, and viewing product details.

## Installation

To run this app locally, you will need to have Python 3 and Django installed on your computer.

1. Clone the repository to your local machine:

```shell

$ git clone https://github.com/your-username/crud-app-django.git
```

2. Change into the project directory:

```shell

$ cd crud-app-django
```

3.  Install the required Python packages:

```shell

$ pip install -r requirements.txt
```

4. Create a new database for the app:

```shell

$ python manage.py migrate
```

Usage

To start the app, run the following command from the project directory:

```shell

$ python manage.py runserver
```

This will start the development server, and you can access the app in your web browser at http://localhost:8000/.

The app has the following features:

- **List view**: Displays a list of all products in the database. Each product is shown with its name, description, and price. The list view supports pagination, so you can navigate through multiple pages of results.
- **Detail view:** Clicking on a product in the list view takes you to the product detail page, which shows additional information about the product, including its SKU and quantity in stock.
- **Create view:** You can add a new product to the database by clicking the "Add Product" button on the list view. This takes you to a form where you can enter the product details.
- **Update view:** To edit an existing product, click the "Edit" button next to the product on the list view. This takes you to a form where you can modify the product details.
- **Delete view:** To delete a product, click the "Delete" button next to the product on the list view. This removes the product from the database.

## API

This app also exposes a REST API for accessing and modifying the list of products. The API supports the following endpoints:

- GET /products/: Returns a paginated list of all products in the database.
- POST /products/: Creates a new product in the database.
- GET /products/:id/: Returns the details of a specific product.
- PUT /products/:id/: Updates the details of a specific product.
- DELETE /products/:id/: Deletes a specific product from the database.

You can use a tool like curl or a REST client like Postman to interact with the API.

Here are some of the examples 

1. Get a paginated list of all products:

```shell
$ curl http://localhost:8000/products/?page=1
```
This will return the first page of products in the database, with a maximum of 10 products per page.

2. Create a new product:

```shell
$ curl -X POST -H "Content-Type: application/json" -d '{"name": "Product 1", "description": "This is the first product", "price": 19.99}' http://localhost:8000/products/

```
This will create a new product with the specified details.

3. Get the details of a specific product:

```shell
$ curl http://localhost:8000/products/1/
```
This will return the details of the product with ID 1.

4. Update the details of a specific product:

``` shell
$ curl -X PUT -H "Content-Type: application/json" -d '{"name": "Updated Product 1", "description": "This is an updated version of the first product", "price": 24.99}' http://localhost:8000/products/1/

```
This will update the details of the product with ID 1.

5. Delete a specific product:

```shell
$ curl -X DELETE http://localhost:8000/products/1/

```
This will delete the product with ID 1 from the database.


## Contributing

If you would like to contribute to this project, feel free to fork the repository and submit a pull request with your changes. Please make sure to write tests for any new functionality and ensure that all existing tests pass.

## License

This project is licensed under the MIT License. See the LICENSE file for details.