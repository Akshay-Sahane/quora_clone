from quora.models.questions import QuestionModel
from django.views.generic import ListView


class HomeView(ListView):
    paginate_by = 10  # set pagination size
    model = QuestionModel
    template_name = 'home.html'
