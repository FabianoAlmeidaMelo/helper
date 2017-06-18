from django.contrib import admin
from helper.contabil.models import Contador

class ContadorAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(course=None)

admin.site.register(Contador, ContadorAdmin)
