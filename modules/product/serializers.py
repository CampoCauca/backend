from rest_framework import serializers
from administracion.models import (
    Articulo,
    Categoria,
    Movimiento,
    Stock,
    UnidadDeMedida,
    Imagen,
)


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


class UnidadDeMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadDeMedida
        fields = "__all__"


class MovimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimiento
        fields = "__all__"


class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        fields = "__all__"


class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagen
        fields = "__all__"


class ArticuloSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(source="categoria_id_categoria", read_only=True)
    unidadDeMedida = UnidadDeMedidaSerializer(
        source="unidad_de_medida_idunidad_de_medida", read_only=True
    )

    stock = serializers.SerializerMethodField()
    imagen = serializers.SerializerMethodField()

    class Meta:
        model = Articulo
        fields = [
            "id_articulo",
            "nombre_articulo",
            "descripcion_articulo",
            "categoria",
            "unidadDeMedida",
            "persona_id_persona",
            "stock",
            "imagen",
        ]

    def get_imagen(self, obj):
        try:
            imagenes = Imagen.objects.filter(articulo_id_articulo=obj.id_articulo)
            return ImagenSerializer(imagenes, many=True).data
        except Imagen.DoesNotExist:
            return None

    def get_stock(self, obj):
        try:
            latest_stock = Stock.objects.filter(
                articulo_id_articulo=obj.id_articulo
            ).latest("id_stock")

            return StockSerializer(latest_stock).data
        except Stock.DoesNotExist:
            return None
