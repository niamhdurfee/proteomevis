from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^fetch_edges/$', views.fetch_edges, name='fetch_edges'),
    url(r'^fetch_proteins/$', views.fetch_proteins, name='fetch_proteins'),
    url(r'^fetch_edge/$', views.fetch_edge, name='fetch_edge'),
    url(r'^export_nodes/$', views.export_nodes, name='export_nodes'),
    url(r'^export_edges/$', views.export_edges, name='export_edges'),
    url(r'^export_splom/$', views.export_splom, name='export_splom'),
    url(r'^query/$', views.query, name='query'),
]
