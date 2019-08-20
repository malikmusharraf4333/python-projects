from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.utils import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import FoodQuestion, Questionaire, GKQuestion , DjangoQuestion
from . serializers import QuestionaireSerializer, FoodQuestionSerialzer, GKQuestionSerialzer, DjangoQuestionSerialzer

from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.

SelectedQuestionaire = None

# class QuestionViewset(viewsets.ModelViewSet):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerialzer

class QuestionaireViewset(viewsets.ModelViewSet):
    serializer_class = QuestionaireSerializer
    queryset = Questionaire.objects.all()

class QuestionList(APIView):


     def get(request, self):
         allQuestions = FoodQuestion.objects.all()
         serializer = FoodQuestionSerialzer(allQuestions, many=True)
         return Response(serializer.data)

     def post(self, request , format = None):
         body_unicode = request.body.decode('utf-8')
         body = json.loads(body_unicode)
         id = body['questionaireID']
         questionCounter = body['QuestionID']
         #answer = body['answer']
         if id == 1:
             allQuestions = FoodQuestion.objects.get(pk = questionCounter)
             serializer = FoodQuestionSerialzer(allQuestions)
             return Response(serializer.data)
         if id == 2:
             allQuestions = GKQuestion.objects.get(pk=questionCounter)
             serializer = GKQuestionSerialzer(allQuestions, many = False)
             return Response(serializer.data)
         if id == 3:
             allQuestions = DjangoQuestion.objects.get(pk=questionCounter+3)
             serializer = DjangoQuestionSerialzer(allQuestions)
             return Response(serializer.data)





         #id = request.POST.get('questionaireID')


         print ("hello")

