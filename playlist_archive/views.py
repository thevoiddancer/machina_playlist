from django.shortcuts import render

def landing_page(request):
    return render(request, 'playlist_archive/landing.html')
