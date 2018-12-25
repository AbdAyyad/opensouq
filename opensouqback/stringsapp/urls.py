from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^hamming/', views.hamming_api.as_view()),
    url(r'^levenstion/', views.levenstion_api.as_view()),
]