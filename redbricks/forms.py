from django import forms
from .models import Reviews


# Modelform for posting reviews
class ReviewPostForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['ratings','comments']