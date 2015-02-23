# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import authenticate, login, logout

from django.views.generic import ListView, CreateView

from models import *
from forms import *
from datetime import *
import random
from django.conf import settings

from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.db.models import Q

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    return render_to_response('index.html',
                              context_instance=RequestContext(request))

class MisTrabajosList(ListView):
    model = Trabajo
    #paginate_by = 10
    #ordering = ['fecha_creacion']

    def get_queryset(self):
        return Trabajo.objects.filter(user=self.request.user).order_by('-id')

class TodosTrabajosList(ListView):
    model = Trabajo

    #paginate_by = 10

class MisReportesDiariosList(ListView):
    model = ReporteDiario

    def get_queryset(self):
        return ReporteDiario.objects.filter(user=self.request.user)

class TodosReportesDiariosList(ListView):
    model = ReporteDiario

def VerMisReportesDiariosPorTrabajo(request, trabajo_id):

    objeto_trabajo = get_object_or_404(Trabajo,id = trabajo_id)

    try:
        objeto_reporte_diario = ReporteDiario.objects.filter(trabajo = objeto_trabajo)
        objeto_cotizacion_item = ItemCotizacion.objects.filter(trabajo = objeto_trabajo)
    except:
        objeto_report_diario = []
        objeto_cotizacion_item = []

    # paginator = Paginator(objeto_reporte_diario, 3)
    # page = request.GET.get('page')
    # try:
    #     objeto_reporte_diario = paginator.page(page)
    #
    # except PageNotAnInteger:
    #     # If page is not an integer, deliver first page.
    #     objeto_reporte_diario = paginator.page(1)
    #
    # except EmptyPage:
    #     # If page is out of range (e.g. 9999), deliver last page of results.
    #     objeto_reporte_diario = paginator.page(paginator.num_pages)

    context = {'objeto_reporte_diario': objeto_reporte_diario,
               'objeto_cotizacion_item':objeto_cotizacion_item,
               'objeto_trabajo':objeto_trabajo,
               }
    return render_to_response('core/trabajo_report_list.html',
                              context,
                              context_instance=RequestContext(request))

def CotizadorView(request):
    """
    Allow input of data on persona
    """
    mensajeEstado = ""
    form = None
    try:
        if request.method == "POST":
            form = CotizadorForm(request.POST)
            if form.is_valid():
                form.save()

                plaintext = get_template('email.txt')
                htmly     = get_template('email.html')

                data = form.cleaned_data

                d = Context({ 'user': request.user,
                              'form': data,
                              'STATIC_URL': settings.STATIC_URL})

                subject, from_email, to = 'Nueva Cotización de Soluciones + Simples', 'gerencia@solucionesmassimples.com', 'pabloandresvidal@gmail.com'

                text_content = plaintext.render(d)
                html_content = htmly.render(d)

                msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()

                #########################################Email para el usuario###############################
                plaintext = get_template('email.txt')
                htmly     = get_template('email.html')

                data = form.cleaned_data

                d = Context({ 'user': request.user,
                              'form': data,
                              'STATIC_URL': settings.STATIC_URL})

                subject, from_email, to = 'Su Cotización ha sido recibida - Soluciones + Simples', 'gerencia@solucionesmassimples.com', request.POST['email']

                text_content = plaintext.render(d)
                html_content = htmly.render(d)

                msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()

                ##send_mail('Nueva Cotización', 'Nueva Cotización', 'gerencia@solucionesmassimples.com',['pabloandresvidal@gmail.com'], fail_silently=False)

                mensajeEstado = u'La información fue enviada exitosamente.'
                tipoMensajeEstado = 'true'
            else:
                mensajeEstado = u'No fue posible enviar la información, por favor vuelva a intentarlo.'
                tipoMensajeEstado = 'false'        
        else:
            form = CotizadorForm()
            print form
    except Exception, e:
        print "Error del Sistema  ", e
        print request.POST, "REQUEST########################", e
    context = {'form': form,
               'mensajeEstado': mensajeEstado,}
    return render_to_response('cotizador.html',
                              context,
                              context_instance=RequestContext(request))


