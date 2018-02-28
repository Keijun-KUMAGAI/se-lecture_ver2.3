from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView
from django.contrib.auth import get_user_model, logout
from .models import Student
from .forms import StudentForm, LoginForm
from django.core.urlresolvers import reverse_lazy, reverse
from timetable.models import Timetable
from django.http import HttpResponseRedirect, Http404
# Create your views here.

User = get_user_model()

def StudentCreate(request):
  template_name = 'student/student_create.html'
  form = StudentForm(request.POST or None)
  context = {
  'form':form,
  }
  if form.is_valid():
    print(form.cleaned_data)
    username = form.cleaned_data['username']
    email = form.cleaned_data['email']
    password = form.cleaned_data['password']
    new_student = User.objects.create_user(username,email,password)
    department = form.cleaned_data['department']
    student = Student.objects.get(user = new_student)
    student.department = department
    student.save()
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/timetable/')
    return HttpResponseRedirect('/timetable/')
  return render(request,template_name,context)


def Login(request):
    template_name = 'student/login.html'
    form = LoginForm(request.POST or None)
    context = {
    'form':form,
    }
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = authenticate(request, username=username, password=password)

      if user is not None:
          login(request, user)
          return HttpResponseRedirect('/timetable/')

    return render(request,template_name,context)

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/timetable/')
