from django.http import HttpResponse
from django.shortcuts import render
import requests

# Create your views here.

def home(request):
  if request.method == 'POST':
    pass
  response = requests.get('https://unisource.nahom.eu.org/api/v1/resource/')
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
    # Extract the search query from the request
    query = request.GET.get('searchInput')
    print(query)
    
    # Ensure query is not empty before proceeding
    if not query:
        data = {}
    else:
        # Prepare query parameter
        params = {'query': query}
        
        # Make the GET request to the external API
        response = requests.get('https://unisource.nahom.eu.org/api/v1/resource/', params=params)
        
        # Check the response status code
        if response.status_code == 200:
            # Parse JSON response into Python data
            data = response.json()
        else:
            # If response status code is not 200, handle it gracefully
            data = {}
            # Optionally, you can log the error or handle it in a different way
            
    # Prepare the context data and render the template
    context = {'data': data}
    return render(request, 'search.html', context)