from django.urls import path
from .views.users import SignUp, SignIn, SignOut, ChangePassword
from .views.plants import PlantsView, PlantView

urlpatterns = [
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-password/', ChangePassword.as_view(), name='change-password'),
    path('plants/', PlantsView.as_view(), name='plants'),
    path('plants/<int:pk>', PlantView.as_view(), name='plant'),
]