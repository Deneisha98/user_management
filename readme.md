# User Management System
## Overview
This project implements a User Management System using FastAPI, SQLAlchemy, and PostgreSQL. It supports user profile management, professional status upgrades, role-based access control, and full API documentation. The system is containerized using Docker and follows a CI/CD pipeline via GitHub Actions.

---

## Features

### User Profile Management
- Users can update their profile fields: first_name, last_name, bio, location, etc.
- Managers and Admins can upgrade users to **Professional Status**.
  
### Role-Based Access Control

- Roles: ANONYMOUS, AUTHENTICATED, MANAGER, and ADMIN.
  
### API Documentation
Integrated Swagger UI for API testing and documentation at:
- **Swagger UI**: http://localhost:8000/docs
  
### Database
- PostgreSQL with SQLAlchemy ORM.
- Alembic for database migrations.
  
---
## Setup Instructions

### Prerequisites  
- Docker and Docker Compose  
- Python 3.10+  
- PostgreSQL  

### Installation  

1.**Clone the repository**  
   git clone https://github.com/Deneisha98/user_management.git
   cd user_management
2.**Set up environment variables**
    cp .env.sample .env
3.**Start the application**
  docker compose up --build
4.**Access the API**
  -Swagger UI: http://localhost:8000/docs
  -PgAdmin: http://localhost:5050
    -Default credentials: admin@example.com / adminpassword
### Tests

#### Running Tests
To execute all tests using **Pytest**, run the following command:
pytest

### List of Tests Added
- test_lock_unlock_account
Verifies locking and unlocking a user account.

- test_professional_status_update
Tests updating a user's professional status.

- test_invalid_user_missing_required_fields
Ensures required fields validation for user creation.

- test_email_uniqueness_constraint
Prevents duplicate email entries in the database.

- test_empty_fields_rejected
Ensures that empty fields are not accepted during user updates.

- test_user_profile_update
Validates that users can successfully update their profile fields.

- test_invalid_uuid_rejected
Ensures the API rejects invalid UUID formats for user_id.

- test_duplicate_email_rejected
Verifies that duplicate email addresses are rejected.

- test_role_validation
Ensures only valid roles (ANONYMOUS, AUTHENTICATED, MANAGER, ADMIN) can be assigned.

- test_professional_status_timestamp
Tests that the professional status timestamp updates correctly when a user's status is upgraded.

### Known QA Issues

The following QA issues were identified and resolved:

1. API does not validate UUID format for user_id
2. Missing Role Validation
3. Professional Status Timestamp Missing
4. Empty Fields Accepted
5. Duplicate Email Allowed

### CI/CD Pipeline

The project uses GitHub Actions for continuous integration and deployment.

Pipeline Steps:
1. Testing:
Runs the Pytest suite to ensure all tests pass.

2. Build and Push Docker Image:
Builds the Docker image and pushes it to DockerHub.

3. Security Scan:
Scans the Docker image for vulnerabilities using Trivy.

### Deployment
The application can be deployed locally or via DockerHub.

#### Run Locally:
To run the application locally:

uvicorn app.main:app --reload

Access the API documentation at:
http://localhost:8000/docs

#### Docker Deployment:
Pull the Docker image:

docker pull deneisha98/user_management:latest

Run the Docker container:
docker run -p 8000:8000 deneisha98/user_management:latest

### Access the API at:
http://localhost:8000/docs

### Reflection Document
For an overview of the project, QA issues, and testing strategy, please take a look at the Reflection Document.