from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .models import User
import jwt, datetime
from django.core.exceptions import ValidationError
#returns jwt payload

class RegisterAPI(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
    
class LoginAPI(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = User.objects.filter(email=email).first()
        if user is None :
            raise AuthenticationFailed("User not Found")
        
        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password!")
        
        payload = user.setPayload()
        print(payload)
        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt' : token,
        }
        return response

class LogoutAPI(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message' : 'success',
        }
        return response
    
class IntroductionAPI(APIView):
    def get(self, request): #decide get
        payload = User.getPayload(self, request)
        user = User.objects.get(email=payload['email'])
        serializer = UserSerializer(user)
        print(serializer.data)
        return Response({"introduction" : serializer.data.get("introduction")})
    
    def patch(self, request):
        #receive only introduction
        #authentication is managed via jwt
        payload = User.getPayload(self, request)
        user = User.objects.get(email=payload['email'])
        serializer = UserSerializer(user, data=request.data, partial=True)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(status=200)
        except ValidationError as e:
            return Response({'error': e.detail}, status=400)
        
