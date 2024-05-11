import base64
import os
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from administracion.models import Articulo, Imagen
from modules.imagenProducto.serializers import ImagenSerializer


class ImagenProductoViewSet(viewsets.ModelViewSet):
    queryset = Imagen.objects.all()
    serializer_class = ImagenSerializer
    permission_classes = [permissions.AllowAny]

    def generate_unique_name(self, ext):
        """
        Generate a unique name for the image file.
        """

        import time

        timestamp = str(int(time.time()))
        return f"image_{timestamp}.{ext}"

    def get_queryset(self):
        queryset = super().get_queryset()

        idProducto = self.request.GET.get("idProducto")

        if idProducto:
            queryset = queryset.filter(articulo_id_articulo=idProducto)

        return queryset

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "idProducto",
                openapi.IN_QUERY,
                description="ID of the producto",
                type=openapi.TYPE_INTEGER,
            ),
        ],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):

        base64Image = request.data.get("url", None)
        idProducto = request.data.get("articulo_id_articulo", None)
        descripcionImagen = request.data.get("descripcion", None)

        if base64Image:

            try:

                format, imgstr = base64Image.split(";base64,")
                ext = format.split("/")[-1]

                unique_name = self.generate_unique_name(ext)
                file_path = os.path.join("static", "media", "img", unique_name)

                with open(file_path, "wb") as f:
                    f.write(base64.b64decode(imgstr))

                productoInstance = get_object_or_404(Articulo, id_articulo=idProducto)

                Imagen.objects.create(
                    url=file_path,
                    articulo_id_articulo=productoInstance,
                    descripcion=descripcionImagen,
                )

                return Response(status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {"error": "Base64 image data not provided"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    @swagger_auto_schema(auto_schema=None)
    def partial_update(self, request, pk, *args, **kwargs):
        return super().partial_update(request, pk, *args, **kwargs)

    @swagger_auto_schema(auto_schema=None)
    def retrieve(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
