class BaseCriteria:
    def apply(self, queryset):
        raise NotImplementedError()