# ALX Travel App

A Django-based travel listing platform with RESTful API, MySQL database integration, and comprehensive API documentation using Swagger.

## Features

- **Django REST Framework** for building robust APIs
- **MySQL** database for data persistence
- **Swagger/OpenAPI** documentation via drf-yasg
- **CORS** support for cross-origin requests
- **Celery** integration for background tasks
- **Environment-based** configuration using django-environ
- **Production-ready** project structure

## Prerequisites

- Python 3.8+
- MySQL 5.7+ or MariaDB 10.3+
- RabbitMQ (for Celery tasks)
- Git

## Project Structure

```
alx_travel_app/
├── alx_travel_app/          # Main project directory
│   ├── __init__.py
│   ├── settings.py          # Project settings with environment variables
│   ├── urls.py              # Main URL configuration with Swagger
│   ├── wsgi.py
│   └── asgi.py
├── listings/                # Listings app
│   ├── __init__.py
│   ├── admin.py            # Django admin configuration
│   ├── apps.py             # App configuration
│   ├── models.py           # Database models
│   ├── serializers.py      # DRF serializers
│   ├── views.py            # API views
│   ├── urls.py             # App URL patterns
│   └── migrations/         # Database migrations
├── requirements.txt         # Project dependencies
├── .env.example            # Environment variables template
├── .gitignore              # Git ignore file
├── manage.py               # Django management script
└── README.md               # Project documentation
```

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/alx_travel_app.git
   cd alx_travel_app
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   
   # On Linux/Mac
   source venv/bin/activate
   
   # On Windows
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and update with your configuration:
   - `SECRET_KEY`: Django secret key
   - `DB_NAME`: MySQL database name
   - `DB_USER`: MySQL username
   - `DB_PASSWORD`: MySQL password
   - `DB_HOST`: MySQL host (default: localhost)
   - `DB_PORT`: MySQL port (default: 3306)

5. **Create MySQL database**
   ```sql
   CREATE DATABASE alx_travel_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```

6. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

8. **Collect static files (for production)**
   ```bash
   python manage.py collectstatic
   ```

## Running the Application

### Development Server
```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000/`

### Running Celery Worker (Optional)
```bash
celery -A alx_travel_app worker -l info
```

### Running Celery Beat (Optional)
```bash
celery -A alx_travel_app beat -l info
```

## API Documentation

Swagger documentation is automatically available at:
- **Swagger UI**: `http://localhost:8000/swagger/`
- **ReDoc**: `http://localhost:8000/redoc/`
- **OpenAPI Schema (JSON)**: `http://localhost:8000/swagger.json`
- **OpenAPI Schema (YAML)**: `http://localhost:8000/swagger.yaml`

## API Endpoints

### Listings
- `GET /api/listings/` - List all listings
- `POST /api/listings/` - Create a new listing (requires authentication)
- `GET /api/listings/{id}/` - Retrieve a specific listing
- `PUT /api/listings/{id}/` - Update a listing (requires authentication)
- `PATCH /api/listings/{id}/` - Partially update a listing (requires authentication)
- `DELETE /api/listings/{id}/` - Delete a listing (requires authentication)
- `GET /api/listings/active/` - Get all active listings
- `GET /api/listings/my_listings/` - Get listings created by current user

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key | Required |
| `DEBUG` | Debug mode | `True` |
| `ALLOWED_HOSTS` | Allowed hosts list | `localhost,127.0.0.1` |
| `DB_NAME` | MySQL database name | `alx_travel_db` |
| `DB_USER` | MySQL username | `root` |
| `DB_PASSWORD` | MySQL password | Required |
| `DB_HOST` | MySQL host | `localhost` |
| `DB_PORT` | MySQL port | `3306` |
| `CORS_ALLOWED_ORIGINS` | CORS allowed origins | `http://localhost:8000` |
| `CELERY_BROKER_URL` | Celery broker URL | `amqp://guest:guest@localhost:5672//` |

## Development Guidelines

### Code Style
- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings to all classes and functions

### Git Workflow
1. Create feature branches from `main`
2. Make atomic commits with clear messages
3. Create pull requests for code review
4. Merge after approval

### Testing
```bash
python manage.py test
```

## Troubleshooting

### MySQL Connection Error
- Ensure MySQL service is running
- Verify database credentials in `.env`
- Check if database exists

### Migration Issues
```bash
python manage.py makemigrations --empty listings
python manage.py migrate --fake-initial
```

### Static Files Not Loading
```bash
python manage.py collectstatic --noinput
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

