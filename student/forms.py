from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()
department_choice = (
    ('文学部','文学部'),
    ('教育学部','教育学部'),
    ('法学部','法学部'),
    ('経済学部','経済学部'),
    ('情報学部','情報学部'),
    ('理学部','理学部'),
    ('医学部','医学部'),
    ('工学部','工学部'),
    ('農学部','農学部'))


class LoginForm(forms.Form):
  username = forms.CharField()
  password = forms.CharField(widget=forms.PasswordInput)

class StudentForm(forms.Form):
  username = forms.CharField()
  email = forms.CharField()
  department = forms.ChoiceField(widget=forms.RadioSelect,choices=department_choice)
  password = forms.CharField()
  password2 = forms.CharField()


  def clean(self):
    password = self.cleaned_data.get('password')
    password2 = self.cleaned_data.get('password2')
    if password != password2:
      raise forms.ValidationError("password must match")


  def clean_username(self):
    username = self.cleaned_data.get('username')
    qs = User.objects.filter(username=username)
    if qs.exists():
      raise forms.ValidationError("username token")
    return username

  def clean_email(self):
    email = self.cleaned_data.get('email')
    qs = User.objects.filter(email=email)
    if qs.exists():
      raise forms.ValidationError("email token")
    return email