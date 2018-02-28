from django import forms
from .models import Lecture

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
  ('5','5限目')
)
day_choice = (
  ('月','月曜日'),
  ('火','火曜日'),
  ('水','水曜日'),
  ('木','木曜日'),
  ('金','金曜日')
)

class LectureForm(forms.ModelForm):
  class Meta():
    model = Lecture
    fields = (
      'lecture_code',
      'day',
      'time',
      'lecture_type',
      'title',
      'professor_name',
      'location',
      'syllabus',
      'target',
      'description',
      'year',
      'credit',
      # 'created_at'
    )

class LectureSearchForm(forms.Form):
  title =         forms.CharField(required=False)
  lecture_type =  forms.ChoiceField(widget=forms.CheckboxSelectMultiple,choices=lecture_type_choices)
  time =          forms.ChoiceField(widget=forms.CheckboxSelectMultiple,choices=time_choice)
  day =           forms.ChoiceField(widget=forms.CheckboxSelectMultiple,choices=day_choice)
