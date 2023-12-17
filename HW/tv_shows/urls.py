from django.urls import path
from . import views


urlpatterns = [
    path('tv_shows_list/', views.tv_shows_list, name='tv_shows_list'),
    path('tv_shows_list/<int:id>/', views.tv_shows_detail, name='tv_shows_detail')
]
