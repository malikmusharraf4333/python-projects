from django.db import models

# Create your models here.
class Questionaire(models.Model):
    name = models.CharField(max_length=100,default="")

    def __unicode__(self):
        return self.name
class FoodQuestion(models.Model):
    #question_id = models.IntegerField()
    question = models.TextField(max_length=200,default="")
    option1 = models.CharField(max_length=50,default="")
    option2 = models.CharField(max_length=50, default="")
    option3 = models.CharField(max_length=50, default="")
    option4 = models.CharField(max_length=50, default="")
    answer = models.CharField(max_length=50, default="")
    questionaire = models.ForeignKey(Questionaire,on_delete=models.CASCADE )

    def __unicode__(self):
        return self.question

class GKQuestion(models.Model):
    #question_id = models.IntegerField()
    question = models.TextField(max_length=200,default="")
    option1 = models.CharField(max_length=50,default="")
    option2 = models.CharField(max_length=50, default="")
    option3 = models.CharField(max_length=50, default="")
    option4 = models.CharField(max_length=50, default="")
    answer = models.CharField(max_length=50, default="")
    questionaire = models.ForeignKey(Questionaire,on_delete=models.CASCADE )
    def __unicode__(self):
        return self.question

class DjangoQuestion(models.Model):
    #question_id = models.IntegerField()
    question = models.TextField(max_length=200,default="")
    option1 = models.CharField(max_length=50,default="")
    option2 = models.CharField(max_length=50, default="")
    option3 = models.CharField(max_length=50, default="")
    option4 = models.CharField(max_length=50, default="")
    answer = models.CharField(max_length=50, default="")
    questionaire = models.ForeignKey(Questionaire,on_delete=models.CASCADE )

    def __unicode__(self):
        return self.question



