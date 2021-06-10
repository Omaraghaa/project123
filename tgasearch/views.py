from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from isodate import parse_duration
from django.conf import settings
from django.shortcuts import render, redirect
from urllib.request import urlopen as uReq 
import pandas as pd
from pandas.io.json import json_normalize
pd.options.display.max_colwidth = 100000

def index2(request):
    record = {}
    context = {}
    if request.method == 'POST':
        search_query = request.POST['tga']
        tga_url ='https://tga-search.clients.funnelback.com/s/search.html?query='
        search_query=search_query.replace(' ','+')
        request_url = tga_url  + str(search_query) + '&collection=tga-artg'
        uclient=uReq(request_url)
        res=uclient.read()
        uclient.close()
        soup =BeautifulSoup(res,'html.parser')
        sresults=soup.findAll('ul', attrs={'class':'attributes'})
        lenrst= len(sresults)
        l5=[]
        for i in sresults:
            if i!=' ':
                i=i.text
                i=i.splitlines()
                l5.append(i)
        r=[]
        l6=[]
        if lenrst==0:
            r=["No results found"]
        for i in l5:
            r2={}
            for j in i:
                if j!='':
                    ssplit = j.split(':')
                    key = ssplit.pop(0)
                    r2[key] = ssplit
            l6.append(r2)
            r=l6
        context = {

            'record' : r
            
        }    
    return render(request, 'tgasearch/tgasearch.html',context)

