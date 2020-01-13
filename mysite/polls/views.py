from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return HttpResponse("Hello, world.")

def detail(request, qid):
  return HttpResponse("You're checking QID %s." %qid)

def results(request, qid):
  response = "You're looking at QID %s."
  return HttpResponse(response %qid)

def vote(request, qid):
  return HttpResponse("You're voting on question %s." %qid)