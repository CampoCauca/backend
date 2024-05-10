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
from django.shortcuts import get_object_or_404

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

    def create(self, request, *args, **kwargs):
        # Get the base64 encoded image data from the request
        base64Image = request.data.get("url", None)
        idProducto = request.data.get("articulo_id_articulo", None)
        descripcionImagen = request.data.get("descripcion", None)

        if base64Image:

            try:
                # Decode the base64 image data
                format, imgstr = base64Image.split(";base64,")

                ext = format.split("/")[-1]

                # Generate a unique name for the image
                unique_name = self.generate_unique_name(ext)
                # Construct the file path
                file_path = os.path.join("static", "media", "img", unique_name)
                # Decode the base64 data and save it as a file
                with open(file_path, "wb") as f:
                    f.write(base64.b64decode(imgstr))

                productoInstance = get_object_or_404(Articulo, id_articulo=idProducto)

                Imagen.objects.create(
                    url=file_path,
                    articulo_id_articulo=productoInstance,
                    descripcion=descripcionImagen,
                )

                # Return the URL of the saved image
                return Response(status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {"error": "Base64 image data not provided"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def generate_unique_name(self, ext):
        """
        Generate a unique name for the image file.
        """
        # Implement your own logic to generate a unique name
        # For example, you can use UUID or timestamp-based names
        # Here's a simple example using timestamp
        import time

        timestamp = str(int(time.time()))
        return f"image_{timestamp}.{ext}"
