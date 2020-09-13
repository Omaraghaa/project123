from django.shortcuts import render

# Create your views here.
import requests

from isodate import parse_duration

from django.conf import settings
from django.shortcuts import render, redirect


def index(request):
    clinical_data = []
    if request.method == 'POST':
        search_query = request.POST['search']

        clinic_url = 'https://clinicaltrials.gov/api/query/full_studies'

        clincal_parameters = {
            'expr': search_query,
            'min_rnk': 1,
            'max_rnk': 9,
            'fmt': 'json'
        }
        clinical_request = requests.get(clinic_url, params=clincal_parameters)

        clinical_values = clinical_request.json()['FullStudiesResponse']

        clinical_data = clinical_values['FullStudies']


    context = {
        'clinical_data': clinical_data
    }

    return render(request, 'search/index.html', context)
