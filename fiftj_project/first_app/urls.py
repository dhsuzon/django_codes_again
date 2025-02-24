
from django.urls import path
from first_app.views import Home,About,submit_form,DjangoForm,StudentForm


urlpatterns = [
    path("",Home,name="homepage"),
    path("about/",About,name="aboutpage"),
    path("form/",submit_form,name="submit_form"),
    path("DjangoForm/",StudentForm,name="DjangoForm"),
    
]
