from django.contrib import admin
from .models import Imovel


class ImovelAdmin(admin.ModelAdmin):
    list_display = ['endereco', 'thumb']
    search_fields = ['endereco', 'complemento', 'bairro', 'uf']
    actions = None
    list_display_links = None

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Imovel, ImovelAdmin)