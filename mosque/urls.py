from django.urls import path
from mosque import views

urlpatterns = [
    # [...]
    path('list', views.MosqueList.as_view(),  name = 'all_mosques'),
    path('create', views.CreateMosque.as_view(), name = 'create_mosque'),
]