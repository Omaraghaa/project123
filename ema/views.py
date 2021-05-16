from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from isodate import parse_duration
from django.conf import settings
from django.shortcuts import render, redirect
from urllib.request import urlopen as uReq 

def index3(request):
    r = {}
    context = {}
    if request.method == 'POST':
        search_query = request.POST['ema']
        ema_url ='https://www.ema.europa.eu/en/medicines?search_api_views_fulltext='
        search_query=search_query.replace(' ','+')
        request_url = ema_url  + str(search_query)
        print("url "+request_url)
        html = requests.get(request_url).content
        soup = BeautifulSoup(html, "html.parser")
        links = [a["href"] for a in soup.find_all("a", {"class": "ecl-link ecl-list-item__link"})]
        link_list=[]
        l1=[]
        ema_url2="https://www.ema.europa.eu"
        for i in links:
            if ema_url2 not in i:
                link_list.append(ema_url2 + i)
        for url_result in link_list:
            html1 = requests.get(url_result).content
            soup1 = BeautifulSoup(html1, "html.parser")
            table= soup1.select("tbody")
            l5=[]
            for i in table:
                i=i.text
                i=i.splitlines()
                for j in i:
                    if j!='' and j!='About this medicine' and j!='About this procedure' and j!='Key dates and outcomes' and  not(j.startswith ('This type of referral is')):
                        l5.append(j.strip())
            l1.append(l5)
            r=l1
        if len(link_list)==0:
            r=['No results found']
        context = {

                'record' : r
                
            }    
    return render(request, 'ema/ema.html',context)

