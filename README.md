# Fraud Detection API

This is a backend-only Django REST API that identifies and flags potentially fraudulent job applications. The system simulates realistic scenarios using seeded fake data and demonstrates good backend design patterns.

---

## Features

- Built with Django and Django REST Framework (DRF)
- Models: JobPost, Resume, IPAddressLog, JobApplication
- Flags duplicate applications based on job, resume, and IP
- Pagination, filtering, and ordering enabled
- Custom management command for reseeding and flagging
- Shell-tested logic to verify data accuracy
- Aggregated `/api/stats/` endpoint
- Full Docker support
- Clean test coverage with `unittest`
- API-only, no frontend

---

## Quick Start

```bash
# Clone the repo
git clone https://github.com/phkgh/fraud-detection-api.git
cd fraud-detection-api

# Start the project with Docker
docker-compose up --build

# Reseed fresh data and flag duplicates
docker-compose exec web python manage.py reseed_and_flag

# Run API locally at:
# http://localhost:8000/api/jobs/
# http://localhost:8000/api/applications/
# http://localhost:8000/api/stats/
```

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
