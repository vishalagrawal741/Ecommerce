# E-commerce Application

This is a fully functional e-commerce application built using Django for the backend and HTML, CSS, and JavaScript for the frontend. The project was developed as part of a team e-learning project, with a focus on the front-end implementation.

## Features

- **User Authentication**: Secure user login and registration system.
- **Product Catalog**: Display of products with details, images, and pricing.
- **Product Management**: Admin interface for adding, updating, and deleting products.
- **Shopping Cart**: Users can add products to the cart and proceed to checkout.
- **Responsive Design**: Ensures compatibility across various devices and screen sizes.

## Technologies Used

- **Frontend**:
  - HTML
  - CSS
  - JavaScript

- **Backend**:
  - Django
  - SQLite (as the database)

## Project Structure

ecommerce/
├── catalog/
│ ├── migrations/
│ ├── templates/
│ │ └── catalog/
│ │ ├── index.html
│ │ └── index2.html
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
├── ecommerce/
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── media/
│ └── products/
│ ├── Iphone.jpg
│ ├── OIP.jpeg
│ ├── RR_car.jpg
│ └── Screenshot_2024-07-19_155403.png
├── db.sqlite3
└── manage.py


## Setup Instructions

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/ecommerce.git
    ```
2. **Navigate to the project directory**:
    ```sh
    cd ecommerce
    ```
3. **Install the required dependencies**:
    ```sh
    pip install -r requirements.txt
    ```
4. **Apply migrations**:
    ```sh
    python manage.py migrate
    ```
5. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

## Contributions

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
