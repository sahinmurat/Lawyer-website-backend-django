from django.urls import path
from .views import  list
app_name = "lawyer"

urlpatterns = [
    path("list", list, name="list"),
     
]

 