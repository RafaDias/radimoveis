from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import Imovel
from .forms import ImovelForm


class Home(ListView):
    model = Imovel
    template_name = 'imoveis/home.html'
    context_object_name = 'imoveis'
    paginate_by = 4

    def get_queryset(self):
        filtro = self.request.GET.get('search')
        if not filtro:
            return self.model.objects.all()

        return self.model.objects.pesquisar_pelo_endereco(filtro)


class ImovelDashboard(LoginRequiredMixin, Home):
    template_name = 'imoveis/dashboard.html'


class ImovelCreate(LoginRequiredMixin, CreateView):
    form_class = ImovelForm
    template_name = 'imoveis/imovel_form.html'
    context_object_name = 'form'
    success_url = reverse_lazy('imoveis:dashboard')


class ImovelUpdate(LoginRequiredMixin, UpdateView):
    form_class = ImovelForm
    context_object_name = 'form'
    success_url = reverse_lazy('imoveis:dashboard')

    def get_object(self):
        return Imovel.objects.get(slug=self.kwargs.get('slug', None))


class ImovelDetail(DetailView):
    model = Imovel

    def get_context_data(self, *args, **kwargs):
        context = super(ImovelDetail, self).get_context_data(*args, **kwargs)
        context['imoveis_proximos'] = \
            Imovel.objects.pesquisar_enderecos_proximos(context['imovel'].id)
        return context


class ImovelDelete(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        slug = request.POST.get('slug', None)
        imovel_a_ser_removido = get_object_or_404(Imovel, slug=slug)
        imovel_a_ser_removido.delete()
        return JsonResponse({'message': 'Removido com sucesso!'})


