from django.db import models
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .models import AlbumInfo, BandInfo

# Create your models here.

class BandInfo(models.Model):
    name = models.CharField(blank=False, null=False, max_length=200)

    def __repr__(self):
        return self.name

class AlbumInfo(models.Model):
    name = models.CharField(blank=False, null=False, max_length=200)
    band: 'BandInfo' = models.ForeignKey('BandInfo', models.CASCADE, blank=False, null=False, related_name='albums')

    def __repr__(self):
        return f'{self.band}: {self.name}'
    
class SongInfo(models.Model):
    name = models.CharField(blank=False, null=False)
    album: 'AlbumInfo' = models.ForeignKey('AlbumInfo', models.CASCADE, blank=False, null=False, related_name='songs')

    def __repr__(self) -> str:
        return f'{self.album.band} ({self.album}): {self.name}'
    
    