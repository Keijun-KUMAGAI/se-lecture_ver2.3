from django.shortcuts import render
from django.views.generic import DetailView, View, ListView
from .models import Timetable

from django.contrib.auth import get_user_model
from student.models import Student
from review.models import Review
from lecture.models import Lecture
from django.db.models import Q
from grade.models import Grade
from django.http import HttpResponseRedirect, Http404
User = get_user_model()


class TimetableDetail(View):
    template_name = 'timetable/timetable_edit.html'
    def get(self, request):
      timetable, timetable_list, grade = Timetable.objects.get_two_timetable_and_grade(request)
      context = {
      'timetable':timetable,
      'timetable_list':timetable_list,
      'grade':grade,
      'lecture_all':Lecture.objects.all(),
      'user_all':User.objects.all(),
      'student_all':Student.objects.all(),
      'review_all':Review.objects.all(),
      }
      return render(request,self.template_name,context)

class TimetableList(ListView):
    paginate_by = 20
    model = Lecture
    template_name  = 'timetable/timetable_search.html'

    def __init__(self, **kwargs):
          super(TimetableList, self).__init__(**kwargs)
          self.form = None
    def get_queryset(self):
        qs           = super(TimetableList, self).get_queryset()
        time         = self.request.GET.get('time', None)
        day          = self.request.GET.get('day', None)
        timetable    = self.request.GET.get('timetable_id', None)
        lecture_type_custom    = self.request.GET.getlist('lecture_type', 'error')

        lookups = Q()
        lecture_type = ['基礎セミナー','言語文化Ⅰ','言語文化Ⅱ','言語文化Ⅲ','健康・スポーツ科学','文系基礎科目','理系基礎科目（文系）','理系基礎科目（理系）','文系教養科目','理系教養科目','全学教養科目','開放科目']
        if not 'error' in lecture_type_custom:
            lecture_type = lecture_type_custom
        else:
            if self.request.user.is_authenticated():
                lecture_type.append(self.request.user.student.department + '専門')
                if self.request.user.student.department == '情報学部':
                    lecture_type.append('情報文化学部専門')
            else:
                lecture_type = ['基礎セミナー','言語文化Ⅰ','言語文化Ⅱ','言語文化Ⅲ','健康・スポーツ科学','文系基礎科目','理系基礎科目（文系）','理系基礎科目（理系）','文系教養科目','理系教養科目','全学教養科目','開放科目','文学部専門','教育学部専門','教育学部専門','法学部専門','経済学部専門','情報学部専門','理学部専門','医学部専門','工学部専門','農学部専門','情報文化学部専門']
        lookups.add(Q(day=day),lookups.connector)
        lookups.add(Q(time=time),lookups.connector)
        lookups.add(Q(lecture_type__in=lecture_type),lookups.connector)
        qs = qs.filter(lookups).distinct()
        return qs
    def get_context_data(self, **kwargs):
        ctx = super(TimetableList, self).get_context_data(**kwargs)
        ctx['timetable_id'] = self.request.GET.get('timetable_id', None)
        ctx['time'] = self.request.GET.get('time', None)
        ctx['day'] = self.request.GET.get('day', None)
        ctx.update(dict(form=self.form,
                        query_string=self.request.GET.urlencode()))
        return ctx

class TimetableRegister(View):
    template_name = 'timetable/timetable_edit.html'
    def get(self, request):
      time            = self.request.GET.get('time', None)
      day             = self.request.GET.get('day', None)
      timetable_id    = self.request.GET.get('timetable_id', None)
      lecture_id      = self.request.GET.get('lecture_id',None)

      print("time:"+time)
      print("day:"+day)

      Timetable.objects.get_lecture_register(timetable_id,time,day,lecture_id)
      timetable, timetable_list, grade = Timetable.objects.get_two_timetable_and_grade(request)

      return HttpResponseRedirect('/timetable/')

class TimetableAnregister(View):
    template_name = 'timetable/timetable_edit.html'
    def get(self, request):
      time            = self.request.GET.get('time', None)
      day             = self.request.GET.get('day', None)
      timetable_id    = self.request.GET.get('timetable_id', None)
      lecture_id      = None

      Timetable.objects.get_lecture_register(timetable_id,time,day,lecture_id)
      timetable, timetable_list, grade = Timetable.objects.get_two_timetable_and_grade(request)

      return HttpResponseRedirect('/timetable/')
