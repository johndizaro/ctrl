import gi

from geral.geral import Geral

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')
from gi.repository import Gtk, Adw, GObject, Pango, Gdk

Adw.init()


# class Pai(object):
#     def __init__(self, peso, altura):
#         self.peso = peso
#         self.altura = altura
#
#
# class Filha(Pai):
#     def __init__(self, peso, altura, cabelo):
#         super().__init__(peso, altura)
#         self.cabelo = cabelo


class UnidadeMediaScreen(Gtk.ApplicationWindow):
    brazilian_states = [
        (1, 'Acre'), (2, 'Alagoas'), (3, 'Amapá'), (4, 'Amazonas'),
        (5, 'Bahia'), (6, 'Ceará'), (7, 'Distrito Federal'), (8, 'Espírito Santo'),
        (9, 'Goiás'), (10, 'Maranhão'),
        (11, 'Mato Grosso'), (12, 'Mato Grosso do Sul'),
        (13, 'Minas Gerais'), (14, 'Pará'), (15, 'Paraíba'), (16, 'Paraná'),
        (17, 'Pernambuco'), (18, 'Piauí'), (19, 'Rio de Janeiro'),
        (20, 'Rio Grande do Norte'), (21, 'Rio Grande do Sul'), (22, 'Rondônia'),
        (23, 'Roraima'), (24, 'Santa Catarina'), (25, 'São Paulo'), (26, 'Sergipe'),
        (27, 'Tocantins'),
    ]

    def __init__(self, pai):
        super(UnidadeMediaScreen, self).__init__()
        self._pai = pai
        self._gr = Geral()
        self._montagem_janela()

    def _montagem_janela(self):

        self.set_title(title="Unidade de Medida")
        self.set_default_size(width=-1, height=400)
        self._montagem_headerbar()

        self.set_destroy_with_parent(setting=True)

        self.set_transient_for(parent=self._pai)
        self.set_resizable(resizable=False)

        self._montar_layout()

        self.present()

    def _montagem_headerbar(self):
        # self.a.info("Montagem do header do menu principal")
        self._gr.meu_logger.info("inicio")
        headerbar = Gtk.HeaderBar.new()
        headerbar.set_show_title_buttons(setting=True)
        self.set_titlebar(titlebar=headerbar)

        bt_salvar = Gtk.Button.new_with_label(label='Salvar')
        bt_salvar.set_icon_name(icon_name='document-save-symbolic')
        bt_salvar.get_style_context().add_class(class_name='destructive')
        bt_salvar.set_tooltip_text(text="Salvar alterações")
        # bt_salvar.connect('clicked', self.on_bt_salvar_clicked)
        headerbar.pack_start(child=bt_salvar)

        bt_undor = Gtk.Button.new_with_label(label='Desfazer')
        bt_undor.set_icon_name(icon_name='edit-undo')
        bt_undor.get_style_context().add_class(class_name='suggested-action')
        bt_undor.set_tooltip_text(text="Restaurar configuração na tela")
        # bt_undor.connect('clicked', self.on_bt_undor_clicked)
        headerbar.pack_start(child=bt_undor)

        bt_ajudar = Gtk.Button.new_with_label(label='Ajudar')
        bt_ajudar.set_icon_name(icon_name='help-browser-symbolic')
        bt_ajudar.get_style_context().add_class(class_name='')
        bt_ajudar.set_tooltip_text(text="Uma preve explicação sobre a tela")
        # bt_ajudar.connect('clicked', self.on_bt_ajudar_clicked)
        headerbar.pack_end(child=bt_ajudar)

        return headerbar

    def _montar_layout(self):
        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        vbox.set_margin_top(margin=10)
        vbox.set_margin_end(margin=10)
        vbox.set_margin_bottom(margin=10)
        vbox.set_margin_start(margin=10)
        vbox.set_valign(Gtk.Align.CENTER)

        vbox.append(child=self._montar_campos())

        self.set_child(child=vbox)

    def _montar_campos(self):
        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=10)

        vbox.append(child=self._fields_entries())
        vbox.append(child=self._treeview())

        return vbox

    def _treeview(self):

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        vbox.get_style_context().add_class(class_name='card')


        # Janela com rolagem onde será adicionado o Gtk.TreeView().
        scrolledwindow = Gtk.ScrolledWindow.new()
        scrolledwindow.set_propagate_natural_height(True)
        # scrolledwindow.get_style_context().add_class(class_name='boxed-list')

        vbox.append(child=scrolledwindow)

        # Criando um modelo com `Gtk.ListStore()`.
        self.list_store = Gtk.ListStore.new(
            [GObject.TYPE_INT, GObject.TYPE_STRING],
        )

        # Misturando os dados.
        # random.shuffle(self.brazilian_states)

        # Adicionando os dados no `Gtk.ListStore()`.
        for state in self.brazilian_states:
            self.list_store.insert_with_values(state[0], (0, 1), state)

        # Criando um `Gtk.TreeView()`.
        tree_view = Gtk.TreeView.new_with_model(model=self.list_store)
        tree_view.set_vexpand(expand=True)

        scrolledwindow.set_child(child=tree_view)

        # Nome das colunas (title).
        cols = ('ID', 'Estados')
        for column_index, title in enumerate(cols):
            # Criando um rederizador do tipo texto.
            cell_render = Gtk.CellRendererText.new()

            # Configurando o rederizador da primeira coluna.
            if column_index == 0:
                cell_render.set_property('weight_set', True)
                cell_render.set_property('weight', Pango.Weight.BOLD)

            if column_index == 1:
                cell_render.set_property('foreground', '#698B22')
                cell_render.set_property('weight', Pango.Weight.BOLD)

            # Criando a coluna.
            tree_view_column = Gtk.TreeViewColumn(
                title=title,
                cell_renderer=cell_render,
                # Posição (Coluna 0, coluna 1) em que o CellRendererText
                # e o titulo serão inseridos.
                text=column_index,
            )

            # Definindo que a coluna pode ordenar o conteúdo.
            tree_view_column.set_sort_column_id(sort_column_id=column_index)

            # Adicionando a coluna no `Gtk.TreeView()`.
            tree_view.append_column(column=tree_view_column)

        return vbox

    def _fields_entries(self):
        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        vbox.get_style_context().add_class(class_name='card')

        self._l_label = Gtk.Label(label="Sigla da unidade  de medida",
                                  margin_top=10,
                                  margin_end=0,
                                  margin_start=10,
                                  xalign=0)
        vbox.append(child=self._l_label)

        self._e_entry = Gtk.Entry(max_length=0,
                                  text="",
                                  tooltip_text="Descrição sigla da unidade de medida",
                                  margin_start=10,
                                  margin_end=10,
                                  margin_top=0,
                                  margin_bottom=10)
        vbox.append(child=self._e_entry)

        self._l_label1 = Gtk.Label(label="Descricao da unidade  de medida",
                                   margin_top=10,
                                   margin_end=0,
                                   margin_start=10,
                                   xalign=0)
        vbox.append(child=self._l_label1)

        self._e_entry1 = Gtk.Entry(max_length=0,
                                   text="",
                                   tooltip_text="Descrição da unidade de medida",
                                   margin_start=10,
                                   margin_end=10,
                                   margin_top=0,
                                   margin_bottom=10)
        vbox.append(child=self._e_entry1)

        return vbox


class UnidadeMedida(UnidadeMediaScreen):
    def __init__(self, pai):
        super(UnidadeMedida, self).__init__(pai)
        self._pai = pai

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = UnidadeMediaScreen(pai=self._pai)
        win.present()

    def do_startup(self):
        Gtk.Application.do_startup(self)

    def do_shutdown(self):
        Gtk.Application.do_shutdown(self)
