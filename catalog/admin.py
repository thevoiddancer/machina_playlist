from django.contrib import admin

# Register your models here.
from .models import AlbumInfo, BandInfo, AlbumInfo, SongInfo

admin.site.register(BandInfo)
admin.site.register(AlbumInfo)
admin.site.register(SongInfo)