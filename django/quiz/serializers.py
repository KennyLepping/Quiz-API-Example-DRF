from rest_framework import serializers
from .models import Quizzes, Question, Answer


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:

        model = Answer
        fields = [
            'id',
            'answer_text',
            'is_right',
        ]


# List Quizzes
class QuizSerializer(serializers.ModelSerializer):

    #question = serializers.StringRelatedField(many=True)
    answer_set = AnswerSerializer(many=True, read_only=True)

    class Meta:

        model = Quizzes
        fields = [
            'title', 'question', 'answer_set',
        ]
        depth = 1


class RandomQuestionSerializer(serializers.ModelSerializer):

    # answer = serializers.StringRelatedField(many=True)
    # answer = AnswerSerializer(many=True, read_only=True)

    class Meta:

        model = Question
        fields = [
            'title',
            'answer',
        ]
        depth = 1


class QuestionSerializer(serializers.ModelSerializer):

    # answer = serializers.StringRelatedField(many=True)
    # answer = AnswerSerializer(many=True, read_only=True)

    class Meta:

        model = Question
        fields = [
            'quiz',
            'title',
            'answer',
        ]
        depth = 1
