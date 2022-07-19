from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    response = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/objects').json()
    return render(request, "smartframe/index.html", {
        'response': response
    })