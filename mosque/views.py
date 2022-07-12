from django.shortcuts import render
from django.urls import reverse_lazy
from mosque.forms import MosqueForm
from django.contrib.gis import admin
from django.views import generic
from django.contrib.gis.geos import fromstr, Point
from django.contrib.gis.db.models.functions import Distance
from .models import Mosque


class MosqueList(generic.ListView):
    model = Mosque
    context_object_name = "mosques"
    template_name = "mosques/all_mosques.html"
    queryset = Mosque.objects.all()

class NearestMosque(generic.ListView):
    model = Mosque
    context_object_name = "mosques"
    template_name = "mosques/index.html"

    def get_queryset(self):
        if self.request.GET:
            longitude = float(self.request.GET.get("longitude"))
            latitude = float(self.request.GET.get("latitude"))
            user_location = Point(longitude, latitude, srid=4326)
            queryset = Mosque.objects.annotate(
                distance=Distance("location", user_location)
            ).order_by("distance")[0:6]

            self.extra_context = {"user_location": (longitude, latitude)}
            return queryset
        else:
            return None

        


class CreateMosque(generic.CreateView):
    model = Mosque
    form_class = MosqueForm
    context_object_name = "mosques"
    template_name = "mosques/new_mosque.html"
    success_url = reverse_lazy("list")

    def form_valid(self, form):
        longitude = form.cleaned_data["longitude"]
        latitude = form.cleaned_data["latitude"]
        location = Point(longitude, latitude, srid=4326)
        instance = form.save(commit=False)
        instance.location = location
        instance.save()
        return super().form_valid(form)
