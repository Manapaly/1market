import random
import string
import time

from django.shortcuts import render
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from orders.models import Order
from rest_framework.response import Response

from datetime import datetime
from django.conf import settings
from rest_framework_simplejwt import exceptions
from rest_framework_simplejwt.utils import datetime_to_epoch, format_lazy
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

random.seed(time.time())


@csrf_exempt
def send_to_email(request):
    if request.method == 'POST':
        email = request.POST['email']

        send_mail(
            subject='Verification',
            message=f'Verification code for registration : {RegisterView.random_gen_code}',
            from_email='settings.EMAIL_HOST_USER',
            recipient_list=[email, ],
            fail_silently=False
        )

    return render(request, 'index.html')


class RegisterView(APIView):
    random_gen_code = ''.join(random.choice(string.digits) for i in range(6))

    def post(self, request):
        # code = request['code']

        # if code != RegisterView.random_gen_code:
        #     raise ValidationError("Verify code doesn't satisfy")

        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        if (serializer.data["user_type"] == "Customer"):
            new_order = Order(user=User.objects.get(id=serializer.data["id"]))
            new_order.save()
        else:
            print("\n\n---SELLER IS CREATED----\n\n")

        return Response(serializer.data)

