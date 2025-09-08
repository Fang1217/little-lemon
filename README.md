# Capstone Project - Meta Backend Developer Course

This repository contains the capstone project for the Meta Backend Developer Professional Certificate on Coursera.
The project demonstrates end-to-end backend development skills, including database design, RESTful API implementation, authentication, testing, and deployment.

## Project Overview

The goal of this project is to design and implement a backend system for a fictional application, applying real-world software engineering practices.
It showcases key backend development concepts such as:
- Designing and normalizing relational databases
- Implementing REST APIs with Django
- Managing authentication and authorization
- Writing unit and integration tests
  
## Features
- User registration and authentication (JWT or session-based)
- CRUD operations for application resources
- Role-based access control
- Input validation and error handling
- Pagination and filtering for API endpoints
- Automated testing and CI/CD setup

## Tech Stack
- Language: Python
- Framework: Django / Django REST Framework
- Database: MySQL or SQLite
- Authentication: JWT / Django Auth System
- Testing: Pytest / Django Test Framework
- Version Control: Git & GitHub

## Installation & Setup
Prerequisites
MySQL Server
Python 3.10+
Git

## Steps
```
# Clone the repository
git clone https://github.com/Fang1217/little-lemon.git
cd little-lemon

# Create virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

## Running Tests
python manage.py test

Or if using pytest:
pytest

## Learning Outcomes
Through this capstone, the following skills were demonstrated:
- Designing normalized relational databases
- Building RESTful APIs with Django
- Implementing secure authentication & authorization
- Writing testable, modular backend code
