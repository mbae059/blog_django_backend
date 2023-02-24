from rest_framework.views import APIView
from .serializers import FeedSerializer, LikeSerializer
from .models import Feed, Like, Comment
from rest_framework.response import Response

class FeedAPI(APIView):
    def get(self, request, nickname, id):
        
        try :
            feed = Feed.objects.get(nickname=nickname, id=id)
        except Feed.DoesNotExist:
            return Response(status=404)
        
        serializer = FeedSerializer(feed)

        return Response(serializer.data)
    
    def post(self, request):
        serializer = FeedSerializer(data=request.data)
        print(serializer)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class LikeAPI(APIView):
    def get(self, request, feed_id):
        print(11111111111)
        likeQueryset = Like.objects.filter(feed_id=feed_id)
        print(1)
        return likeQueryset.size()