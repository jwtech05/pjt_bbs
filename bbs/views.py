from bbs.models import Bbs
from bbs.serializers import BbsSerializer
from rest_framework import generics

class BbsList(generics.ListCreateAPIView):
    queryset = Bbs.objects.all()
    serializer_class = BbsSerializer

class BbsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bbs.objects.all()
    serializer_class = BbsSerializer