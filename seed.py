import os
import sys
import django
import random
from datetime import datetime, timedelta
from faker import Faker

# Setup Django first
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fraud_system.settings")
django.setup()

fake = Faker()
random.seed(42)

NUM_JOBS = 100
NUM_RESUMES = 50000
NUM_IPS = 5000
NUM_APPLICATIONS = 100000


def create_jobs(JobPost):
    print("Creating jobs...")
    jobs = [JobPost(title=fake.job(), company_name=fake.company())
            for _ in range(NUM_JOBS)]
    JobPost.objects.bulk_create(jobs)


def create_resumes(Resume):
    print("Creating resumes...")
    resumes = [Resume(file_id=f"resume_{i}") for i in range(NUM_RESUMES)]
    Resume.objects.bulk_create(resumes)


def create_ips(IPAddressLog):
    print("Creating IPs...")
    ips = [IPAddressLog(ip_address=fake.ipv4()) for _ in range(NUM_IPS)]
    IPAddressLog.objects.bulk_create(ips)


def create_applications(JobPost, Resume, IPAddressLog, JobApplication):
    print("Creating applications...")
    jobs = list(JobPost.objects.all())
    resumes = list(Resume.objects.all())
    ips = list(IPAddressLog.objects.all())

    applications = []
    for _ in range(NUM_APPLICATIONS):
        job = random.choice(jobs)
        resume = random.choice(resumes)
        ip = random.choice(ips)
        from django.utils import timezone
        timestamp = timezone.make_aware(
            fake.date_time_between(start_date='-30d', end_date='now'))

        applications.append(JobApplication(
            job_post=job,
            resume=resume,
            ip_address=ip,
            timestamp=timestamp
        ))
    JobApplication.objects.bulk_create(applications, batch_size=1000)


def run(JobPost, Resume, IPAddressLog, JobApplication):
    if JobApplication.objects.exists():
        print("Already seeded. Skipping.")
        return
    create_jobs(JobPost)
    create_resumes(Resume)
    create_ips(IPAddressLog)
    create_applications(JobPost, Resume, IPAddressLog, JobApplication)
    print("Done.")


if __name__ == '__main__':
    from api.models import JobPost, Resume, IPAddressLog, JobApplication
    run(JobPost, Resume, IPAddressLog, JobApplication)
