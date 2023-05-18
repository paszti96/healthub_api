from django.urls import path
from main import views

# Define the URL patterns for the my_django_app.
urlpatterns = [
    # Map the /news/ URL to the fetch_news view function.
    path('nearest/', views.fetch_nearest, name='fetch_nearest'),
]
