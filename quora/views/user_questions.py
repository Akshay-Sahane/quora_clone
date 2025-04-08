from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from quora.models.questions import QuestionModel


class UserQuestionListView(ListView):
    paginate_by = 10
    model = QuestionModel
    template_name = 'users/questions.html'

    def get_queryset(self):
        """
        To filter and return questions which are asked by requesting user
        """
        return self.model.objects.filter(
            created_by=self.request.user
        )

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
