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
from apps.image_inference.serializers import


class GeneratorView(APIView):
    def get(self, request, *args, **kwargs):


        asset = kwargs.get('asset', None)
        column = kwargs.get('column', None)
        query_params = dict()
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        query_params['start_date'] = start_date
        query_params['end_date'] = end_date
        query_params['asset'] = asset
        query_params['column'] = column

        query_serializer = ParquetQuerySerializer(data=query_params)
        is_valid = query_serializer.is_valid(raise_exception=False)

        if is_valid:
            collected = self.collect_data(filters=query_params)
            return Response(collected)
        else:
            return Response(query_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def collect_data(self, filters):
        spark = SparkSession.builder.appName('narrativewave').getOrCreate()
        df = spark.read.parquet(str(settings.ROOT_DIR / "resulting_datasets"))
        df.printSchema()

        if filters.get('asset'):
            df = df.filter(df['asset'] == filters['asset'])

        if filters.get('column'):
            df = df.filter(df['column'] == filters['column'])

        if filters.get('start_date'):
            start_date = datetime.date.fromisoformat(filters.get('start_date'))
            df = df.filter(df.date_type > start_date)
            # df.where(df.date_type > start_date)  # alternative way

        if filters.get('end_date'):
            end_date = datetime.date.fromisoformat(filters.get('end_date'))
            df = df.filter(df.date_type < end_date)
            # df.where(df.date_type > end_date)  # alternative way

        result = [row.asDict() for row in df.collect()]

        return result


class call_model(APIView):
    def get(self, request):
        try:
            response = requests.get(settings.MODEL_DOMAIN + 'model/')
            json_response = json.loads(response.content)
            if json_response.get('running'):
                return JsonResponse({'running': True}, status=200)
            return JsonResponse({'running': False}, status=200)
        except:
            return JsonResponse({'running': False}, status=200)

    def post(self, request):
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
