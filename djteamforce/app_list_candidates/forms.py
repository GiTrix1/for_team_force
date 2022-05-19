from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Profile


class CreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=70, required=False)
    middle_name = forms.CharField(max_length=70, required=False)
    last_name = forms.CharField(max_length=70, required=False)
    skills = forms.CharField(max_length=500, required=False)
    language = forms.CharField(max_length=50, required=False)
    hobbies = forms.CharField(max_length=500, required=False)

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''


class SkillsForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('skills', )
