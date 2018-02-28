from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.db.models.signals import pre_save, post_save

from django.core.urlresolvers import reverse
from grade.models import Grade
from lecture.models import Lecture

User = get_user_model()

department_choice = (
    ('文学部','文学部'),
    ('教育学部','教育学部'),
    ('法学部','法学部'),
    ('経済学部','経済学部'),
    ('情報学部','情報学部/情報文化学部'),
    ('理学部','理学部'),
    ('医学部','医学部'),
    ('工学部','工学部'),
    ('農学部','農学部'))


class StudentManager(models.Manager):
    def get_current_student(self, request):
        if request.user.is_authenticated():
            current_student = request.user.student
        else:
            guest_id = request.session.get('guest_id',None)
            if guest_id is not None:
              current_student = Student.objects.get(id=guest_id)
            else:
              print("new student created")
              new_student = Student.objects.create(user=None)
              request.session['guest_id'] = new_student.id
              current_student = new_student
        return current_student

class Student(models.Model):
    user              = models.OneToOneField(User,related_name="student", null=True)
    slug              = models.SlugField(max_length=50)
    active            = models.BooleanField(default=True)
    department        = models.CharField(choices=department_choice,max_length=30,null=True,)
    created_at        = models.DateField(auto_now_add=True)

    grade  = models.OneToOneField(Grade,related_name='student',null=True)
    favorite_lecture  = models.ManyToManyField(Lecture,related_name='favorite_student')

    objects = StudentManager()


    def __str__(self):
        return str(self.id)

def User_post_save_receiver(sender, instance, created, *args, **kwargs):
  if created:
    Student.objects.create(user=instance)

def Student_post_save_receiver(sender, instance, created, *args, **kwargs):
  if created:
    new_grade = Grade.objects.create()
    instance.grade = new_grade
    instance.save()

post_save.connect(User_post_save_receiver,sender=User)
post_save.connect(Student_post_save_receiver,sender=Student)
