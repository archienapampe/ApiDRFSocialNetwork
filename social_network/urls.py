from django.contrib import admin
from django.urls import path, include

from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('api/post/', include('posts.api.urls')),
    path('api/user/', include('users.api.urls')),
    path('api/likes/', include('likes.api.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/',
         include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += doc_urls
