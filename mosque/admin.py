from django.contrib.gis import admin
from mosque.models import Mosque

@admin.register(Mosque)
class MosqueAdmin(admin.OSMGeoAdmin):
    list_display = ('name', 'location')
