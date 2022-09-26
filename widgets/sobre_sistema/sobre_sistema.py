import gi

try:
    gi.require_version(namespace='Gtk', version='4.0')
except(ValueError, ImportError):
    print("Erro version:{}{}".format(ValueError, ImportError))
try:
    gi.require_version(namespace='GdkPixbuf', version='2.0')
except (ValueError, ImportError):
    print("Erro version:{}{}".format(ValueError, ImportError))

from gi.repository import GdkPixbuf
from gi.repository import Gtk, Gdk
from geral.geral import Geral

class SobreSistema:
    """Janela do AboutDialog"""

    def __init__(self, parent):


        self.x = Gtk.AboutDialog()

        self.parent = parent
        self.x.set_transient_for(self.parent)

        self.x.set_program_name("CTRL Controle")
        self.x.set_name("AutoKey")

        self.x.set_modal(modal=True)
        self.x.set_resizable(False)
        self.x.set_comments("Sistema de montagem de preço")

        # colocar logo no aboutdialog
        # pixbuf = GdkPixbuf.Pixbuf.new_from_file(
        #     "/home/john/Documentos/sistemas/python/desktop/gtk4/ctrl/icons/mensagem_informativo_mod1.png")
        # texture = Gdk.Texture.new_for_pixbuf(pixbuf)
        # self.x.set_logo(texture)
        # --------------------------

        version = '{}.{}.{}'.format("ALPHA", "0", 1)
        self.x.set_version(version)

        # dlg.set_website(common.HOMEPAGE)
        self.x.set_authors(["John Evan Dizaro (Desenvolvedor) <johndizaro@gmail.com>", ])

        self.x.show()

        # self.run()
        # self.dlg.destroy()
        # del self.dlg
