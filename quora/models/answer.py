from django.db import models
from django.conf import settings
from quora.models.questions import QuestionModel


class AnswerModel(models.Model):
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE, related_name='answers')
    content = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Answer by {self.created_by.username} on {self.question.title}"

    def is_upvoted_by(self, user):
        return self.upvotes.filter(id=user.id).exists()
