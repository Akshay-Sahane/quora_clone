from django.urls import path, include

from quora.views.home import HomeView
from quora.views.question import QuestionCreateView, QuestionDetailView, QuestionAnswerView
from quora.views.upvote import AnswerUpvoteView
from quora.views.user_questions import UserQuestionListView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('ask/', QuestionCreateView.as_view(), name='ask_question'),
    path('my_questions', UserQuestionListView.as_view()),
    path('question/<int:question_id>/', QuestionDetailView.as_view(), name='question_detail'),
    path('questions/<int:question_id>/answers', QuestionAnswerView.as_view(), name='question_answer'),
    path('answers/<int:answer_id>/upvote/', AnswerUpvoteView.as_view(), name='answer_upvote')
]
