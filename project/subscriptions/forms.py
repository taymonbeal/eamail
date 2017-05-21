from django import forms

from .models import Subscriber

class NewSubscriberForm(forms.ModelForm):

    class Meta:
        model = Subscriber
        fields = ('email', 'interests')
        widgets = { 'interests': forms.CheckboxSelectMultiple }
