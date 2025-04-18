from django.test import TestCase
from django.utils import timezone
from api.models import JobPost, Resume, IPAddressLog, JobApplication


class FlaggingLogicTests(TestCase):
    def setUp(self):
        self.job = JobPost.objects.create(title="Dev", company_name="TestCo")
        self.resume = Resume.objects.create(file_id="resume_test")
        self.ip = IPAddressLog.objects.create(ip_address="1.1.1.1")

    def test_duplicate_application_flagged(self):
        ts = timezone.now()
        a1 = JobApplication.objects.create(
            job_post=self.job,
            resume=self.resume,
            ip_address=self.ip,
            timestamp=ts
        )
        a2 = JobApplication.objects.create(
            job_post=self.job,
            resume=self.resume,
            ip_address=self.ip,
            timestamp=ts
        )
        self.assertFalse(a1.is_flagged)
        self.assertTrue(a2.is_flagged)
