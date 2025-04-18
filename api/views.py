from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render

from rest_framework import viewsets
from .models import JobPost, Resume, IPAddressLog, JobApplication
from .serializers import (
    JobPostSerializer,
    ResumeSerializer,
    IPAddressLogSerializer,
    JobApplicationSerializer
)


class JobPostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer


class ResumeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer


class IPAddressLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = IPAddressLog.objects.all()
    serializer_class = IPAddressLogSerializer


class JobApplicationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = JobApplication.objects.select_related(
        'job_post', 'resume', 'ip_address').all()
    serializer_class = JobApplicationSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['job_post', 'resume', 'ip_address', 'is_flagged']
    ordering_fields = ['timestamp', 'id']
    ordering = ['-timestamp']  # default
