from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
from django.urls import reverse
from django.http import HttpResponse


# READ
def item_view(request):
    if request.method == 'GET':
        item = models.Item.objects.all()
        return render(request, template_name='movies/movies.html', context={'item': item})


# CREATE
def create_movies_item_view(request):
    if request.method == 'POST':
        form = forms.MovieForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect(reverse('movies'))
    else:
        form = forms.MovieForm()
        return render(request, template_name='crud/create_movies_item.html', context={'form': form})


# DELETE
def delete_movies_item_view(request):
    if request.method == 'GET':
        delete_movies_item = models.Item.objects.all()
        return render(request, template_name='crud/delete/delete_movies_item.html', context={'delete_movies_item': delete_movies_item})


def movies_item_drop_view(request, id):
    movies_item_id = get_object_or_404(models.Item, id=id)
    movies_item_id.delete()
    return redirect(reverse('delete_movies_item'))


# UPDATE
def edit_movies_item_view(request):
    if request.method == 'GET':
        edit_movies_item = models.Item.objects.all()
        return render(request, template_name='crud/edit/edit_movies_item.html', context={'edit_movies_item': edit_movies_item})


def edit_movies_item(request, id):
    movies_item_id = get_object_or_404(models.Item, id=id)
    if request.method == 'POST':
        form = forms.MovieForm(instance=movies_item_id, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('edit_movies_item'))

    else:
        form = forms.MovieForm(instance=movies_item_id)
        return render(request, template_name='crud/update/movies_item_edit.html', context={
            'form': form,
            'movies_item_id': movies_item_id
        })

