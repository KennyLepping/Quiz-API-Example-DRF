from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from .views import (
    RandomQuestionTopic,
    StartQuiz,
    QuizViewSet,
    QuestionViewSet
)

app_name = 'quiz'

router = routers.DefaultRouter()
router.register('quizzes', QuizViewSet)
router.register('questions', QuestionViewSet)

urlpatterns = router.urls

urlpatterns += [
    # path('', Quiz.as_view(), name='quiz'),
    #path('q/', Question.as_view(), name='question'),
    #path('a/', Answer.as_view(), name='answer'),
    path('r/<str:topic>/', RandomQuestionTopic.as_view(), name='RandomQuestionTopic'),
    path('single/<str:title>/', StartQuiz.as_view(), name='quiz'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
