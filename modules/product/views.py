from urllib import response
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.forms import ValidationError

from administracion.models import (
    Articulo,
    Categoria,
    Movimiento,
    Stock,
    UnidadDeMedida,
    Imagen,
)
from rest_framework import viewsets, permissions
from .serializers import (
    ArticuloSerializer,
    CategoriaSerializer,
    MovimientoSerializer,
    StockSerializer,
    UnidadDeMedidaSerializer,
    ImagenSerializer,
)

from rest_framework import status
from rest_framework.response import Response

import base64
import os
import uuid


class UniqueFileNameGenerator:

    def __init__(self, prefix=""):
        self.prefix = prefix

    def generate(self, extension):
        while True:
            filename = f"{self.prefix}{uuid.uuid4()}.{extension}"
            if not os.path.exists(os.path.join("static/media/img", filename)):
                return filename


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [permissions.AllowAny]


class UnidadDeMedidaViewSet(viewsets.ModelViewSet):
    queryset = UnidadDeMedida.objects.all()
    serializer_class = UnidadDeMedidaSerializer
    permission_classes = [permissions.AllowAny]


class ArticuloViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = super().get_queryset()

        # Get persona_id_persona from URL parameter

        id_persona = self.request.GET.get("idPersona")

        # Filter queryset based on persona_id_persona
        if id_persona:
            queryset = queryset.filter(persona_id_persona=id_persona)

        return queryset


class MovimientoViewSet(viewsets.ModelViewSet):
    queryset = Movimiento.objects.all()
    serializer_class = MovimientoSerializer
    permission_classes = [permissions.AllowAny]


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [permissions.AllowAny]


class UniqueFileNameGenerator:

    def __init__(self, prefix=""):
        self.prefix = prefix

    def generate(self, extension):
        while True:
            filename = f"{self.prefix}{uuid.uuid4()}.{extension}"
            if not os.path.exists(os.path.join("static/media/img", filename)):
                return filename


class ImagenViewSet(viewsets.ModelViewSet):
    queryset = Imagen.objects.all()
    serializer_class = ImagenSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            # Extract base64 data from the request
            image_data = serializer.validated_data["image"]
            print("LLEGA AQUI")
            format, imgstr = image_data.split(";base64,", 1)
            ext = format.split("/")[-1]  # Extract image extension
            
            # Validate base64 content
            if ext not in ["jpg", "jpeg", "png"]:
                raise ValidationError("Unsupported image format.")
            if not base64.b64decode(imgstr):
                raise ValidationError("Invalid base64 data.")

            # Decode base64 data and create a ContentFile object
            decoded_content = base64.b64decode(imgstr)
            content_file = ContentFile(decoded_content, name=f"image.{ext}")

            # Generate a unique filename
            unique_filename_generator = UniqueFileNameGenerator()
            unique_filename = unique_filename_generator.generate(ext)

            # Save the image to the static/media/img folder (modify if needed)
            image_path = default_storage.save(
                os.path.join("static/media/img", unique_filename), content_file
            )
            
            
            image_url = default_storage.url(image_path)  # Get the image URL

            # Return a success response with the image URL
            return response({"image_url": image_url}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
