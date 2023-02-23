from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime

class User(AbstractUser):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    introduction = models.TextField(default="default")
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def getPayload(self, request):
        token = request.COOKIES.get('jwt')

        if not token :
            raise AuthenticationFailed("Unauthenticated")

        try :
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unauthenticated")
        return payload
    
    def setPayload(self) :
        payload = {
            'id': self.id,
            'email' : self.email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        return payload
    
    class Meta:
        db_table = "User"