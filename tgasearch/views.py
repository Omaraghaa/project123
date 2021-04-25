from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from isodate import parse_duration
from django.conf import settings
from django.shortcuts import render, redirect
from urllib.request import urlopen as uReq 

def index2(request):
    record = {}
    context = {}
    if request.method == 'POST':
        search_query = request.POST['tga']

        tga_url ='https://tga-search.clients.funnelback.com/s/search.html?query='
        search_query=search_query.replace(' ','+')
        request_url = tga_url  + str(search_query) + '&collection=tga-artg'
        #print("url "+request_url)

        uclient=uReq(request_url)
        res=uclient.read()
        uclient.close()
        #res=requests.get(request_url)
        soup =BeautifulSoup(res,'html.parser')
        sresults=soup.findAll('ul', attrs={'class':'attributes'})
        print (len(sresults))
        r=[]
        for i in sresults:
          r.append(i.text)
        context = {

            'record' : r
            
        }    
    return render(request, 'tgasearch/tgasearch.html',context)

