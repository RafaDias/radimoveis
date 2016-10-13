from geopy.distance import vincenty as distancia_em_km
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save
from django.shortcuts import resolve_url
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from .geolocation import location_a_partir_do
from .choices import UF


class ImovelManager(models.Manager):
    def pesquisar_pelo_endereco(self, query):
        return self.get_queryset().filter(
            models.Q(endereco__icontains=query) | \
            models.Q(bairro__icontains=query) | \
            models.Q(uf__icontains=query)
        )

    def pesquisar_enderecos_proximos(self, id):
        location = self.get_queryset().get(id=id).location()
        imoveis_proximos = set()
        for imovel in self.get_queryset().exclude(id=id):
            if distancia_em_km(location, imovel.location()).kilometers <= 1.0:
                imoveis_proximos.add(imovel)

        return imoveis_proximos


class Imovel(models.Model):
    breve_descricao = models.CharField(_('Breve descrição'), max_length=40)
    slug = models.SlugField(_('Atalho'), unique=True)
    endereco = models.CharField(_('Endereço'), max_length=80, null=True, blank=True)
    preco = models.DecimalField(_('Preço'), max_digits=8, decimal_places=2)
    telefone = models.CharField(_('Telefone'), max_length=20, null=True, blank=True)
    complemento = models.CharField(_('Complemento'), max_length=30, null=True, blank=True)
    uf = models.CharField(
        _('UF'), max_length=2, blank=False, null=True, choices=UF
    )
    bairro = models.CharField(_('Bairro'), max_length=20, null=True, blank=True)
    imagem = models.ImageField(_('Imagem'), upload_to='img')
    criado_em = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    detalhes = models.TextField(_('Descrição'))
    lat = models.FloatField(default=0)
    lng = models.FloatField(default=0)
    objects = ImovelManager()

    def thumb(self):
        return mark_safe(u'<img src="%s" width=150 height=150 />' % self.imagem.url)

    thumb.short_description = _('Imagem')

    def __str__(self):
        return self.breve_descricao

    def endereco_completo(self):
        return "{} - {} {} - {}".format(
            self.endereco, self.complemento, self.bairro, self.uf)

    def location(self):
        return self.lat, self.lng

    def get_absolute_url(self):
        return resolve_url('imoveis:detail', slug=self.slug)

    class Meta:
        db_table = "Imovel"
        ordering = ('-criado_em',)
        verbose_name = 'Imóvel'
        verbose_name_plural = 'Imóveis'


def pre_save_imovel_signal_receiver(sender, instance, *args, **kwargs):

    # configura slug
    slug = slugify(instance.breve_descricao)
    existe = Imovel.objects.filter(slug=slug).exists()
    if existe:
        slug = "{}-{}".format(slug, instance.id)
    instance.slug = slug

    # configura location
    location = location_a_partir_do(instance.endereco_completo())
    if location:
        instance.lat, instance.lng = location['lat'], location['lng']

pre_save.connect(pre_save_imovel_signal_receiver, sender=Imovel)
