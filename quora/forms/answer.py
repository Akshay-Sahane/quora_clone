from django import forms

from quora.models.answer import AnswerModel


class AnswerForm(forms.ModelForm):
    class Meta:
        model = AnswerModel
        fields = ['question', 'content']


class AnswerDisplayForm(AnswerForm):
    class Meta:
        model = AnswerModel
        fields = ['content']