from django.urls import path
from .views import UserRegisterApi


urlpatterns=[

    path('register/',UserRegisterApi.as_view()),

]
#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