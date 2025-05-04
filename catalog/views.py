from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView
from django.shortcuts import render
from .models import BandInfo, AlbumInfo

# Create your views here.
def catalog_view(request):
    return render(request, 'catalog/catalog.html')

def bands_view(request):
    return render(request, 'catalog/bands.html')

class BandListView(ListView):
    model = BandInfo

    def get_queryset(self):
        queryset = BandInfo.objects.all()
        print(queryset)
        return queryset
    
class AlbumListView(ListView):
    model = AlbumInfo

    def get_queryset(self):
        band_name = self.kwargs['band_name']
        # From band
        _queryset = BandInfo.objects.get(name=band_name).albums.all()
        # From album
        queryset = AlbumInfo.objects.filter(band__name=band_name)
        return queryset
    
    