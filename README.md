# Fraud Detection API

This is a backend-only Django REST API that identifies and flags potentially fraudulent job applications. The system simulates realistic scenarios using seeded fake data and demonstrates good backend design patterns.

---

## Features

- Built with Django and Django REST Framework (DRF)
- Models: JobPost, Resume, IPAddressLog, JobApplication
- Flags duplicate applications based on job, resume, and IP
- Pagination, filtering, and ordering: Built-in Django REST Framework features for managing large datasets
- Custom management command: reseed_and_flag flushes the database, reseeds data, and injects duplicates intentionally
- Shell-tested logic to verify data accuracy
- Real-time statistics endpoint: /api/stats/ returns key metrics including total and flagged applications
- Dockerized for deployment: PostgreSQL and Django containers
- Unit tests: Covers flagging logic, views, and key behaviors
- API-only, no frontend
- Duplicate detection logic: Flags applications with the same job, resume, and IP combination
- Realistic dataset: 100,000 applications, 50,000 resumes, 5,000 IPs, and 100 jobs seeded using Faker
 

---

**Tech Stack**

    - Python 3.10

    - Django 4.x

    - Django REST Framework

    - PostgreSQL

    - Docker and Docker Compose

    - Faker (Python library)

## Quick Start

```bash
# Clone the repo
git clone https://github.com/phkgh/fraud-detection-api.git
cd fraud-detection-api

# Start the project with Docker
docker-compose up --build

# Reseed fresh data and flag duplicates
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py reseed_and_flag

# Run API locally at:
# http://localhost:8000/api/jobs/
# http://localhost:8000/api/applications/
# http://localhost:8000/api/stats/
```

---

**API Endpoints**

    GET /api/jobs/ — List job posts

    GET /api/resumes/ — List resumes

    GET /api/applications/ — Paginated job applications

    GET /api/stats/ — Real-time summary metrics

---

**Example curl request:**
curl http://localhost:8000/api/stats/

**Example JSON response:**
{
  "total_applications": 100000,
  "unique_jobs": 100,
  "unique_resumes": 50000,
  "flagged_duplicates": 5000
}

---
**Running Tests**
docker-compose exec web python manage.py test
-This command runs unit tests covering flagging logic, statistics endpoint, and application view behavior.

---
**Docker Architecture**

    web: Django backend with Django REST Framework, Faker, and PostgreSQL connector

    db: PostgreSQL service

    Configuration files: .env, Dockerfile, docker-compose.yml

---
## Project Structure

```
fraud-detection-api/
├── api/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── pagination.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   ├── tests_api/
│   │   └── test_applications.py
│   └── management/
│       └── commands/
│           └── reseed_and_flag.py
│
├── fraud_system/
│   ├── __init__.py
│   ├── settings.py
│   └── urls.py
│
├── seed.py
├── sanity_check.py
├── manage.py
├── requirements.txt
├── docker-compose.yml
├── Dockerfile
├── .gitignore
├── LICENSE
└── README.md
```

---

## Author

Hemanth Kumar Pappu
[**@phkgh**](https://github.com/phkgh)
