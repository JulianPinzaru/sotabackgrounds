from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from schultz.backgrounds_generate import generate_images
from image_generator.serializers import GeneratorRequestSerializer


class call_model(APIView):

    def get(self, request):
        # Ping to determine if service is running
        response = {'running': True}
        return JsonResponse(response, status=200)

    def post(self, request):
        query_serializer = GeneratorRequestSerializer(data=request.data)
        is_valid = query_serializer.is_valid(raise_exception=False)

        if is_valid:
            network = query_serializer.data['network']
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
                seeds=query_serializer.data['seeds'],
                truncation_psi=query_serializer.data['truncation_psi'],
                noise_mode=query_serializer.data['noise_mode'],  # random , None
                outdir='out',
                class_idx=query_serializer.data['class_idx'])
            response = {'image': img_base64_str}
            return Response(response, status=200)
        else:
            return Response(query_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



