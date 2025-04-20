# Fraud Detection API

This is a backend-only Django REST API designed to detect duplicate or fraudulent job applications. It demonstrates strong backend engineering practices including:

- **100,000 applications** seeded using realistic Faker data
- **Flagging logic** for repeated applications by the same resume/IP to the same job
- **Read-optimized endpoints** for job posts, resumes, IP logs, and applications
- **Pagination, filtering, and ordering**
- **Custom stats endpoint** for summary metrics
- **Custom Django management command** to reseed and reflag data
- **Unit tests** for key business logic
- **Dockerized setup** for easy deployment and reproducibility

## Quick Start

```bash
git clone https://github.com/phkgh/fraud-detection-api.git
cd fraud-detection-api
docker-compose up --build
```

Then access:

- [http://localhost:8000/api/jobs/](http://localhost:8000/api/jobs/)
- [http://localhost:8000/api/applications/](http://localhost:8000/api/applications/)
- [http://localhost:8000/api/stats/](http://localhost:8000/api/stats/)

**Project Structure:**

## Project Structure

.
├── api/
 │   ├── **init**.py
 │   ├── admin.py
 │   ├── apps.py
 │   ├── models.py
 │   ├── pagination.py
 │   ├── serializers.py
 │   ├── urls.py
 │   ├── views.py
 │   ├── tests_api/
 │   │   └── test_applications.py
 │   ├── management/
 │   │   └── commands/
 │   │       └── reseed_and_flag.py
├── fraud_system/
 │   ├── **init**.py
 │   ├── settings.py
 │   ├── urls.py
├── seed.py
├── sanity_check.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
├── LICENSE

**Author:**

phkgh
