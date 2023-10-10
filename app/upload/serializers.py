from rest_framework import parsers, renderers, serializers, status


class FileUploadSerializers(serializers.Serializer):
    image = serializers.ImageField()

    class Meta:
        fields = ['image']
