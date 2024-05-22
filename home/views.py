from django.http import HttpResponse
from django.shortcuts import render
import requests

# Create your views here.

def home(request):
  if request.method == 'POST':
    pass
  response = requests.get('https://unisource.web.nahom.eu.org/api/v1/resource/')
  # response = requests.get('https://unisource.onrender.com/api/v1/resource/')
  cat = requests.get('https://unisource.web.nahom.eu.org/api/v1/category/')
  print('response')
  if response.status_code == 200:
    data = response.json()
    # category = cat.json()
  else:
    data = {}
    category = {}
  print(data)
  category = data
  context = {'data':data, 'category':category}
  return render(request, 'index.html', context)


def login(request):
  return render(request, 'login.html')