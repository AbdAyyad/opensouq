from django.shortcuts import render
from rest_framework.views import APIView, Response
# import hamming_distance, levenstion_distance
from . import hamming_distance
from . import levenstion_distance

class hamming_api(APIView):
    def post(self, request, format=None):
        string_one = request.data['string_one']
        string_two = request.data['string_two']

        hamming = hamming_distance.hamming_distance(string_one, string_two)

        return Response({'hamming': hamming.distance})

class levenstion_api(APIView):
    def post(self, request, format=None):
        string_one = request.data['string_one']
        string_two = request.data['string_two']

        levenstion = levenstion_distance.levention_distance(string_one, string_two)
       
        return Response({'levenstion': levenstion.distance})