def TrabajoView(request):
    mensajeEstado = ""
    form = None
    try:
        if request.method == "POST":
            form = TrabajoForm(request.POST)
            if form.is_valid():
                trabajo = form.save(commit=False)
                trabajo.user = request.user
                trabajo.save()
                #send_mail('Nueva Cotización', 'Nueva Cotización', 'gerencia@solucionesmassimples.com',['pabloandresvidal@gmail.com'], fail_silently=False)
                mensajeEstado = u'La información fue enviada exitosamente.'
                tipoMensajeEstado = 'true'
            else:
                mensajeEstado = u'No fue posible enviar la información, por favor vuelva a intentarlo.'
                tipoMensajeEstado = 'false'
        else:
            form = TrabajoForm()
            print form
    except Exception, e:
        print "Error del Sistema  ", e
        print request.POST, "REQUEST########################", e
    context = {'form': form,
               'mensajeEstado': mensajeEstado,}
    return render_to_response('trabajo.html',
                              context,
                              context_instance=RequestContext(request))

def ReporteDiarioView(request):
    mensajeEstado = ""
    try:
        if request.POST:
            form = ReporteDiarioForm(request.POST)
            if form.is_valid():
                reporte = form.save(commit=False)
                reporte.user = request.user

                trabajo_id = request.POST['trabajo']

                objeto_trabajo = Trabajo.objects.get(id = trabajo_id)
                reporte.trabajo = objeto_trabajo

                reporte.report = request.POST['report']

                if 'foto1' in request.FILES:
                    image_file = request.FILES['foto1']
                    reporte.foto1.save(image_file.name, image_file)

                if 'foto2' in request.FILES:
                    image_file = request.FILES['foto2']
                    reporte.foto2.save(image_file.name, image_file)

                if 'foto3' in request.FILES:
                    image_file = request.FILES['foto3']
                    reporte.foto3.save(image_file.name, image_file)

                if 'foto4' in request.FILES:
                    image_file = request.FILES['foto4']
                    reporte.foto4.save(image_file.name, image_file)

                reporte.save()

                #send_mail('Nueva Cotización', 'Nueva Cotización', 'gerencia@solucionesmassimples.com',['pabloandresvidal@gmail.com'], fail_silently=False)
                mensajeEstado = u'La información fue enviada exitosamente.'
                tipoMensajeEstado = 'true'
            else:
                mensajeEstado = u'No se pudo enviar la información, por favor vuelva a intentarlo.'
                tipoMensajeEstado = 'false'
        else:
            form = ReporteDiarioForm(user=request.user)
            print form
    except Exception, e:
        print "Error del Sistema  ", e
    return render_to_response("reporte.html", {
        "form": form,
        "mensajeEstado":mensajeEstado,
    }, context_instance=RequestContext(request))

def TrabajoView2(request):
    cotizacion_formset = CotizacionFormSet()
    mensajeEstado = ""

    if request.POST:
        form = TrabajoForm(request.POST)
        if form.is_valid():
            trabajo = form.save(commit=False)
            trabajo.user = request.user
            cotizacion_formset = CotizacionFormSet(request.POST, instance=trabajo)
            if cotizacion_formset.is_valid():
                trabajo.save()
                cotizacion_formset.save()
                return HttpResponseRedirect("/mistrabajos/")
        else:
            cotizacion_formset = CotizacionFormSet(request.POST)
            mensajeEstado = "No fue posible crear el trabajo, por favor verifique la información."
    else:
        form = TrabajoForm()
        cotizacion_formset = CotizacionFormSet(instance=Trabajo())
    return render_to_response("trabajo_form.html", {
        "form": form,
        "mensajeEstado":mensajeEstado,
        "cotizacion_formset": cotizacion_formset,
    }, context_instance=RequestContext(request))


def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/dashboard')
    return render_to_response('login.html', context_instance=RequestContext(request))

def TerminarSesion(request):
    logout(request)
    return HttpResponseRedirect(reverse(index))

def Error403(request):
    return render_to_response("403.html", {
    }, context_instance=RequestContext(request))

def Error404(request):
    return render_to_response("404.html", {
    }, context_instance=RequestContext(request))