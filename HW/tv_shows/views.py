from django.shortcuts import render, get_object_or_404
from . import models


# Create your views here.
def tv_shows_list(request):
    if request.method == 'GET':
        tv_shows = models.Tv_shows.object.all()
        return render(request, template_name='tv_shows/tv_shows.html',
                      context={'tv_shows': tv_shows})


def tv_shows_detail(request, id):
    if request.method == 'GET':
        tv_shows_id = get_object_or_404(models.Tv_shows, id=id)
        return render(request, template_name='tv_shows/tv_shows_detail.html',
                      context={'tv_shows_id': tv_shows_id})
