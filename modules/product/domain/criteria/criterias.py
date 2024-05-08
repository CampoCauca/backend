from .base_criteria import BaseCriteria

class PriceCriteria(BaseCriteria):
    def __init__(self, minPrice):
        self.minPrice = int(minPrice)
    
    def apply(self, queryset):
        return queryset.filter(valor_venta=range(0, self.minPrice))
    
class NameCriteria(BaseCriteria):
    def __init__(self, name):
        self.name = name
    
    def apply(self, queryset):
        return queryset.filter(nombre_articulo=self.name)
    
class CategoryCiteria(BaseCriteria):
    def __init__(self, category):
        self.category = category
    
    def apply(self, queryset):
        return queryset.filter(categoria_id_categoria=self.category)
    
class StockCiteria(BaseCriteria):
    def __init__(self, stock):
        self.stock = stock
    
    def apply(self, queryset):
        return queryset.filter(categoria_id_categoria=self.stock)