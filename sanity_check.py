# sanity_check.py

import os
import django

# ✅ Set up Django settings before importing any Django modules
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fraud_system.settings")
django.setup()

if __name__ == "__main__":
    from api.models import JobPost, Resume, IPAddressLog, JobApplication

    print("📊 Total Job Posts:", JobPost.objects.count())
    print("📄 Total Resumes:", Resume.objects.count())
    print("📡 Total IP Addresses:", IPAddressLog.objects.count())
    print("📬 Total Job Applications:", JobApplication.objects.count())

    print("\n📝 Sample Job Post:", JobPost.objects.first())
    print("📎 Sample Resume:", Resume.objects.first())
    print("🌐 Sample IP Address:", IPAddressLog.objects.first())
    print("📨 Sample Job Application:",
          JobApplication.objects.select_related('job_post', 'resume', 'ip_address').first())
