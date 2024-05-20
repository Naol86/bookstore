from django.http import HttpResponse
from django.shortcuts import render
import requests

# Create your views here.

def home(request):
  if request.method == 'POST':
    pass
  response = requests.get('https://unisource.web.nahom.eu.org/api/v1/resource/')
  cat = requests.get('https://unisource.web.nahom.eu.org/api/v1/category/')
  if response.status_code == 200 and cat.status_code == 200:
    data = response.json()
    category = cat.json()
  else:
    data = {}
    category = {}
  category = data
  context = {'data':data, 'category':category}
  return render(request, 'index.html', context)