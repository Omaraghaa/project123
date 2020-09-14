from django.shortcuts import render

# Create your views here.
import requests

from isodate import parse_duration

from django.conf import settings
from django.shortcuts import render, redirect


def FDA(request):
    FDA_values = []
    if request.method == 'POST':
        search_query = request.POST['search']

        FDA_url = 'https://api.fda.gov/drug/event.json?'
        
        request_url = FDA_url + 'search=patient.drug.medicinalproduct:' + str(search_query) + '&limit=100'
        
        FDA_response = requests.get(request_url).json()

        FDA_values = FDA_response['results']

        #clinical_data = clinical_values['FullStudies']


    context = {
        'FDA_values': FDA_values
    }

    return render(request, 'FDA/FDA.html', context)
