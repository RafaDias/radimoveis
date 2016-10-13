from django.conf.urls import url
from radimoveis.imoveis.views import Home, ImovelDashboard, ImovelCreate, \
    ImovelUpdate, ImovelDetail, ImovelDelete

urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^dashboard/$', ImovelDashboard.as_view(), name='dashboard'),
    url(r'^new/$', ImovelCreate.as_view(), name='new'),
    url(r'^delete/$', ImovelDelete.as_view(),  name='delete'),
    url(r'^edit/(?P<slug>[\w_-]+)/$', ImovelUpdate.as_view(), name='edit'),
    url(r'^imoveis/(?P<slug>[\w_-]+)/$', ImovelDetail.as_view(), name='detail'),

]
