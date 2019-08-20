from django.contrib import admin
from . models import FoodQuestion, Questionaire, GKQuestion , DjangoQuestion
# Register your models here.

admin.site.register(FoodQuestion)
admin.site.register(Questionaire)
admin.site.register(GKQuestion)
admin.site.register(DjangoQuestion)

