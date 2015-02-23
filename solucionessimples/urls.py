from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.static import serve
from core.views import MisTrabajosList, MisReportesDiariosList, TrabajoView, ReporteDiarioView, VerMisReportesDiariosPorTrabajo,TodosTrabajosList, TodosReportesDiariosList
from core.views import TrabajoView2
from django.contrib.auth.decorators import login_required

admin.autodiscover()

urlpatterns = patterns('core.views',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'index', name='index'),
    url(r'^cotizador/$', 'CotizadorView'),
    url(r'^quienessomos/', TemplateView.as_view(template_name="quienessomos.html")),
    url(r'^galeria/', TemplateView.as_view(template_name="galeria.html")),
    url(r'^portafolio/', TemplateView.as_view(template_name="portafolio.html")),
    url(r'^servicios/', TemplateView.as_view(template_name="servicios.html")),
    url(r'^trabajo/$', login_required(TrabajoView2)),
    url(r'^reporte/$', login_required(ReporteDiarioView)),

    url(r'^dashboard/', login_required(TemplateView.as_view(template_name="dashboard.html"))),
    url(r'^mistrabajos/$', login_required(MisTrabajosList.as_view())),
    url(r'^misreportesdiarios/$', login_required(MisReportesDiariosList.as_view())),
    url(r'^todostrabajos/$', login_required(TodosTrabajosList.as_view())),
    url(r'^todosreportesdiarios/$', login_required(TodosReportesDiariosList.as_view())),

    url(r'^mistrabajos/(?P<trabajo_id>\d+)/$', login_required(VerMisReportesDiariosPorTrabajo)),

    url(r'^login/$', 'login_user'),
    url(r'^logout/$', 'TerminarSesion'),

    url(r'^403/$', 'Error403'),
    url(r'^404/$', 'Error404'),

    url(r'^', include('cms.urls')),
	#url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    #url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
)

if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns
