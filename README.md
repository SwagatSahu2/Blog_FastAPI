# Blog API with FastAPI

This is a **Blog API** built using **FastAPI**. It provides endpoints for managing users, blogs, comments, and raw SQL queries. The project uses SQLAlchemy for database interactions and supports authentication with JWT tokens.

---

## Features

- **User Management**:

  - Create users
  - Retrieve user details

- **Blog Management**:

  - Create, update, delete, and retrieve blogs
  - Associate blogs with users

- **Comment Management**:

  - Add, retrieve, and delete comments for blogs

- **Raw SQL Queries**:

  - Execute raw SQL queries for advanced use cases

- **Authentication**:
  - JWT-based authentication for secure access

---

## Project Structure

<pre><code>📁 c:\PythonPract\Blog ├── 📁 app │ ├── __init__.py │ ├── auth.py # Authentication logic │ ├── database.py # Database connection and session management │ ├── hashing.py # Password hashing utilities │ ├── main.py # Entry point for the FastAPI app │ ├── models.py # SQLAlchemy models │ ├── 📁 routers # API routers │ │ ├── blog.py # Blog-related endpoints │ │ ├── comments.py # Comment-related endpoints │ │ ├── login.py # Login endpoint │ │ ├── rawQueries.py # Raw SQL query endpoints │ │ ├── user.py # User-related endpoints │ ├── schemas.py # Pydantic models for request/response validation ├── 📁 sql │ ├── queries.yaml # SQL queries in YAML format ├── 📁 utils │ ├── sql_loader.py # Utility to load SQL queries from YAML ├── .gitignore # Git ignore file ├── requirements.txt # Python dependencies </code></pre>

---

## Installation

### Prerequisites

- Python 3.10 or higher
- SQL Server with a database named `BlogCrudDb`
- ODBC Driver 17 for SQL Server

### Steps

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Blog
   ```
2. Create a virtual environment:
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
3. Install dependencies:
   pip install -r requirements.txt
4. Update the database connection string in
   DATABASE_URL = "mssql+pyodbc://<username>:<password>@<server>/<database>?driver=ODBC+Driver+17+for+SQL+Server&TrustServerCertificate=yes"
5. Run the application:
   uvicorn app.main:app --reload
6. Access the API documentation at:
   Swagger UI: http://127.0.0.1:8000/docs
   ReDoc: http://127.0.0.1:8000/redoc

### Endpoints

1. Authentication
   POST /login: Authenticate and get a JWT token.
2. Users
   POST /user: Create a new user.
   GET /user: Retrieve all users.
   GET /user/{id}: Retrieve a user by ID.
3. Blogs
   POST /blog: Create a new blog.
   GET /blog: Retrieve all blogs.
   GET /blog/{id}: Retrieve a blog by ID.
   PUT /blog/{id}: Update a blog.
   DELETE /blog/{id}: Delete a blog.
4. Comments
   POST /blogs/{blog_id}/comments: Add a comment to a blog.
   GET /blogs/{blog_id}/comments: Retrieve comments for a blog.
   DELETE /comments/{comment_id}: Delete a comment.
5. Raw SQL Queries
   GET /raw/blog-titles: Retrieve blog titles using raw SQL.
   GET /raw/blog-fields: Retrieve specific fields from blogs using raw SQL.
   GET /raw/blog-creator: Retrieve the creator of a blog using raw SQL.
   GET /raw/blogs: Retrieve blogs by user ID using raw SQL.

### License

    This project is licensed under the MIT License. See the LICENSE file for details.

### Contributing

    Contributions are welcome! Please fork the repository and submit a pull request.

### Contact

    For questions or support, contact [swagatsahu687@gmail.com].
