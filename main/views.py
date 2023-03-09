from django.shortcuts import render
from rest_auth.views import UserDetailsView
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import DestroyAPIView, ListAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .utils import Weather, News

class FetchWeather(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        #serializer = WeatherSerializer(data=request.data)
        #serializer.is_valid(raise_exception=True)
        cat = request.data.get("category")
        longitude = request.data.get("longitude")
        latitude = request.data.get("latitude")
        #existing_result = None
        if cat == "hourly":
            response, status_code = Weather.hourly(latitude, longitude)
        response, status_code = Weather.daily(latitude, longitude)
        return Response(data=response, status=status_code)

class NewsSources(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return News.getSources()
    

class Headlines(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        