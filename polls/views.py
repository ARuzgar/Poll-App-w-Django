from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return HttpResponse("Hello World! You're at the polls index.")

def aDarkSecret(request):
	return HttpResponse("Lots of passed, non shall be shared. The inflictions deep and sharp, as the tip of a razor should be. Farewell, sleep in disguise.")
# Create your views here.
