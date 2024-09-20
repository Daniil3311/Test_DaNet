from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Data
from .serializers import DataSerializer


# class DataUploadView(APIView):
#     parser_classes = [FileUploadParser]
#
#     def get(self, request):
#         queryset = Data.objects.all()
#         print(queryset)
#         serializer = DataSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def post(self,request):
#         # print(request.data)
#         queryset = Data.objects.all()
#         serializer = DataSerializer(data=request.data)
#         if serializer.is_valid():
#             data_serializers = serializer.save()
#             data_serializers.save()
#             print(serializer)
#             return Response(request.data, status=201)
#         else:
#             print(serializer.errors)
#             return Response(serializer.errors, status=400)
#
class DataUploadView(viewsets.ModelViewSet):
    serializer_class = DataSerializer
    queryset = Data.objects.all()
