from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.utils import timezone
from api.models import JobPost, Resume, IPAddressLog, JobApplication
from faker import Faker
import random

fake = Faker()
random.seed(42)

NUM_JOBS = 100
NUM_RESUMES = 50000
NUM_IPS = 5000
NUM_APPLICATIONS = 100000


class Command(BaseCommand):
    help = 'Flush DB, reseed fake data, and flag repeated applications'

    def handle(self, *args, **kwargs):
        self.stdout.write("🚿 Flushing database...")
        call_command("flush", "--noinput")

        self.stdout.write("🛠 Running migrations...")
        call_command("migrate")

        self.stdout.write("🌱 Seeding fresh data...")
        jobs = [JobPost(title=fake.job(), company_name=fake.company())
                for _ in range(NUM_JOBS)]
        JobPost.objects.bulk_create(jobs)
        jobs = list(JobPost.objects.all())

        resumes = [Resume(file_id=f"resume_{i}") for i in range(NUM_RESUMES)]
        Resume.objects.bulk_create(resumes)
        resumes = list(Resume.objects.all())

        ips = [IPAddressLog(ip_address=fake.ipv4()) for _ in range(NUM_IPS)]
        IPAddressLog.objects.bulk_create(ips)
        ips = list(IPAddressLog.objects.all())

        self.stdout.write(
            "📬 Creating job applications and flagging duplicates...")
        seen = set()
        applications = []
        for _ in range(NUM_APPLICATIONS):
            job = random.choice(jobs)
            resume = random.choice(resumes)
            ip = random.choice(ips)
            key = (job.id, resume.id, ip.id)
            is_flagged = key in seen
            seen.add(key)

            applications.append(JobApplication(
                job_post=job,
                resume=resume,
                ip_address=ip,
                timestamp=timezone.now(),
                is_flagged=is_flagged
            ))

        JobApplication.objects.bulk_create(applications, batch_size=1000)
        self.stdout.write(self.style.SUCCESS("✅ Done reseeding and flagging!"))
