class BaseCriteria:
    def apply(self, queryset):
        if not queryset:
            return queryset
        raise NotImplementedError()