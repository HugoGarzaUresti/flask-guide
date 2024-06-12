# Spring Boot (Flask Equivalent)

This guide demonstrates how to create a simple web application using Flask, a lightweight web framework for Python.

## Requirements

- Python 3.x
- `Flask` library

## Setup

1. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

2. Run the application:
    ```sh
    python run.py
    ```

## Code Explanation

### `app/__init__.py`

This module contains the Flask application.

- **`app`**: An instance of the Flask class.
- **`home`**: A route that returns a simple greeting.

### `run.py`

This script serves as the entry point for the application. It calls the `main` function to start the Flask server.

## Additional Information

- Flask is a lightweight web framework that is easy to set up and use for simple web applications.
- You can add more routes and functionality to the Flask app as needed.
