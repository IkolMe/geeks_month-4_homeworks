from django.urls import path
from . import views


urlpatterns = [
    path('', views.item_view, name='movies'),
    path('create_movies_item/', views.create_movies_item_view, name='create_movies_item'),
    path('delete_movies_item/', views.delete_movies_item_view, name='delete_movies_item'),
    path('movies_item_drop/<int:id>/delete/', views.delete_movies_item_view, name='delete_movie_item'),
    path('edit_movies_item/', views.edit_movies_item_view, name='edit_movies_item'),
    path('movies_item_edit/<int:id>/update/', views.edit_movies_item, name='edit_movies_item'),
]
