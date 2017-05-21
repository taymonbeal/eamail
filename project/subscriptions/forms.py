from django import forms

from .models import Subscriber

class NewSubscriberForm(forms.ModelForm):

    class Meta:
        model = Subscriber
        fields = ('email', 'interests')

    def save(self, *args, **kwargs):
        if self.token is None:
            self.token = Token()
            self.token.save()
        super(Subscriber, self).save(*args, **kwargs)
