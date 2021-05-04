from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
   return HttpResponse("<em> My Second Project </em>")

def help(request):
   my_dict = {'insert_help':'help is being inserted now!'}
   return render(request, 'help.html', context=my_dict)