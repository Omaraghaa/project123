from django.shortcuts import render

# Create your views here.
import requests

from isodate import parse_duration

from django.conf import settings
from django.shortcuts import render, redirect

def index1(request):
    record = {}
    context = {}
    if request.method == 'POST':
        search_query = request.POST['api']

        FDA_url = 'https://researchdata.edu.au/registry/services/e14f5b9056dc/getGrants?'

        request_url = FDA_url + 'id=' + str(search_query) 
        print("url "+request_url)
        r = requests.get(request_url).json()
        context = {

            'record' : r['message']['recordData']
        }    
    return render(request, 'api/api.html',context)

