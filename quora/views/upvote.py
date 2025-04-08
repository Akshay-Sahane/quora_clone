from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django import views

from quora.models.upvote import AnswerUpvoteModel
from quora.models.answer import AnswerModel
from django.db import transaction


class AnswerUpvoteView(views.View):
    http_method_names = ["post"]

    @method_decorator(login_required)
    def post(self, request, answer_id):
        with transaction.atomic():
            answer = get_object_or_404(AnswerModel, id=answer_id)

            # Check if user already upvoted
            try:
                already_upvoted = AnswerUpvoteModel.objects.get(
                    answer=answer, upvoted_by=request.user
                )
            except AnswerUpvoteModel.DoesNotExist:
                already_upvoted = None

            # if not upvoted create object in model AnswerUpvoteModel
            if not already_upvoted:
                AnswerUpvoteModel.objects.create(answer=answer, upvoted_by=request.user)
            else:
                # is already upvoted then update is_active flag value to its opposite value
                already_upvoted.is_active = not already_upvoted.is_active
                already_upvoted.save()

            return redirect('question_detail', question_id=answer.question.id)
