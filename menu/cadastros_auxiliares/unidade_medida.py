from enum import Enum

import gi
from dacite import from_dict

from db.infa_dataclass.mysql.entities.entity_unidade_medida import EntityUnidaMedida
from db.infa_dataclass.mysql.repositories.repository_unidade_medida import RepositoryUnidaMedida
from geral.geral import Geral

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')
from gi.repository import Gtk, Adw, GObject, Pango

Adw.init()


class TVUnidaMedida(Enum):
    um_id = 0
    um_sigla = 1
    um_descricao = 2


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
    def __init__(self, pai):
        super(UnidadeMediaScreen, self).__init__()
        self._pai = pai
        self._gr = Geral()

        self._COL_UM_ID = 0
        self._COL_UM_SIGLA = 1
        self._COL_UM_DESCRICAO = 2

        self._eum = EntityUnidaMedida()

        self._rum = RepositoryUnidaMedida()

        try:
            self._dict_eum = self._rum.select_all()
        except Exception as e:
            self._gr.meu_logger.error(f"{e}")
            print(f'{e}')
            return
        self._montagem_janela()

    def _montagem_janela(self):
        self._gr.meu_logger.info("Inicio da montagem da janela")

        self.set_title(title="Unidade de Medida")
        self.set_default_size(width=-1, height=400)
        self._montagem_headerbar()

        self.set_destroy_with_parent(setting=True)

        self.set_transient_for(parent=self._pai)
        self.set_resizable(resizable=False)

        self._montar_layout()

        self.present()

    def _montagem_headerbar(self):
        self._gr.meu_logger.info("Montagem do header do menu principal")

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
        bt_undor.set_tooltip_text(text="Restaurar tela")
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
        self._gr.meu_logger.info("inicio da montagem")
        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        vbox.set_margin_top(margin=10)
        vbox.set_margin_end(margin=10)
        vbox.set_margin_bottom(margin=10)
        vbox.set_margin_start(margin=10)
        vbox.set_valign(Gtk.Align.CENTER)

        vbox.append(child=self._montar_campos())

        self.set_child(child=vbox)

    def _montar_campos(self):
        self._gr.meu_logger.info("inicio da montagem")
        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=10)

        vbox.append(child=self._fields_entries())
        vbox.append(child=self._treeview())

        return vbox

    def _treeview(self):
        self._gr.meu_logger.info("inicio da montagem")

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        vbox.get_style_context().add_class(class_name='card')

        # Janela com rolagem onde será adicionado o Gtk.TreeView().
        scrolledwindow = Gtk.ScrolledWindow.new()
        scrolledwindow.set_propagate_natural_height(True)
        # scrolledwindow.get_style_context().add_class(class_name='boxed-list')

        vbox.append(child=scrolledwindow)

        # Criando um modelo com `Gtk.ListStore()`.
        self.list_store = Gtk.ListStore.new(
            [GObject.TYPE_INT, GObject.TYPE_STRING, GObject.TYPE_STRING],
        )
        # Adicionando os dados no `Gtk.ListStore()`.
        for registro in self._dict_eum:
            # self.list_store.append(registro.values())
            self.list_store.append([registro['um_id'], registro['um_sigla'], registro['um_descricao']])

            # Criando um `Gtk.TreeView()`.
        tree_view = Gtk.TreeView.new_with_model(model=self.list_store)
        tree_view.connect('row_activated', self.on_row_activated)
        # tree_view.connect('cursor_changed', self.on_cursor_changed)
        tree_view.set_activate_on_single_click(True)
        tree_view.set_vexpand(expand=True)

        tree_view.set_margin_start(margin=10)
        tree_view.set_margin_end(margin=10)
        tree_view.set_margin_top(margin=10)
        tree_view.set_margin_bottom(margin=10)
        tree_view.set_grid_lines(Gtk.TreeViewGridLines.HORIZONTAL)

        scrolledwindow.set_child(child=tree_view)

        # Nome das colunas (title).
        cols = ('ID',
                self._eum.get_title("um_sigla"),
                self._eum.get_title("um_descricao")
                )

        for column_index, title in enumerate(cols):
            # Criando um rederizador do tipo texto.
            cell_render = Gtk.CellRendererText.new()

            # Configurando o rederizador da primeira coluna apenas.
            # if column_index == 0:
            #     cell_render.set_property('alignment', Pango.Alignment.RIGHT)
            #     cell_render.set_property('weight_set', True)
            # cell_render.set_property('weight', Pango.Weight.BOLD)
            # cell_render.set_visible(False)

            if column_index == TVUnidaMedida.um_sigla.value:
                # cell_render.set_property('foreground', '#698B22')
                cell_render.set_property('weight', Pango.Weight.BOLD)

            # Criando a coluna.
            tree_view_column = Gtk.TreeViewColumn(
                title=title,
                cell_renderer=cell_render,
                # Posição (Coluna 0, coluna 1) em que o CellRendererText
                # sera inseridos.
                text=column_index,
            )

            if column_index == TVUnidaMedida.um_id.value:
                tree_view_column.set_visible(visible=False)

            # Definindo que a coluna pode ordenar o conteúdo.
            tree_view_column.set_sort_column_id(sort_column_id=column_index)

            # Adicionando a coluna no `Gtk.TreeView()`.
            tree_view.append_column(column=tree_view_column)

        return vbox

    def _inserir_dados_na_tela(self, dic):
        self._e_um_sigla.set_text(dic.um_sigla)
        self._e_um_descricao.set_text(dic.um_descricao)

    def on_row_activated(self, path, column, user_data):
        (model, node) = path.get_selection().get_selected()
        if not node:
            return
        selected = int(model.get_value(node, TVUnidaMedida.um_id.value))
        self._gr.meu_logger.info(f"id selecionado:{selected}")

        try:
            registro = self._rum.select_one(id=selected)
        except Exception as e:
            self._gr.meu_logger.error(f"{e}")
            print(f'{e}')
            return
        else:
            self._eum = from_dict(data_class=EntityUnidaMedida, data=registro)
            self._inserir_dados_na_tela(self._eum)

        self._gr.meu_logger.info(f"registro do id selecionado:{registro}")

    # def on_cursor_changed(self,widget):
    #     campo = ""
    #     selection = widget.get_selection()
    #     modelX, iterX = selection.get_selected()
    #     if not iterX:
    #         return False
    #     campo = modelX.get_value(iterX,1)
    #     print(campo)
    # self._e_entry.grab_focus()

    def _fields_entries(self):
        self._gr.meu_logger.info("inicio da montagem")
        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        vbox.get_style_context().add_class(class_name='card')

        self._l_label = Gtk.Label(label="Sigla da unidade  de medida",
                                  margin_top=10,
                                  margin_end=0,
                                  margin_start=10,
                                  xalign=0)
        vbox.append(child=self._l_label)

        self._e_um_sigla = Gtk.Entry(max_length=0,
                                     text="",
                                     tooltip_text="Descrição sigla da unidade de medida",
                                     margin_start=10,
                                     margin_end=10,
                                     margin_top=0,
                                     margin_bottom=10)
        vbox.append(child=self._e_um_sigla)

        self._l_label1 = Gtk.Label(label="Descricao da unidade  de medida",
                                   margin_top=10,
                                   margin_end=0,
                                   margin_start=10,
                                   xalign=0)
        vbox.append(child=self._l_label1)

        self._e_um_descricao = Gtk.Entry(max_length=0,
                                         text="",
                                         tooltip_text="Descrição da unidade de medida",
                                         margin_start=10,
                                         margin_end=10,
                                         margin_top=0,
                                         margin_bottom=10)
        vbox.append(child=self._e_um_descricao)

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
