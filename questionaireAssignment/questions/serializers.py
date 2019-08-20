
from rest_framework import serializers

from .models import Questionaire, FoodQuestion, GKQuestion , DjangoQuestion

class QuestionaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionaire
        fields = '__all__'

class FoodQuestionSerialzer(serializers.ModelSerializer):
    class Meta:
        model = FoodQuestion
        fields = '__all__'

class GKQuestionSerialzer(serializers.ModelSerializer):
    class Meta:
        model = GKQuestion
        fields = '__all__'
class DjangoQuestionSerialzer(serializers.ModelSerializer):
    class Meta:
        model = DjangoQuestion
        fields = '__all__'