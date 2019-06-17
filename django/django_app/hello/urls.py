from django.urls import path
from . import views

urlpatterns = [
    
    # path("<int:id>/<name>", views.index, name="index"),
    path("", views.index, name="index"),
    path("next", views.next, name="next"),
    path("form", views.form, name="form"),
]
