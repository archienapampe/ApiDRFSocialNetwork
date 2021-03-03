from django.contrib.auth import authenticate, get_user_model
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.permissions import AllowAny
from activity_log.models import ActivityLog
from django.db.models import Max

from .serializers import (
    UserSerializer,
    LastActivityModelSerializer,
    LastLoginModelSerializer,
)

User = get_user_model()


@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if username is None or password is None:
        return Response({'error': 'Please, enter user name and password'})
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid data'})

    user.last_login = timezone.now()
    user.save(update_fields=['last_login'])
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key}, status=HTTP_200_OK)


class CreateUser(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


class LastLoginRetrieveApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = LastLoginModelSerializer


class LastActivityRetrieveApiView(ListAPIView):
    queryset = ActivityLog.objects.values('user').annotate(datetime=Max('datetime'))
    serializer_class = LastActivityModelSerializer
