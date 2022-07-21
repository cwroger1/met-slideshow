from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    response = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/search?hasImages=true&q=flowers')
    if response.status_code > 299:
        response.raise_for_status()
    return render(request, "smartframe/index.html", {
        'response': response.json()
    })