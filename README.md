 🔐 Identity-Core-API

A secure REST API built with **FastAPI** that provides user authentication and authorization using **JWT (JSON Web Tokens)**. The project includes user registration, login, role-based access control, password hashing, and PostgreSQL database integration.

---

 🚀 Features

- User Registration
- User Login
- JWT Access Token Authentication
- Refresh Token Support
- Password Hashing
- Role-Based Authorization
- Protected API Endpoints
- PostgreSQL Database Integration
- Alembic Database Migrations
- RESTful API Design

---

 🛠 Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy / SQLModel
- Pydantic
- JWT
- Uvicorn

---

## 📂 Project Structure

```
Identity-Core-API/
│── app/
│   ├── routers/
│   ├── models/
│   ├── schemas/
│   ├── database/
│   
│   ├── auth/
│   └── main.py
│

├── requirements.txt
├── .env
└── README.md
```

---

## ⚙ Installation

### Clone the repository

```bash
git clone <repository-url>
```

### Move into the project

```bash
cd Identity-Core-API
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🗄 Configure Environment Variables

Create a `.env` file and add:

```env
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## ▶ Run the Application

```bash
uvicorn app.main:app --reload
```

---

## 📖 API Documentation

After starting the server, open:

```
http://127.0.0.1:8000/docs
```

Interactive Swagger UI is available for testing all endpoints.

---

## 🔑 Authentication Flow

1. Register a new user.
2. Login using email and password.
3. Receive an Access Token and Refresh Token.
4. Use the Access Token to access protected endpoints.
5. Refresh the Access Token when it expires.

---

## 📌 Main Endpoints

- Register User
- Login User
- Refresh Token
- Get Current User
- Protected Routes
- Admin Routes (Role Based)

---

## 📚 What I Learned

- Building secure REST APIs
- JWT Authentication
- Role-Based Authorization
- Password Hashing
- Database Design
- FastAPI Best Practices
- PostgreSQL Integration

---

## 🎯 Future Improvements

- Email Verification
- Password Reset
- Docker Support
- Redis Token Blacklisting
- Rate Limiting
- Unit Testing
- CI/CD Pipeline

---

## 👨‍💻 Author

**Srisanth Arudra**

If you found this project helpful, feel free to ⭐ the repository.
