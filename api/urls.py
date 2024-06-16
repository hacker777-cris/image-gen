from django.urls import path
from . import views

urlpatterns = [
    path("", views.ImageGenerationView.as_view()),
]
