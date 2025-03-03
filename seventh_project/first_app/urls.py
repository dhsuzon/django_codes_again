from django.urls import path
from first_app.views import Home

urlpatterns = [
    path("",Home,name="home")
]
