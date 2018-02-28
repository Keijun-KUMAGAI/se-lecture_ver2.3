from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, View, UpdateView
from django.urls import reverse_lazy
from django.db.models import Q

from .models import Lecture
from review.models import Review
from .forms import LectureForm, LectureSearchForm
from review.forms import ReviewForm
from student.models import Student

# Create your views here.
class LectureList(ListView):
  template_name = 'lecture/lecture_list.html'
  model = Lecture

class LectureDetail(View):
     template_name = 'lecture/lecture_detail.html'
     def get(self,request,pk):
         print(self.request.GET)
         lecture = Lecture.objects.get(pk=pk)
         current_student = Student.objects.get_current_student(request)
         context = {
         'lecture':lecture,
         'form':ReviewForm,
         'review_list':Review.objects.filter(lecture=lecture),
         'student':current_student
         }
         return render(request,self.template_name,context)
     def post(self, request, pk):
         print(self.request.POST)
         new_review = ReviewForm(request.POST)
         lecture = Lecture.objects.get(pk=pk)
         current_student = Student.objects.get_current_student(request)
         context = {
         'lecture':lecture,
         'form':ReviewForm,
         'review_list':Review.objects.filter(lecture=lecture),
         'student':current_student

         }
         if new_review.is_valid():
            print(self.request.POST)
             # 省略する
            title           = new_review.cleaned_data['title']
            comment         = new_review.cleaned_data['comment']
            rate_pass       = new_review.cleaned_data['rate_pass']
            rate_professor  = new_review.cleaned_data['rate_professor']
            Review.objects.create(lecture=lecture,title=title,comment=comment,rate_pass=rate_pass,rate_professor=rate_professor,student=current_student)
             # 省略する
            return render(request,self.template_name,context)
         else:
             context['form'] = new_review
             return render(request,self.template_name,context)


class LectureCreate(CreateView):
  model = Lecture
  template_name = 'lecture/lecture_create.html'
  success_url = reverse_lazy('lecture:search')
  def get_form(self, **kwargs):
    form = LectureForm(self.request.POST or None)
    print(self.request.POST)
    print(form.is_valid())
    return form

class LectureUpdate(UpdateView):
  model = Lecture
  template_name = 'lecture/lecture_update.html'
  fields = ('title','professor_name','target','syllabus','location','description','year','lecture_code','credit')
  def get_object(self, **kwargs):
      obj = super(LectureUpdate, self).get_object()
      print(obj)
      return obj



class LectureSearchList(ListView):
  paginate_by = 20
  model = Lecture
  template_name  = 'lecture/lecture_search.html'

  def __init__(self, **kwargs):
        super(LectureSearchList, self).__init__(**kwargs)
        self.form = None

  def get_queryset(self):
        # あとでmanegerに押し込む

        qs           = super(LectureSearchList, self).get_queryset()
        title        = self.request.GET.get('title', None)
        time         = self.request.GET.getlist('time', None)
        day          = self.request.GET.getlist('day', None)
        lecture_type = self.request.GET.getlist('lecture_type', None)
        lookups = Q()
        if day:
          lookups.add(Q(day__in=day),lookups.connector)
        if time:
          lookups.add(Q(time__in=time),lookups.connector)
        if title != '':
          lookups.add(Q(title__icontains=title) | Q(professor_name__icontains=title),lookups.connector)
        if lecture_type:
          if '情報学部専門' in lecture_type:
              lecture_type.append('情報文化学部専門')
          lookups.add(Q(lecture_type__in=lecture_type),lookups.connector)

        # /あとでmanegerに押し込む

        if day or time or title or lecture_type:
            qs = qs.filter(lookups).distinct()
            print("検索条件で絞る")
        return qs

  def get_context_data(self, **kwargs):
        ctx = super(LectureSearchList, self).get_context_data(**kwargs)
        ctx['form'] = LectureSearchForm
        ctx.update(dict(form=self.form,
                        query_string=self.request.GET.urlencode()))
        return ctx
