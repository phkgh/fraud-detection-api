from rest_framework import serializers
from .models import JobPost, Resume, IPAddressLog, JobApplication


class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = '__all__'


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'


class IPAddressLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPAddressLog
        fields = '__all__'


class JobApplicationSerializer(serializers.ModelSerializer):
    job_post = JobPostSerializer()
    resume = ResumeSerializer()
    ip_address = IPAddressLogSerializer()

    class Meta:
        model = JobApplication
        fields = '__all__'
