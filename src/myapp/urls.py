from django.urls import path
from .views import  list,create,detail_comment, update_delete, like

app_name = "lawyer"

urlpatterns = [
    path("list", list, name="list"),
    path("create", create , name="create"),
    path("<str:slug>/detail-comment", detail_comment , name="detail-comment"),
    path("<str:slug>/update",update_delete , name="delete-update"),
    path("<str:slug>/like",like , name="like"),
    # path("category",category , name="category"),
    # path("categorycreate",categorycreate , name="categorycreate"),
]

 