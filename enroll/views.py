import re
from django.shortcuts import render
from django.core.cache import cache
from importlib_metadata import version

# Create your views here.


# def home(request):

#       mv= cache.get('movie', 'has_expired')
#       if mv == 'has_expired':
#             cache.set('movie','the bangla',30)
#             mv= cache.get('movie')
#       return render(request, 'enroll/home.html',{'fm':mv})



# def home(request):
#       fee = cache.get_or_set('fees',2000,10, version=2)
#       return render(request, 'enroll/home.html',{'fm':fee})



# def home(request):
#       data= {'name':'shukumar', 'roll':12}
#       cache.set_many(data, 10)
#       fee = cache.get_many(data)
#       return render(request, 'enroll/home.html',{'fm':fee})


def home(request):
      cache.delete('fees')
      return render(request, 'enroll/home.html')