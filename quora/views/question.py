from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django import views
from django.db import transaction

from quora.models.questions import QuestionModel
from quora.forms.question import QuestionForm
from quora.forms.answer import AnswerForm, AnswerDisplayForm


class QuestionCreateView(views.View):
    http_method_names = [
        "get", "post"
    ]

    def get(self, request):
        form = QuestionForm()
        return render(request, 'quora/question.html', {'form': form})

    @method_decorator(login_required)
    def post(self, request):
        with transaction.atomic():
            form = QuestionForm(request.POST)
            if form.is_valid():
                question = form.save()
                question.created_by = request.user
                question.save()
                return redirect('question_detail', question_id=question.id)

            return render(request, 'quora/ask_question.html', {'form': form})


class QuestionDetailView(views.View):
    def get(self, request, question_id):
        question = get_object_or_404(QuestionModel, id=question_id)
        answers = question.answers.all()
        form = AnswerDisplayForm()
        return render(request, 'quora/question_detail.html', {
            'question': question,
            'answers': answers,
            'form': form
        })


class QuestionAnswerView(views.View):

    @method_decorator(login_required)  # user should be logged in to answer to question
    def post(self, request, question_id):
        # to validate forma data and store answer for question
        with transaction.atomic():  # using database transaction
            question = get_object_or_404(QuestionModel, id=question_id)
            request.POST._mutable = True
            request.POST['question'] = question
            form = AnswerForm(request.POST)
            if form.is_valid():
                answer = form.save()
                answer.created_by = request.user
                answer.save()
                return redirect('question_detail', question_id=question.id)
            else:
                # render form again with form errors
                return render(request, 'quora/question_detail.html', {'form': form})
