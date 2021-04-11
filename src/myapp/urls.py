from django.urls import path
from .views import  list, create

app_name = "blog"

urlpatterns = [
    path("list", list, name="list"),
    path("create", create , name="create")
 ]

 