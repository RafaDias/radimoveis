from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from .choices import UF


class ImovelManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(endereco__icontains=query)


class Imovel(models.Model):
    breve_descricao = models.CharField(_('Breve descrição'), max_length=40)
    endereco = models.CharField(_('Endereço'), max_length=80, null=True, blank=True)
    slug = models.SlugField(_('Atalho'), unique=True)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    telefone = models.CharField(_('Telefone'), max_length=20, null=True, blank=True)
    complemento = models.CharField(_('Complemento'), max_length=30, null=True, blank=True)
    uf = models.CharField(
        _('UF'), max_length=2, blank=False, null=True, choices=UF
    )
    bairro = models.CharField(_('Bairro'), max_length=20, null=True, blank=True)
    imagem = models.ImageField(_('Imagem'), upload_to='img')
    criado_em = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    detalhes = models.TextField(_('Descrição'))
    objects = ImovelManager()

    def thumb(self):
        return mark_safe(u'<img src="%s" width=150 height=150 />' % (self.imagem.url))

    thumb.short_description = _('Imagem')

    def __str__(self):
        return self.breve_descricao

    class Meta:
        db_table = "Imovel"
        ordering = ('-criado_em',)
        verbose_name = 'Imóvel'
        verbose_name_plural = 'Imóveis'