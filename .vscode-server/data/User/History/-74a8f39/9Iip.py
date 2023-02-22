from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import ImageSerializer
import os
from .models import Image
from uuid import uuid4
from backend.settings import MEDIA_ROOT, MEDIA_URL
from rest_framework.exceptions import AuthenticationFailed
import jwt 
from User.models import User



class ImageAPIView(APIView):
    #view images
    def get(self, request, uuid_name) :
        imageQueryset = Image.objects.filter(uuid_name = uuid_name)
        
        #if image does not exists
        if not imageQueryset.exists() :
            return Response(404)
        
        image = imageQueryset.first()
        serializer = ImageSerializer(image)

        image_url = os.path.join(MEDIA_URL, uuid_name)
        response = {
            'image_url': image_url
        }
        print(response)
        return Response(response)

    def post(self, request):

        # 일단 파일 불러와
        image = request.FILES.get('image')
        name = image.name

        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)
        save_path += '.jpeg'
        #save file

        token = request.COOKIES.get('jwt')

        if not token :
            raise AuthenticationFailed("Unauthenticated")

        try :
            payload = jwt.decode(token, 'secret', algorithms=['HS256']) #json file
            user = User.objects.get(email=payload['email'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unauthenticated")


        serializer = ImageSerializer(data={'name':name, 'userEmail': user.email, 'uuid_name':uuid_name}) #use dict for creating

        if serializer.is_valid() :
            with open(save_path, 'wb+') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)
            serializer.save()
            return Response(status=200)
        else :
            return Response(status=400)
    
    #do not change the content of the image but only name
    def put(self, request, uuid_name) :
        imageQueryset = Image.objects.get(uuid_name=uuid_name)

        if not imageQueryset.exists():
            return Response(404)
        
        image = imageQueryset.first()

        imageBeforeName = image.get('name')
        imageAfterName = request.data.get('name')

        serializer = ImageSerializer(image, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)