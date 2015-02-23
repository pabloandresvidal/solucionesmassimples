from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _
from core.menu import TestMenu

class SolucionesSimplesApp(CMSApp):
    name = _("SolucionesSimples App") # give your app a name, this is required
    ##urls = ["solucionessimples.urls"] # link your app to url configuration(s)
    menus = [TestMenu]

apphook_pool.register(SolucionesSimplesApp) # register your app