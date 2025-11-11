# Task Manager API

A simple RESTful API built with FastAPI for managing tasks. This project demonstrates clean API design, proper HTTP methods, and modern Python development practices.

## 🚀 Features

- ✅ Create, read, update, and delete tasks (CRUD operations)
- ✅ Filter tasks by completion status
- ✅ RESTful API design with proper status codes
- ✅ Input validation using Pydantic models
- ✅ Interactive API documentation (Swagger UI)
- ✅ Fast and lightweight using FastAPI

## 🛠️ Tech Stack

- **Python 3.8+**
- **FastAPI** - Modern web framework for building APIs
- **Pydantic** - Data validation using Python type hints
- **Uvicorn** - ASGI server

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## 🔧 Installation & Setup

1. Clone the repository:
```bash
git clone https://github.com/ky-cx/task-manager-api.git
cd task-manager-api
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python main.py
```

The API will be available at `http://localhost:8000`

## 📚 API Documentation

Once the server is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🎯 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message and API overview |
| GET | `/tasks` | Get all tasks |
| GET | `/tasks?completed=true` | Get completed tasks |
| POST | `/tasks` | Create a new task |
| GET | `/tasks/{id}` | Get a specific task |
| PUT | `/tasks/{id}` | Update a task |
| DELETE | `/tasks/{id}` | Delete a task |

## 📝 Example Usage

### Create a new task:
```bash
curl -X POST "http://localhost:8000/tasks" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Learn FastAPI",
    "description": "Build a REST API project",
    "completed": false
  }'
```

### Get all tasks:
```bash
curl -X GET "http://localhost:8000/tasks"
```

### Update a task:
```bash
curl -X PUT "http://localhost:8000/tasks/1" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Learn FastAPI",
    "description": "Completed the tutorial",
    "completed": true
  }'
```
## 🎬 Quick Demo

Once the server is running, you can test the API:

### Create a task
```bash
curl -X POST "http://localhost:8000/tasks" \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn FastAPI", "description": "Complete the tutorial"}'
```

### Get all tasks
```bash
curl http://localhost:8000/tasks
```

### Update a task
```bash
curl -X PUT "http://localhost:8000/tasks/1" \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn FastAPI", "completed": true}'
```

## 📸 Screenshots

*API Documentation (Swagger UI)*
![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)

## 🧪 Testing
```bash
# Run with test data
python -c "
import requests
response = requests.get('http://localhost:8000')
print(response.json())
"
```

## 🔮 Future Enhancements

- [ ] Add PostgreSQL database persistence
- [ ] Implement user authentication (JWT)
- [ ] Add task categories and tags
- [ ] Deploy to Heroku/Railway
- [ ] Add unit tests with pytest

## 👨‍💻 Author

**Conghui Xu**
- Email: hsuconghui@gmail.com
- LinkedIn: [linkedin.com/in/cx27](https://linkedin.com/in/conghui-xu)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

⭐ If you find this project useful, please consider giving it a star!
