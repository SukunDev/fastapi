# FastAPI Project with Pytest (Advanced Setup)

Welcome to your FastAPI + Pytest project setup! This project has been prepared with advanced testing configurations, full CRUD operations, authentication, and structured routing.

---

## Features

- **FastAPI** application structure
- **JWT Authentication** (register and login)
- **User CRUD** (create, read, update, delete)
- **Database:** SQLite (production) + In-memory SQLite (for testing)
- **Testing:** Pytest, Pytest-asyncio, Httpx
- **Dependency Overrides** for clean database during testing
- **Negative Testing** for error handling
- **Full Pydantic v2 Compatibility**

---

## Installation

1. **Clone this repository**

```bash
$ git clone https://github.com/SukunDev/fastapi.git
$ cd fastapi
```

2. **Create and activate virtual environment**

```bash
$ python -m venv venv
$ source venv/bin/activate  # Linux/MacOS
$ venv\Scripts\activate   # Windows
```

3. **Install requirements**

```bash
$ pip install -r requirements.txt
```

4. **Environment Variables**

Create a `.env` file based on `.env.example` and set your env.

---

## Running the Server

```bash
$ fastapi run app/main.py
```

Server will start at: `http://127.0.0.1:8000`

API Documentation available at: `http://127.0.0.1:8000/docs`

---

## Running Tests

### Run All Tests

```bash
$ pytest -v
```

### Run Specific Test File

```bash
$ pytest -v test/test_auth.py
$ pytest -v test/test_user.py
```

### Run Test with Coverage Report

```bash
$ pytest --cov=app
```

### Test Folder Structure

```
test/
  conftest.py         # Fixtures for database and client
  test_auth.py        # Positive test: register and login
  test_user.py        # Positive test: user CRUD
  test_auth_negative.py # Negative test: wrong login, duplicate register
  test_user_negative.py # Negative test: non-existent user operations
```

---

## Testing Overview

| Test File               | Focus                                        |
| :---------------------- | :------------------------------------------- |
| `test_auth.py`          | User register and login success              |
| `test_user.py`          | User CRUD success                            |
| `test_auth_negative.py` | Handle duplicate registration, invalid login |
| `test_user_negative.py` | Handle missing user cases                    |

---

---

## Author

> Sukundev's custom FastAPI stack 🚀

---

Happy coding and testing! 🌟

If you encounter any issues, feel free to open a discussion or reach out.
