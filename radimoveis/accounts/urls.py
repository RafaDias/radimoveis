from django.conf.urls import url
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'entrar/$', login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'sair/$', logout, {'next_page': 'imoveis:home'}, name='logout'),
]
