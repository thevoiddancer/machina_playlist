from django.urls import path, include
from .views import bands_view, catalog_view, BandListView, AlbumListView

urlpatterns = [
    path('', catalog_view, name='catalog'),
    # path('bands', bands_view, name='catalog-bands')
    path('bands/', BandListView.as_view(), name='catalog-bands'),
    path('bands/<str:band_name>', AlbumListView.as_view(), name='albums'),

]