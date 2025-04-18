from rest_framework.decorators import api_view
from api.models import JobApplication, JobPost, Resume, IPAddressLog
from rest_framework.response import Response
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


@api_view(['GET'])
def stats_view(request):
    total_apps = JobApplication.objects.count()
    flagged_apps = JobApplication.objects.filter(is_flagged=True).count()
    flagged_pct = (flagged_apps / total_apps) * 100 if total_apps else 0

    return Response({
        'total_applications': total_apps,
        'flagged_applications': flagged_apps,
        'flagged_percentage': round(flagged_pct, 2),
        'total_jobs': JobPost.objects.count(),
        'total_resumes': Resume.objects.count(),
        'total_ips': IPAddressLog.objects.count(),
    })
