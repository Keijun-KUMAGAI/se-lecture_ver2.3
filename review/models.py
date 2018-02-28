from django.db import models
from lecture.models import Lecture
from student.models import Student
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse

rate_professor_choice = (
('100','S：100'),
('90','A：90'),
('80','B：80'),
('70','C：70'),
('60','F：60')
)
rate_pass_choice      = (
('100','S：100'),
('90','A：90'),
('80','B：80'),
('70','C：70'),
('60','F：60')
)
# Create your models here.
class Review(models.Model):
    lecture               = models.ForeignKey(Lecture, related_name='review')
    title                 = models.CharField(max_length=120, default='No Title')
    comment               = models.TextField(null=True,blank=True)
    rate_pass             = models.CharField(choices=rate_pass_choice,default='80',max_length=20)
    rate_professor        = models.CharField(choices=rate_professor_choice,default='80',max_length=20)
    created_at            = models.DateField(auto_now_add=True)
    student               = models.ForeignKey(Student, null=True)

    def get_url_for_delete(self):
        return reverse('review:delete',kwargs={'pk':self.pk})
    def get_url_for_update(self):
        return reverse('review:update',kwargs={'pk':self.pk})

    def __str__(self):
        return self.title
