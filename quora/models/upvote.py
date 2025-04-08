from django.db import models

from quora.models.answer import AnswerModel
from django.conf import settings


class AnswerUpvoteModel(models.Model):
    answer = models.ForeignKey(AnswerModel, on_delete=models.CASCADE, related_name='upvotes')
    upvoted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    upvoted_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('answer', 'upvoted_by')  # ensures one upvote per user per answer
