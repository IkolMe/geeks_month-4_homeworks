from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
from django.urls import reverse
from django.views import generic


# READ
class ItemsView(generic.ListView):
    template_name = 'movies/movies.html'
    model = models.Item

    def get_queryset(self):
        return self.model.objects.all()


# CREATE
class CreateView(generic.CreateView):
    template_name = 'crud/create_movies_item.html'
    model = models.Item
    form_class = forms.MovieForm

    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateView, self).form_valid(form=form)


# DELETE
class DeleteView(generic.DeleteViewView):
    template_name = 'crud/delete/delete_movies_item.html'
    model = models.Item
    success_url = 'delete_movies_item'

    def get_object(self, **kwargs):
        movie_id = self.kwargs.get('id')
        return get_object_or_404(models.Item, id=movie_id)


# UPDATE
class UpdateView(generic.UpdateView):
    template_name = 'crud/update/update_movies_item.html'
    model = models.Item
    success_url = 'edit_movies_item'

    def get_object(self, **kwargs):
        movie_id = self.kwargs.get('id')
        return get_object_or_404(models.Item, id=movie_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateView, self).form_valid(form=form)


class SearchView(generic.ListView):
    template_name = 'movies/movies.html'
    paginate_by = 10

    def get_queryset(self):
        return models.Movie.objects.filter(name__icontains=self.request.GET.get('q'))

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context

