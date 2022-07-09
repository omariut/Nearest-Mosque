from django.shortcuts import render
from django.urls import reverse_lazy
# Create your views here.
from django.views import generic
from django.contrib.gis.geos import fromstr, Point
from django.contrib.gis.db.models.functions import Distance
from .models import Mosque


longitude = -80.191788
latitude = 25.761681

user_location = Point(longitude, latitude, srid=4326)

class MosqueList(generic.ListView):
    model = Mosque
    context_object_name = 'mosques'
    queryset = Mosque.objects.annotate(distance=Distance('location',
    user_location)
    ).order_by('distance')[0:6]
    template_name = 'mosques/index.html'


class CreateMosque(generic.CreateView):
    model = Mosque
    context_object_name = 'mosques'
    template_name = 'mosques/new_mosque.html'
    success_url = reverse_lazy('all_mosques')
    fields = '__all__'







