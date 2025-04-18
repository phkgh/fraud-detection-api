from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import JobPost


class JobPostViewSetTests(APITestCase):
    def test_job_list_success(self):
        JobPost.objects.create(title="Dev", company_name="TestCo")
        response = self.client.get("/api/jobs/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Dev", str(response.data))
