from django.urls import path
from . import views

appname = 'html_text'

urlpatterns = [
    path('', views.convertor, name='convertor_view'),
]