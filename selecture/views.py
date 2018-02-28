from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404

def homepage(request):
  return HttpResponseRedirect('/timetable/')
