from django.db import models
from django.core.urlresolvers import reverse

lecture_type_choices = (
  ('基礎セミナー','基礎セミナー'),
  ('言語文化Ⅰ','言語文化Ⅰ'),
  ('言語文化Ⅱ','言語文化Ⅱ'),
  ('言語文化Ⅲ','言語文化Ⅲ'),
  ('健康・スポーツ科学','健康・スポーツ科学'),
  ('文系基礎科目','文系基礎科目'),
  ('理系基礎科目（文系）','理系基礎科目（文系）'),
  ('理系基礎科目（理系）','理系基礎科目（理系）'),
  ('文系教養科目','文系教養科目'),
  ('理系教養科目','理系教養科目'),
  ('全学教養科目','全学教養科目'),
  ('開放科目','開放科目'),
  ('文学部専門','文学部専門'),
  ('教育学部専門','教育学部専門'),
  ('法学部専門','法学部専門'),
  ('経済学部専門','経済学部専門'),
  ('情報学部専門','情報学部専門/情報文化学部専門'),
  ('理学部専門','理学部専門'),
  ('医学部専門','医学部専門'),
  ('工学部専門','工学部専門'),
  ('農学部専門','農学部専門')
)
time_choice = (
  ('1','1限目'),
  ('2','2限目'),
  ('3','3限目'),
  ('4','4限目'),
  ('5','5限目'))
day_choice = (
  ('1','月曜日'),
  ('2','火曜日'),
  ('3','水曜日'),
  ('4','木曜日'),
  ('5','金曜日'))


class Lecture(models.Model):
  lecture_code          = models.CharField(max_length=120,default='0000000')
  day                   = models.CharField(choices=day_choice,max_length=120,null=True)
  time                  = models.CharField(choices=time_choice,max_length=120,null=True)
  lecture_type          = models.CharField(choices=lecture_type_choices,max_length=120,null=True)
  title                 = models.CharField(max_length=120)
  professor_name        = models.CharField(max_length=120)
  location              = models.CharField(max_length=100,null=True,blank=True)
  syllabus              = models.CharField(max_length=120,null=True,blank=True)
  target                = models.CharField(max_length=120,null=True)
  description           = models.TextField(null=True,)
  year                  = models.CharField(max_length=120)
  credit                = models.DecimalField(max_digits=2, decimal_places=1, default=0)
  created_at            = models.DateField("date published",auto_now_add=True)
  popular               = models.IntegerField(default=0)

  class Meta():
      ordering = ['created_at']

  def get_absolute_url(self):
    return reverse('lecture:detail',kwargs={'pk':self.pk})

  def get_absolute_url_for_update(self):
    return reverse('lecture:update',kwargs={'pk':self.pk})

  def __str__(self):
    return self.title

  def point_add(self, student):
        print("計算開始")
        if self.lecture_type == '基礎セミナー':
            student.grade.basic_seminar += self.credit
        if self.lecture_type == '言語文化Ⅰ':
            student.grade.language_english += self.credit
        if self.lecture_type == '健康・スポーツ科学':
            student.grade.sport += self.credit
        if self.lecture_type == '文系基礎科目':
            student.grade.human_basic += self.credit
        if self.lecture_type == '理系基礎科目（文系）':
            student.grade.science_basic_human += self.credit
        if self.lecture_type == '理系基礎科目（理系）':
            student.grade.science_basic_science += self.credit
        if self.lecture_type == '文系教養科目':
            student.grade.liberal_human += self.credit
        if self.lecture_type == '理系教養科目':
            student.grade.liberal_science += self.credit
        if self.lecture_type == '全学教養科目':
            student.grade.liberal_all =2
        if self.lecture_type == '開放科目':
            student.grade.liberal_free += self.credit
        print(student.user)
        if student.user is not None:
            major = student.department + "専門"
            if self.lecture_type == major:
                student.grade.major += self.credit
        else:
            lecture_type = ['基礎セミナー','言語文化Ⅰ','言語文化Ⅱ','言語文化Ⅲ','健康・スポーツ科学','文系基礎科目','理系基礎科目（文系）','理系基礎科目（理系）','文系教養科目','理系教養科目','全学教養科目','開放科目']
            if not self.lecture_type in lecture_type:
                student.grade.major += self.credit







  def get_score_pass(self):
        if self.get_average_pass() > 95:
            return "S"
        if self.get_average_pass() > 85:
            return "A"
        if self.get_average_pass() > 75:
            return "B"
        if self.get_average_pass() > 65:
            return "C"
        return "F"

  def get_score_professor(self):
        if self.get_average_professor() > 95:
            return "S"
        if self.get_average_professor() > 85:
            return "A"
        if self.get_average_professor() > 75:
            return "B"
        if self.get_average_professor() > 65:
            return "C"
        return "F"

  def get_average_pass(self):
        review_list = self.review.all()
        average_number = 0
        average = 0
        if review_list:
            for review in review_list:
                average += int(review.rate_pass)
                average_number += 1
            average = average / average_number
        average = round(average, 2)
        return average

  def get_average_professor(self):
        review_list = self.review.all()
        average_number = 0
        average = 0
        if review_list:
            for review in review_list:
                average += int(review.rate_professor)
                average_number += 1
            average = average / average_number
        average = round(average, 2)
        return average
  def get_day(self):
        if self.day == '1':
            return '月'
        if self.day == '2':
            return '火'
        if self.day == '3':
            return '水'
        if self.day == '4':
            return '木'
        if self.day == '5':
            return '金'
        return self.day
