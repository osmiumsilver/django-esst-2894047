from django import forms

from .models import Notes
class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')
        labels = {
            'text': 'Note text',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'})
        }
    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' in title:
            raise forms.ValidationError('Non-Django not allowed')
        return title