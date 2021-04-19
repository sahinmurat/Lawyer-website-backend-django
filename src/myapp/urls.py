from django.urls import path
from .views import  list,create,detail_comment, update_delete, like, category, categorycreate

app_name = "lawyer"

urlpatterns = [
    path("list", list, name="list"),
    path("create", create , name="create"),
    # path("<str:slug>", post_get_update_delete , name="detail"),
    path("<str:slug>/detail-comment", detail_comment , name="detail-comment"),
    path("<str:slug>/update",update_delete , name="delete-update"),
    path("<str:slug>/like",like , name="like"),
    path("category",category , name="category"),
    path("categorycreate",categorycreate , name="categorycreate"),
    
 
]

 