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
DUPLICATE_RATIO = 0.05  # 5% of applications will be duplicates


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

        self.stdout.write("📬 Creating job applications with 5% duplicates...")

        applications = []
        unique_combos = set()

        # Step 1: Create 95% unique combinations
        while len(unique_combos) < int(NUM_APPLICATIONS * (1 - DUPLICATE_RATIO)):
            key = (
                random.choice(jobs).id,
                random.choice(resumes).id,
                random.choice(ips).id
            )
            unique_combos.add(key)

        # Step 2: Add non-flagged applications
        for job_id, resume_id, ip_id in unique_combos:
            applications.append(JobApplication(
                job_post_id=job_id,
                resume_id=resume_id,
                ip_address_id=ip_id,
                timestamp=timezone.now(),
                is_flagged=False
            ))

        # Step 3: Add 5% flagged duplicates from existing combos
        duplicate_combos = random.sample(
            list(unique_combos), int(NUM_APPLICATIONS * DUPLICATE_RATIO))
        for job_id, resume_id, ip_id in duplicate_combos:
            applications.append(JobApplication(
                job_post_id=job_id,
                resume_id=resume_id,
                ip_address_id=ip_id,
                timestamp=timezone.now(),
                is_flagged=True
            ))

        # Step 4: Shuffle and insert all
        random.shuffle(applications)
        JobApplication.objects.bulk_create(applications, batch_size=1000)

        self.stdout.write(self.style.SUCCESS("✅ Done reseeding and flagging!"))
