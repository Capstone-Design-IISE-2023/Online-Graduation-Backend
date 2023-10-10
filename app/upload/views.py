from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.middleware.csrf import get_token
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.parsers import FormParser, MultiPartParser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from upload.models import Upload
from upload.serializers import FileUploadSerializers

class UploadView(generics.CreateAPIView):
    parser_classes = (MultiPartParser,)
    serializer_class = FileUploadSerializers

    @swagger_auto_schema(method='post',
                        operation_description='Upload images',
                        manual_parameters=[openapi.Parameter(
                            name="image",
                            in_=openapi.IN_FORM,
                            type=openapi.TYPE_FILE,
                            required=True,
                            description="Images"
                            )],
    )
    @action(detail=False, methods=['post'], parser_classes=(MultiPartParser,))
    def post(self, request):
        image = request.FILES['image']
        content_type = image.content_type
        print(f"image: {image}")
        print(f"request: {request}")
        public_uri = Upload.upload_image(image, image.name)
        return HttpResponse(public_uri)
