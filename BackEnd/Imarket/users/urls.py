from django.urls import path
from .views import send_to_email
from .views import RegisterView, LoginView, UserView

urlpatterns = [
    path('register/verify/', send_to_email, name='sending to email'),
    path('user/', UserView.as_view(), name='get correct user'),
    path('register/', RegisterView.as_view(), name='register to the system'),
    path('login/', LoginView.as_view(), name='authorization')
]