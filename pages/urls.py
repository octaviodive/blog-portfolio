from django.urls import path
from . import views

urlpatterns = [
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("privacy-policy/", views.privacy_policy, name="privacy-policy"),
    path("terms-of-service/", views.terms_of_service, name="terms-of-service")
]