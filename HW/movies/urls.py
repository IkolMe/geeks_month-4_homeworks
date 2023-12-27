from django.urls import path
from . import views


app_name = 'movies'

urlpatterns = [
    path('', views.ItemsView.as_view(), name='movies'),
    path('create_movies_item/', views.CreateView.as_view(), name='create_movies_item'),
    path('delete_movies_item/', views.DeleteView.as_view(), name='delete_movies_item'),
    path('edit_movies_item/', views.UpdateView.as_view(), name='edit_movies_item'),
    path('search/', views.SearchView.as_view(), name='search')
]
