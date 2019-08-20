from django.urls import path, include
from . import views


from rest_framework import routers

from . views import  QuestionaireViewset , QuestionList

router = routers.DefaultRouter()
#router.register('v1/',QuestionList.as_view())
router.register('questionaire/', QuestionaireViewset)
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/v1/' , QuestionList.as_view())

]