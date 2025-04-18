from rest_framework.routers import DefaultRouter
from .views import JobPostViewSet, ResumeViewSet, IPAddressLogViewSet, JobApplicationViewSet

router = DefaultRouter()
router.register(r'jobs', JobPostViewSet, basename='jobpost')
router.register(r'resumes', ResumeViewSet, basename='resume')
router.register(r'ips', IPAddressLogViewSet, basename='ipaddresslog')
router.register(r'applications', JobApplicationViewSet,
                basename='jobapplication')

urlpatterns = router.urls  # ✅ This is required so Django knows what to include
