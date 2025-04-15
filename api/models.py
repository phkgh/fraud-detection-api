from django.db import models


class JobPost(models.Model):
    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} at {self.company_name}"


class Resume(models.Model):
    file_id = models.CharField(max_length=64)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_id


class IPAddressLog(models.Model):
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return self.ip_address


class JobApplication(models.Model):
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    ip_address = models.ForeignKey(
        IPAddressLog, on_delete=models.SET_NULL, null=True, blank=True)
    timestamp = models.DateTimeField()
    is_flagged = models.BooleanField(default=False)

    def __str__(self):
        return f"Application to {self.job_post} from {self.ip_address}"
