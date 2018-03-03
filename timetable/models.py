from django.db import models
from lecture.models import Lecture
from student.models import Student
from grade.models import Grade
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse

class TimetableManager(models.Manager):

    def get_two_timetable_and_grade(self, request):
        request.session.set_expiry(3600000)
        if request.user.is_authenticated():
            timetable_id = request.GET.get('timetable_id',None)
            if timetable_id:
              timetable = Timetable.objects.get(pk=timetable_id)
            else:
              timetable = Timetable.objects.filter(student=request.user.student).first()
            timetable_list = Timetable.objects.filter(student=request.user.student)
            grade = Grade.objects.get(student=request.user.student)
        else:
            guest_id = request.session.get('guest_id',None)
            if guest_id is not None:
              guest_student = Student.objects.get(id=guest_id)
              timetable_id = request.GET.get('timetable_id',None)
              if timetable_id:
                 timetable = Timetable.objects.get(pk=timetable_id)
              else:
                timetable = Timetable.objects.filter(student=guest_student).first()
              timetable_list = Timetable.objects.filter(student=guest_student)
              grade = Grade.objects.get(student=guest_student)
            else:
              print("new student created")
              new_student = Student.objects.create()
              request.session['guest_id'] = new_student.id
              timetable = Timetable.objects.filter(student=new_student).first()
              timetable_list = Timetable.objects.filter(student=new_student)
              grade = Grade.objects.get(student=new_student)
        return timetable, timetable_list, grade

    def get_lecture_register(self,timetable_id,time,day,lecture_id):
        timetable = self.get_queryset().get(id=timetable_id)
        lecture_list = [[timetable.mon1,timetable.mon2,timetable.mon3,timetable.mon4,timetable.mon5],
                        [timetable.tue1,timetable.tue2,timetable.tue3,timetable.tue4,timetable.tue5],
                        [timetable.wed1,timetable.wed2,timetable.wed3,timetable.wed4,timetable.wed5],
                        [timetable.thu1,timetable.thu2,timetable.thu3,timetable.thu4,timetable.thu5],
                        [timetable.fri1,timetable.fri2,timetable.fri3,timetable.fri4,timetable.fri5,]]
        lecture_selected = lecture_list[int(day)-1][int(time)-1]
        if lecture_id:
            lecture = Lecture.objects.get(id=lecture_id)
            if lecture != lecture_selected:
                lecture.popular += 1
                lecture.save()
        else:
            lecture = None
            lecture_selected.popular -= 1
            lecture_selected.save()
        if day=="1":
            if time=="1":
                timetable.mon1 = lecture
            if time=="2":
                timetable.mon2 = lecture
            if time=="3":
                timetable.mon3 = lecture
            if time=="4":
                timetable.mon4 = lecture
            if time=="5":
                timetable.mon5 = lecture
        if day=="2":
            if time=="1":
                timetable.tue1 = lecture
            if time=="2":
                timetable.tue2 = lecture
            if time=="3":
                timetable.tue3 = lecture
            if time=="4":
                timetable.tue4 = lecture
            if time=="5":
                timetable.tue5 = lecture
        if day=="3":
            if time=="1":
                timetable.wed1 = lecture
            if time=="2":
                timetable.wed2 = lecture
            if time=="3":
                timetable.wed3 = lecture
            if time=="4":
                timetable.wed4 = lecture
            if time=="5":
                timetable.wed5 = lecture
        if day=="4":
            if time=="1":
                timetable.thu1 = lecture
            if time=="2":
                timetable.thu2 = lecture
            if time=="3":
                timetable.thu3 = lecture
            if time=="4":
                timetable.thu4 = lecture
            if time=="5":
                timetable.thu5 = lecture
        if day=="5":
            if time=="1":
                timetable.fri1 = lecture
            if time=="2":
                timetable.fri2 = lecture
            if time=="3":
                timetable.fri3 = lecture
            if time=="4":
                timetable.fri4 = lecture
            if time=="5":
                timetable.fri5 = lecture
        timetable.save()

