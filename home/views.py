from django.http import HttpResponse
from django.shortcuts import render
import requests

# Create your views here.

def home(request):
  if request.method == 'POST':
    pass
  response = requests.get('http://127.0.0.1:8000/books/2')
  # print(response)
  # response = requests.get('https://unisource.onrender.com/api/v1/resource/')
  cat = requests.get('https://unisource.nahom.eu.org/api/v1/category/')
  if response.status_code == 200:
    data = response.json()
    category = cat.json()
  else:
    data = {}
    category = {}
  # print(data, category)
  context = {'data':data, 'category':category}
  return render(request, 'index.html', context)


def login(request):
  return render(request, 'login.html')


def search(request):
    query = request.GET.get('searchInput')    
    if not query:
        data = {}
    else:
        params = {'query': query}
        response = requests.get('https://unisource.nahom.eu.org/api/v1/resource/', params=params)
        
        # Check the response status code
        if response.status_code == 200:
            data = response.json()
        else:
            data = {}

    # Prepare the context data and render the template
    context = {'data': data}
    return render(request, 'search.html', context)
  

def school(request, id):
  params = {
    "category": id
  }
  response = requests.get('https://unisource.nahom.eu.org/api/v1/resource/', params=params)
  if response.status_code == 200:
    data = response.json()
  else:
    data = {}
  context = {'data':data}
  return render(request, 'school.html', context)