from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta():
        model = Review
        fields = (
        # 'lecture',
        'title',
        'comment',
        'rate_pass',
        'rate_professor',
        # 'created_at',
        )
