from django import forms
from quora.models.questions import QuestionModel


class QuestionForm(forms.ModelForm):
    class Meta:
        model = QuestionModel
        fields = ['title', 'description']
