from django.shortcuts import render

# Create your views here.
import requests

from isodate import parse_duration

from django.conf import settings
from django.shortcuts import render, redirect
import pandas as pd
from pandas.io.json import json_normalize
pd.options.display.max_colwidth = 100000


def index(request):
    c = pd.DataFrame(columns = ['q'])
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

        c = pd.DataFrame.from_dict(json_normalize(clinical_data), orient='columns')
        c = c.loc[:,["Rank","Study.ProtocolSection.IdentificationModule.NCTId", "Study.ProtocolSection.IdentificationModule.Organization.OrgFullName", "Study.ProtocolSection.IdentificationModule.OfficialTitle","Study.ProtocolSection.StatusModule.StatusVerifiedDate"]]
        c.rename(columns={"Study.ProtocolSection.IdentificationModule.NCTId": "NCTId", "Study.ProtocolSection.IdentificationModule.Organization.OrgFullName": "OrgFullName", "Study.ProtocolSection.IdentificationModule.OfficialTitle":"OfficialTitle","Study.ProtocolSection.StatusModule.StatusVerifiedDate":"StatusVerifiedDate"}, inplace=True)
        c = c.to_html(classes='data', index=False)
    context = {
        'clinical_data': c
    }

    return render(request, 'search/index.html', context)
