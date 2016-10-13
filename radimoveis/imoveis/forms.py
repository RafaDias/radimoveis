from django.forms import ModelForm


from .models import Imovel


class ImovelForm(ModelForm):
    class Meta:
        model = Imovel
        exclude = ('criado_em', 'slug', 'lat', 'lng')