class Timetable(models.Model):
    student   = models.ForeignKey(Student, related_name='timetable', null=True)
    grade     = models.OneToOneField(Grade, related_name='timetable',null=True,blank=True)
    title     = models.CharField(max_length=30, default='No Title')
    mon1 = models.ForeignKey(Lecture, related_name='mon1',null=True)
    mon2 = models.ForeignKey(Lecture, related_name='mon2',null=True)
    mon3 = models.ForeignKey(Lecture, related_name='mon3',null=True)
    mon4 = models.ForeignKey(Lecture, related_name='mon4',null=True)
    mon5 = models.ForeignKey(Lecture, related_name='mon5',null=True)

    tue1 = models.ForeignKey(Lecture, related_name='tue1',null=True)
    tue2 = models.ForeignKey(Lecture, related_name='tue2',null=True)
    tue3 = models.ForeignKey(Lecture, related_name='tue3',null=True)
    tue4 = models.ForeignKey(Lecture, related_name='tue4',null=True)
    tue5 = models.ForeignKey(Lecture, related_name='tue5',null=True)

    wed1 = models.ForeignKey(Lecture, related_name='wed1',null=True)
    wed2 = models.ForeignKey(Lecture, related_name='wed2',null=True)
    wed3 = models.ForeignKey(Lecture, related_name='wed3',null=True)
    wed4 = models.ForeignKey(Lecture, related_name='wed4',null=True)
    wed5 = models.ForeignKey(Lecture, related_name='wed5',null=True)

    thu1 = models.ForeignKey(Lecture, related_name='thu1',null=True)
    thu2 = models.ForeignKey(Lecture, related_name='thu2',null=True)
    thu3 = models.ForeignKey(Lecture, related_name='thu3',null=True)
    thu4 = models.ForeignKey(Lecture, related_name='thu4',null=True)
    thu5 = models.ForeignKey(Lecture, related_name='thu5',null=True)

    fri1 = models.ForeignKey(Lecture, related_name='fri1',null=True)
    fri2 = models.ForeignKey(Lecture, related_name='fri2',null=True)
    fri3 = models.ForeignKey(Lecture, related_name='fri3',null=True)
    fri4 = models.ForeignKey(Lecture, related_name='fri4',null=True)
    fri5 = models.ForeignKey(Lecture, related_name='fri5',null=True)

    objects = TimetableManager()

    def __str__(self):
        return (self.title + str(self.pk))

def Timetable_post_save_receiver(sender, instance, *args, **kwargs):
    student = instance.student
    timetable_list = Timetable.objects.filter(student=student)

    # この全部書くやり方ださいからどうにか変えられないかね？
    # あと計算の仕方もださい
    student.grade.basic_seminar = 0
    student.grade.language_english = 0
    student.grade.sport = 0
    student.grade.human_basic = 0
    student.grade.science_basic_human = 0
    student.grade.science_basic_science = 0
    student.grade.liberal_human = 0
    student.grade.liberal_science = 0
    student.grade.liberal_all = 0
    student.grade.liberal_free = 0
    student.grade.major = 0

    for timetable in timetable_list:
        if timetable.mon1:
            timetable.mon1.point_add(student)
        if timetable.mon2:
            timetable.mon2.point_add(student)
        if timetable.mon3:
            timetable.mon3.point_add(student)
        if timetable.mon4:
            timetable.mon4.point_add(student)
        if timetable.mon5:
            timetable.mon5.point_add(student)

        if timetable.tue1:
            timetable.tue1.point_add(student)
        if timetable.tue2:
            timetable.tue2.point_add(student)
        if timetable.tue3:
            timetable.tue3.point_add(student)
        if timetable.tue4:
            timetable.tue4.point_add(student)
        if timetable.tue5:
            timetable.tue5.point_add(student)

        if timetable.wed1:
            timetable.wed1.point_add(student)
        if timetable.wed2:
            timetable.wed2.point_add(student)
        if timetable.wed3:
            timetable.wed3.point_add(student)
        if timetable.wed4:
            timetable.wed4.point_add(student)
        if timetable.wed5:
            timetable.wed5.point_add(student)

        if timetable.thu1:
            timetable.thu1.point_add(student)
        if timetable.thu2:
            timetable.thu2.point_add(student)
        if timetable.thu3:
            timetable.thu3.point_add(student)
        if timetable.thu4:
            timetable.thu4.point_add(student)
        if timetable.thu5:
            timetable.thu5.point_add(student)

        if timetable.fri1:
            timetable.fri1.point_add(student)
        if timetable.fri2:
            timetable.fri2.point_add(student)
        if timetable.fri3:
            timetable.fri3.point_add(student)
        if timetable.fri4:
            timetable.fri4.point_add(student)
        if timetable.fri5:
            timetable.fri5.point_add(student)
    student.grade.save()

post_save.connect(Timetable_post_save_receiver,sender=Timetable)

def Student_post_save_receiver(sender, instance, created, *args, **kwargs):
    if created:
        Timetable.objects.create(title='1年前期',student=instance)
        Timetable.objects.create(title='1年後期',student=instance)
        Timetable.objects.create(title='2年前期',student=instance)
        Timetable.objects.create(title='2年後期',student=instance)
        Timetable.objects.create(title='3年前期',student=instance)
        Timetable.objects.create(title='3年後期',student=instance)
        Timetable.objects.create(title='4年前期',student=instance)
        Timetable.objects.create(title='4年後期',student=instance)

post_save.connect(Student_post_save_receiver,sender=Student)
