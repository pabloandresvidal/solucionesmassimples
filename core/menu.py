from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _
from cms.menu_bases import CMSAttachMenu

class TestMenu(CMSAttachMenu):
    name = _("test menu")

    def get_nodes(self, request):
        nodes = []
        n = NavigationNode(_('Inicio'), "/", 1)
        n2 = NavigationNode(_('Quienes Somos'), "/quienessomos/", 2, 1)
        n3 = NavigationNode(_('Servicios'), "/servicios/", 3, 1)
        n4 = NavigationNode(_('Portafolio'), "/portafolio/", 4, 1)
        n5 = NavigationNode(_('Galeria'), "/galeria/", 5, 1)
        n6 = NavigationNode(_('Cotizador'), "/cotizador/", 6, 1)
        nodes.append(n)
        nodes.append(n2)
        nodes.append(n3)
        nodes.append(n4)
        nodes.append(n5)
        nodes.append(n6)
        return nodes

menu_pool.register_menu(TestMenu)