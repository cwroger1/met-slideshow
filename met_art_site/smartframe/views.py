from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    met_url = "https://collectionapi.metmuseum.org/public/collection/v1/search?hasImages=true&q=flowers"
    response = requests.get(met_url)
    if response.status_code > 299:
        response.raise_for_status()
    return render(request, "smartframe/index.html", {
        'response': response.json()
    })