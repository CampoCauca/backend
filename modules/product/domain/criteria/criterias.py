from .base_criteria import BaseCriteria

class PriceCriteria(BaseCriteria):
    def __init__(self, minPrice):
        self.minPrice = float(minPrice)
    
    def apply(self, queryset):
        return queryset.filter(stock__valor_venta__lte=self.minPrice)
    
class PriceToZeroCriteria(BaseCriteria):
    def __init__(self, maxPrice):
        self.maxPrice = float(maxPrice)
    
    def apply(self, queryset):
        return queryset.filter(Q(stock__valor_venta__lte=self.maxPrice) & Q(stock__valor_venta__gte=0))

class PriceFromExactCriteria(BaseCriteria):
    def __init__(self, minPrice):
        self.minPrice = float(minPrice)
    
    def apply(self, queryset):
        return queryset.filter(stock__valor_venta__gte=self.minPrice)

class NameCriteria(BaseCriteria):
    def __init__(self, name):
        self.name = name
    
    def apply(self, queryset):
        return queryset.filter(nombre_articulo__icontains=self.name)
    
class CategoryCriteria(BaseCriteria):
    def __init__(self, name):
        self.name = name

    def apply(self, queryset):
        return queryset.filter(categoria__nombre_categoria__icontains=self.name)

class StockCriteria(BaseCriteria):
    def __init__(self, min_stock):
        self.min_stock = min_stock
    
    def apply(self, queryset):
        return queryset.filter(stock__cantidad_actual__gte=self.min_stock)