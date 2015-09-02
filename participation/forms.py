from django import forms
from django.forms.models import ModelForm, ModelFormMetaclass
from models import Participation

class ParticipationForm(forms.ModelForm):

    class Meta:
        model = Participation
        fields = ('name', 'age','email', 'phone')