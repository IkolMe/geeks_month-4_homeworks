from django.urls import path
from . import views


urlpatterns = [
    path('parser_cars', views.ParserFormView.as_view(), name='parser_cars'),
]
