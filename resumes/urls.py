from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import ResumeViewSet

router = DefaultRouter()
router.register(prefix=r"resumes", viewset=ResumeViewSet, basename="resume")

urlpatterns = [
    path("", include(router.urls)),

    path("auth-token/", obtain_auth_token, name="obtain-auth-token"),
]

