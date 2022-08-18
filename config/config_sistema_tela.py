import gi

gi.require_version(namespace='Gtk', version='4.0')
from gi.repository import Gtk
# gi.require_version(namespace='Adw', version='1.0')

import platform


class ConfigSistemaTela(Gtk.ApplicationWindow):
    def __init__(self):
        super(ConfigSistemaTela, self).__init__()
        self.set_title(title='Configuração do Sistema')

        vbox_window = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL,spacing=12)


        # vbox_window.set_margin_top(margin=12)
        # vbox_window.set_margin_end(margin=12)
        # vbox_window.set_margin_bottom(margin=12)
        # vbox_window.set_margin_start(margin=12)

        self.set_child(child=vbox_window)
        # self.set_position(Gtk.WindowPosition.CENTER)

        frame_caminhos = Gtk.Frame.new("Caminhos")
        self.set_child(child=frame_caminhos)

        vbox_frame_caminhos = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        frame_caminhos.set_child(child=vbox_frame_caminhos)

        lb_caminho_sistema = Gtk.Label.new()
        lb_caminho_sistema.set_xalign(0)
        lb_caminho_sistema.get_style_context().add_class(class_name='caption-heading')
        lb_caminho_sistema.set_markup(str="Caminho do sistema")
        vbox_frame_caminhos.append(child=lb_caminho_sistema)

        entry1 = Gtk.Entry.new()
        entry1.set_text(text='Entry com a classe warning')
        entry1.get_style_context().add_class(class_name='warning')
        entry1.set_icon_from_icon_name(
            icon_pos=Gtk.EntryIconPosition.SECONDARY,
            icon_name='system-search-symbolic',
        )
        vbox_frame_caminhos.append(child=entry1)

        lb2 = Gtk.Label.new()
        lb2.set_xalign(0)
        lb2.get_style_context().add_class(class_name='caption-heading')
        lb2.set_markup(str="Caminho do sistema")
        vbox_frame_caminhos.append(child=lb2)

        entry2 = Gtk.Entry.new()
        entry2.set_text(text='Entry com a classe regular')
        entry2.get_style_context().add_class(class_name='regular')
        entry2.set_icon_from_icon_name(
            icon_pos=Gtk.EntryIconPosition.SECONDARY,
            icon_name='system-search-symbolic',
        )
        vbox_frame_caminhos.append(child=entry2)

        lb3 = Gtk.Label.new()
        lb3.set_xalign(0)
        lb3.get_style_context().add_class(class_name='caption-heading')
        lb3.set_markup(str="Caminho do sistema")
        vbox_frame_caminhos.append(child=lb3)

        entry3 = Gtk.Entry.new()
        entry3.set_text(text='Entry com a classe success')
        entry3.get_style_context().add_class(class_name='success')
        entry3.set_icon_from_icon_name(
            icon_pos=Gtk.EntryIconPosition.SECONDARY,
            icon_name='system-search-symbolic',
        )
        vbox_frame_caminhos.append(child=entry3)

        lb4 = Gtk.Label.new()
        lb4.set_xalign(0)
        lb4.get_style_context().add_class(class_name='caption')
        lb4.set_markup(str="")
        vbox_frame_caminhos.append(child=lb4)

        entry4 = Gtk.Entry.new()
        entry4.set_text(text='Entry com a classe error')
        entry4.get_style_context().add_class(class_name='error')
        entry4.set_icon_from_icon_name(
            icon_pos=Gtk.EntryIconPosition.SECONDARY,
            icon_name='system-search-symbolic',
        )
        vbox_frame_caminhos.append(child=entry4)

        self.show()

    def popular_tela(self):
        pass

    def on_key_enter_pressed(self, Entry):
        print(f'Valor digitado no entry: {Entry.get_text()}')

    def on_icon_pressed(self, Entry, EntryIconPosition):
        print(f'Valor digitado no entry: {Entry.get_text()}')

    def mostrar_config_tela(self):
        dic_dados = dict()

        so = platform.system()
        dic_dados["system"] = so
        match so:
            case 'Linux':
                pass
            case 'Darwin':
                pass
            case 'Java':
                pass
            case 'Windows':
                pass
            case _:
                pass

        # try:
        #     dic_dados["system"] = platform.system()
        # except (ValueError, ImportError):
        #     dic_dados["system"] = "Não determinado"
        #     print("Erro platform.system():{}{}".format(ValueError, ImportError))

        dic_dados["Plataform"] = platform.platform()

        dic_dados["Python version"] = platform.python_version()
        dic_dados["release"] = platform.release()
        # dic_dados["version"] = platform.version()
        dic_dados["architecture"] = platform.architecture()

        # dic_dados["Caminho rais do sistema"] = ????

        self.dic_config = dic_dados.copy()
        # print(self.dic_config)

    def tela_config(self):
        pass
