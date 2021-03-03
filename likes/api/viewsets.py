from rest_framework import views
from rest_framework.response import Response

from ..models import Like


class CountLikesApiView(views.APIView):

    def get(self, request):
        date_from = request.query_params.get('date_from')
        date_to = request.query_params.get('date_to')

        likes_count = Like.objects.filter(
            date__range=(date_from, date_to)
            ).count()
        return Response({'count likes': likes_count})
