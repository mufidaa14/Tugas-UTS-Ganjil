from django.urls import path
from . import views

urlpatterns = [
    path("depan/", views.depan, name="depan"),
    path("biodata/", views.biodata, name="biodata"),
    path("History/", views.History, name="History"),
    
]