from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from schultz.backgrounds_generate import generate_images
import random

class call_model(APIView):

    def get(self, request):
        if request.method == 'GET':
            # sentence is the query we want to get the prediction for
            params = request.GET.get('sentence')

            G = settings.BACKGROUNDS_MODEL
            response = {'asd': 123}
            # predict method used to get the prediction
            # response = ImageGeneratorConfig.predictor.predict(sentence)

            # returning JSON response
            return JsonResponse(response, status=200)

    def post(self, request):
        if request.method == 'POST':
            network = request.data.get('network')
            seeds = request.data.get('seeds')
            seeds = seeds if seeds else [random.randint(0, 65536)]
            truncation_psi = request.data.get('truncation_psi')
            noise_mode = request.data.get('noise_mode') if request.data.get('noise_mode') else 'none'
            class_idx = request.data.get('class_idx')

            DEVICE = settings.DEVICE
            if network == 'universe_generator':
                GENERATOR = settings.UNIVERSE_MODEL
            elif network == 'backgrounds_generator':
                GENERATOR = settings.BACKGROUNDS_MODEL
            else:
                return JsonResponse({}, status=404)

            img_base64_str = generate_images(
                device=DEVICE,
                generator=GENERATOR,
                process='image',
                seeds=seeds,
                truncation_psi=truncation_psi,
                noise_mode=noise_mode,  # random , None
                outdir='out',
                class_idx=class_idx)
            response = {'image': img_base64_str}
            return JsonResponse(response, status=200)
