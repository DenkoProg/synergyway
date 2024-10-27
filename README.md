# **User Data Fetcher with Celery and Django**

This application extracts user information from external APIs, enriches it with address and credit card data, and stores it in a PostgreSQL database. The tasks are executed asynchronously using Celery, allowing background processing. The project is containerized with Docker for easy deployment.

## **Features**

- Extracts user data from the [JSONPlaceholder API](https://jsonplaceholder.typicode.com/).
- Fetches address and credit card data from the [Random Data API](https://random-data-api.com/).
- Asynchronous background processing with Celery.
- Periodic task execution with Celery Beat.
- Containerized with Docker for easy setup and deployment.
- Includes unit tests using pytest.
- Can be extended for AWS deployment.

## **Project Structure**

- **Django**: Main framework for the web application.
- **Celery**: Asynchronous task queue for background processing.
- **Docker**: Containerization for development and deployment.
- **PostgreSQL**: Database for storing user, address, and credit card data.
- **pytest**: Testing framework.
- **Flake8**: Python linter for code quality.

## **Installation and Setup**

### **1. Prerequisites**

Ensure you have the following installed:
- Docker and Docker Compose
- Python 3.8+ (if running locally)
- Redis (if running locally)

### **2. Clone the Repository**

```bash
git clone <repository-url>
cd <project-directory>
```

### **3. Environment Variables**

Create a `.env` file in the project root with the following environment variables:

```env
DJANGO_SECRET_KEY=your_secret_key
DJANGO_DEBUG=True
DATABASE_NAME=synergyway
DATABASE_USER=postgres
DATABASE_PASSWORD=postgres
DATABASE_HOST=db
DATABASE_PORT=5432
CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://redis:6379/0
```

### **4. Build and Run the Docker Containers**

Build and start the containers using Docker Compose:

```bash
docker-compose up --build
```

This command will start the following containers:
- **web**: Django and Celery application container.
- **db**: PostgreSQL database container.
- **redis**: Redis broker container for Celery.
- **celery-beat**: Celery Beat container for periodic tasks.
- **celery-worker**: Celery worker container for executing tasks.

### **5. Run Migrations**

To apply database migrations:

```bash
docker-compose run web python manage.py migrate
```

### **6. Create a Superuser (Optional)**

To access the Django admin panel, create a superuser:

```bash
docker-compose run web python manage.py createsuperuser
```

You can then log in at [http://localhost:8000/admin](http://localhost:8000/admin).

### **7. Run Celery Workers**

Start the Celery worker:

```bash
docker-compose run web celery -A UserDataEnricher worker --loglevel=info
```

To start Celery Beat for periodic tasks:

```bash
docker-compose run web celery -A UserDataEnricher beat --loglevel=info
```

### **8. Run Tests**

To run the tests using pytest:

```bash
docker-compose run web pytest
```

### **9. View Data**

You can view the stored data in the Django admin panel at [http://localhost:8000/admin](http://localhost:8000/admin) after creating a superuser.

## **Project Configuration**

### **Celery Configuration**

- **Celery Workers:** Celery workers are configured to execute asynchronous tasks for fetching user, address, and credit card data.
- **Celery Beat:** Periodic tasks are scheduled using Celery Beat, allowing automated fetching at regular intervals.
- **Broker and Backend:** Redis is used as both the broker and result backend for Celery.

### **Docker Configuration**

- **Docker Compose:** The project uses Docker Compose to manage services (web, db, redis).
- **Dockerfile:** The Dockerfile builds the Django-Celery application container.

## **Code Quality**

### **Linting**

The project uses Flake8 for linting. Run the linter as follows:

```bash
docker-compose run web flake8 .
```

## **Deployment on AWS (Optional)**

To deploy the application on AWS, consider using:
- **Elastic Beanstalk** or **ECS** for containerized deployment.
- **RDS** for PostgreSQL as the database service.
- **ElastiCache** for Redis as the Celery broker and backend.
- Set up an S3 bucket for static and media file storage.

## **Contributing**

If you wish to contribute to this project:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.
