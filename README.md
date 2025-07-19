# FastAPI Simple App

A simple FastAPI application built as an educational project to learn modern Python web development practices.

## What This Project Covers

This project demonstrates several key concepts in modern Python web development:

- **FastAPI Framework**: Building REST APIs with automatic documentation
- **SQLAlchemy**: Database ORM with async support
- **Repository Pattern**: Clean separation of data access logic
- **Pydantic Models**: Data validation and serialization
- **Dependency Injection**: Using FastAPI's dependency system
- **Async/Await**: Modern Python async programming

## Project Structure

```
fastapi-simple-app/
├── main.py          # FastAPI application entry point
├── router.py        # API route definitions
├── repository.py    # Data access layer
├── schemas.py       # Pydantic models
├── database.py      # Database configuration
└── requirements.txt # Python dependencies
```

## Getting Started

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd fastapi-simple-app
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   uvicorn main:app --reload
   ```

5. **Access the API**
   - API: http://localhost:8000
   - Interactive docs: http://localhost:8000/docs
   - Alternative docs: http://localhost:8000/redoc

## API Endpoints

- `POST /tasks` - Create a new task
- `GET /tasks` - Retrieve all tasks

## Database

The application uses SQLite with async support. The database file (`tasks.db`) is created automatically when you first run the application.

## Learning Goals

This project serves as a hands-on learning experience for:
- Understanding FastAPI's async capabilities
- Implementing clean architecture patterns
- Working with modern Python type hints
- Building RESTful APIs with automatic documentation

Feel free to explore the code, make changes, and experiment with different patterns!
