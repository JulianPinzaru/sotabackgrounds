from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import random
import requests
import json
from apps.image_inference.serializers import GeneratorRequestSerializer


class GeneratorView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            response = requests.get(settings.MODEL_DOMAIN + 'model/')
            json_response = json.loads(response.content)
            if json_response.get('running'):
                return JsonResponse({'running': True}, status=200)
            return JsonResponse({'running': False}, status=200)
        except:
            return JsonResponse({'running': False}, status=200)

    def post(self, request, *args, **kwargs):
        query_serializer = GeneratorRequestSerializer(data=request.data)
        is_valid = query_serializer.is_valid(raise_exception=False)

        if is_valid:
            print(query_serializer.data)
            response = requests.post(settings.MODEL_DOMAIN + 'model/', data=query_serializer.data)
            result = response.json()
            return Response(result)
        else:
            return Response(query_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


