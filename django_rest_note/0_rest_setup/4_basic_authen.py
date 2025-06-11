# setting
"""
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}
"""

# view
"""
from .models import Rest_Api
from .serializers import Rest_ApiSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    queryset = Rest_Api.objects.all()
    serializer_class = Rest_ApiSerializer
    permission_classes = [IsAdminUser]
"""