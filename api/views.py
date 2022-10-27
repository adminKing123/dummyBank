from rest_framework import viewsets
from rest_framework import permissions
from .serializers import RecordSerializer
from .models import Record, Total
from django.http import JsonResponse
import json

class RecordViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Records to be viewed or edited.
    """
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'post']


def total_value(request):
    data = {"total": Total.objects.first().total}
    return JsonResponse(data)