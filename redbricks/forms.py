from django import forms
from .models import Reviews


class ReviewPostForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['ratings','comments']