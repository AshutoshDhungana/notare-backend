from django.urls import path
from .views import test

app_name="notes"

urlpatterns = [
    path('', test)
]
