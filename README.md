# Django URL Shortener

## Overview

This is a simple URL shortener application developed using Django. It allows users to submit a long URL and receive a corresponding shortened URL.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/django-url-shortener.git
    cd django-url-shortener
    ```

2. Create a virtual environment and install dependencies:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Apply migrations to create the database:

    ```bash
    python manage.py migrate
    ```

4. Run the development server:

    ```bash
    python manage.py runserver
    ```

5. Access the application at `http://127.0.0.1:8000/shorten/` in your web browser.

## Usage

1. Open the URL shortener web page.

2. Enter a long URL into the provided form.

3. Click the "Shorten URL" button to generate a shortened URL.

4. A success page will display the shortened URL.

## Project Structure

- `shortener/`: Django app containing the URL shortener functionality.
  - `models.py`: Defines the database model for storing long and short URLs.
  - `forms.py`: Contains the form for accepting long URLs.
  - `views.py`: Implements views for handling form submission and URL redirection.
  - `urls.py`: Defines URL patterns for the app.
  - `templates/`: HTML templates for rendering pages.

- `utils.py`: Utility functions, including the generation of short codes.

- `readme.txt`: Documentation file providing an overview, installation instructions, and basic usage information.

## Contributing

Bugra Ilhan, Basak Ozarslan, Ilayda Yagmur Karadag


## Acknowledgments

- Inspired by [Django](https://www.djangoproject.com/) and [Python](https://www.python.org/).

