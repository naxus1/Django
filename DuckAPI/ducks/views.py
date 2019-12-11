from rest_framework import generics
from ducks.models import Duck
from ducks.serializer import DuckSerializer
from django.shortcuts import get_object_or_404


# Create your views here.

class DuckList(generics.ListCreateAPIView):
    queryset = Duck.objects.all()
    serializer_class = DuckSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj