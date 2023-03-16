# from dataclasses import asdict
import gi
gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')
from gi.repository import Gtk, Adw, GObject, Pango

from dacite import from_dict

from db.infra_dataclass.mysql.engines.engine_unidade_medida import EngineUnidadeMedida
from db.infra_dataclass.mysql.models.model_unidade_medida import ModelUnidadeMedida
# from db.infra_dataclass.mysql.engines.engine_unidade_medida import EngineUnidadeMedida
# from db.infra_dataclass.mysql.models.model_unidade_medida import ModelUnidadeMedida
from geral.geral import Geral
from widgets.dialogs.dialog_message_error import DialogMessageError


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
    def __init__(self, pai):
        super(UnidadeMediaScreen, self).__init__()
        self._pai = pai
        self._gr = Geral()

        self._COL_A01_ID = 0
        self._COL_A01_SIGLA = 1
        self._COL_A01_DESCRICAO = 2

        self._model_unidade_medida = ModelUnidadeMedida()
        self._engine_unidade_medida = EngineUnidadeMedida()

        self._list_dic_registros = list()
        self.ler_dados_para_treeview()

        self._criar_layout(layout_janela=self)

    def _criar_layout(self, layout_janela):
        self._gr.meu_logger.info("Inicio da montagem da janela")

        layout_janela.set_title(title="Unidade de Medida")
        layout_janela.set_default_size(width=-1, height=400)
        layout_janela._montagem_headerbar(layout_janela=layout_janela)

        layout_janela.set_destroy_with_parent(setting=True)

        layout_janela.set_transient_for(parent=self._pai)
        layout_janela.set_resizable(resizable=True)

        layout_janela._desenhar_layout()

        layout_janela.present()

    def _montagem_headerbar(self, layout_janela):
        self._gr.meu_logger.info("Montagem do header do menu principal")

        headerbar = Gtk.HeaderBar.new()
        headerbar.set_show_title_buttons(setting=True)
        Gtk.StyleContext.add_class(headerbar.get_style_context(), "headerbar")
        layout_janela.set_titlebar(titlebar=headerbar)

        bt_salvar = Gtk.Button.new_with_label(label='Salvar')
        bt_salvar.set_icon_name(icon_name='document-save-symbolic')
        bt_salvar.get_style_context().add_class(class_name='suggested-action')
        bt_salvar.set_tooltip_text(text="Salvar alterações no banco de dados")
        bt_salvar.connect('clicked', self.on_bt_salvar_clicked)
        headerbar.pack_start(child=bt_salvar)

        bt_undor = Gtk.Button.new_with_label(label='Limpar Tela')
        bt_undor.set_icon_name(icon_name='edit-clear-all-symbolic')
        bt_undor.get_style_context().add_class(class_name='')
        bt_undor.set_tooltip_text(text="Restaurar apelas a tela")
        bt_undor.connect('clicked', self.on_bt_undor_clicked)
        headerbar.pack_start(child=bt_undor)

        bt_apagar = Gtk.Button.new_with_label(label='Apagar')
        bt_apagar.set_icon_name(icon_name='edit-delete-symbolic')
        bt_apagar.get_style_context().add_class(class_name='destructive-action')
        bt_apagar.set_tooltip_text(text="Apagar unidade de medida do banco de dados")
        bt_apagar.connect('clicked', self.on_bt_apagar_clicked)
        headerbar.pack_start(child=bt_apagar)

        bt_ajudar = Gtk.Button.new_with_label(label='Ajudar')
        bt_ajudar.set_icon_name(icon_name='help-browser-symbolic')
        bt_ajudar.get_style_context().add_class(class_name='')
        bt_ajudar.set_tooltip_text(text="Uma preve explicação sobre a tela")
        # bt_ajudar.connect('clicked', self.on_bt_ajudar_clicked)
        headerbar.pack_end(child=bt_ajudar)

        return headerbar

    def _desenhar_layout(self):
        self._gr.meu_logger.info("inicio da montagem")
        vbox_layout = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox_layout.set_margin_top(margin=10)
        vbox_layout.set_margin_end(margin=10)
        vbox_layout.set_margin_bottom(margin=10)
        vbox_layout.set_margin_start(margin=10)
        vbox_layout.set_valign(Gtk.Align.FILL)
        vbox_layout.set_halign(Gtk.Align.FILL)

        vbox_layout.append(child=self._criar_campos_na_tela())
        # vbox_layout.append(child=self._criar_listview(dic_registros=self._dic_registros))
        # vbox_layout.append(child=self._criar_treeview(dic_registros=self._dic_registros))
        vbox_layout.append(child=self._desenhar_treeview())

        self.set_child(child=vbox_layout)

    def _criar_campos_na_tela(self):

        self._gr.meu_logger.info("inicio da criação dos campos na tela")
        vbox_campos = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        vbox_campos.get_style_context().add_class(class_name='card')

        self._l_label = Gtk.Label(label=self._model_unidade_medida.get_title('a01_sigla'),
                                  margin_top=10,
                                  margin_bottom=0,
                                  margin_start=10,
                                  margin_end=10,
                                  xalign=0,
                                  yalign=0)
        vbox_campos.append(child=self._l_label)

        self._e_a01_sigla = Gtk.Entry(max_length=self._model_unidade_medida.get_size('a01_sigla'),
                                      text="",
                                      tooltip_text=self._model_unidade_medida.get_description('a01_sigla'),
                                      margin_top=0,
                                      margin_end=10,
                                      margin_start=10,
                                      margin_bottom=0)
        # self._e_a01_sigla.set_input_hints(hints=Gtk.InputHints.UPPERCASE_CHARS)
        # self._e_a01_sigla.set_input_purpose(purpose=Gtk.InputPurpose.ALPHA)
        # self._e_a01_sigla.set_placeholder_text("sigla da unidade de medida exe: Kg")

        self._e_a01_sigla.get_style_context().add_class(class_name='accent')
        vbox_campos.append(child=self._e_a01_sigla)

        self._l_label1 = Gtk.Label(label=self._model_unidade_medida.get_title('a01_descricao'),
                                   margin_top=10,
                                   margin_bottom=0,
                                   margin_start=10,
                                   margin_end=10,
                                   xalign=0,
                                   yalign=0)
        vbox_campos.append(child=self._l_label1)

        self._e_a01_descricao = Gtk.Entry(max_length=self._model_unidade_medida.get_size('a01_descricao'),
                                          text="",
                                          tooltip_text=self._model_unidade_medida.get_description('a01_descricao'),
                                          margin_start=10,
                                          margin_end=10,
                                          margin_top=0,
                                          margin_bottom=10)
        self._e_a01_descricao.get_style_context().add_class(class_name='accent')
        vbox_campos.append(child=self._e_a01_descricao)

        return vbox_campos

    def on_key_pressed(self, keyval, keycode, state, user_data):
        print("oi")

    # def editing_done(self, user_data):
    #     print("editing_done")
    #     # texto = self.get_text()
    #     # if not texto:
    #     #     texto = "nd"
    #     # self.emit('edited', self, texto)

    def on_bt_undor_clicked(self, widet):
        self.limpar_campos()

    def on_bt_apagar_clicked(self, widget):

        if self._model_unidade_medida.a01_id > 0:
            self._engine_unidade_medida.deletar(id=self._model_unidade_medida.a01_id)
            self.limpar_campos()
            self.ler_dados_para_treeview()

            self._inserir_dados_treeview(tree_store=self._tree_store, list_dic_registros=self._list_dic_registros)

    def ler_dados_para_treeview(self):
        try:
            self._list_dic_registros = self._engine_unidade_medida.select_all()
            self._gr.meu_logger.info(f"executado select_all(")
        except Exception as e:
            self._gr.meu_logger.error(f"{e}")
            DialogMessageError(parent=self._pai, titulo='Problema ao carregar Unidade de Medida',
                               titulo_mensagem='Problemas ao executar select_all()',
                               mensagem=f'{e}')
        # else:
        #     self._gr.meu_logger.info(f"Dados salvos {self._list_dic_registros}")
        #     self._gr.meu_logger.info(f"vou executar treeview")
        #     self._inserir_dados_treeview(tree_store=self._tree_store, list_dic_registros=self._list_dic_registros)
        #     self._gr.meu_logger.info(f"executei treeview")

    def on_bt_salvar_clicked(self, widget):
        if self.validar_campos():
            self._gr.meu_logger.info(f"Dados para salvar {self._model_unidade_medida}")
            try:
                if self._model_unidade_medida.a01_id == 0:
                    self._engine_unidade_medida.incluir(dicionario=self._model_unidade_medida.dic_UnidadeMedida())
                else:
                    self._engine_unidade_medida.alterar(dicionario=self._model_unidade_medida.dic_UnidadeMedida())
            except Exception as e:
                self._gr.meu_logger.error(f"incluir/alterar: {e}")
                DialogMessageError(parent=self._pai, titulo='Problema ao executar incluir/alterar na Unidade de Medida',
                                   titulo_mensagem='Problemas ao executar select_all()',
                                   mensagem=f'{e}')
                return
            else:
                self.limpar_campos()
                self.ler_dados_para_treeview()
                self._inserir_dados_treeview(tree_store=self._tree_store, list_dic_registros=self._list_dic_registros)

    def limpar_campos(self):

        self._model_unidade_medida = ModelUnidadeMedida()
        self._dic_registros = {}
        self._e_a01_sigla.get_style_context().remove_class(class_name='error')
        self._e_a01_descricao.get_style_context().remove_class(class_name='error')

        self._e_a01_sigla.set_text("")
        self._e_a01_descricao.set_text("")

    def validar_campos(self):

        try:
            # self._e_a01_sigla.get_style_context().remove_class(class_name='error')
            # self._e_a01_sigla.get_style_context().add_class(class_name='accent')
            # self._e_a01_descricao.get_style_context().remove_class(class_name='error')
            # self._e_a01_descricao.get_style_context().add_class(class_name='accent')

            if str(self._e_a01_sigla.get_text()) != "":
                self._model_unidade_medida.a01_sigla = self._e_a01_sigla.get_text()
            else:
                self._model_unidade_medida.a01_sigla = ""

            if str(self._e_a01_descricao.get_text()) != "":
                self._model_unidade_medida.a01_descricao = self._e_a01_descricao.get_text()
            else:
                self._model_unidade_medida.a01_descricao = ""

        except Exception as error:
            DialogMessageError(parent=self,
                               titulo="Erro",
                               titulo_mensagem="Campo com conteúdo inválido",
                               mensagem=str(error))

        return self._model_unidade_medida.verifica_status_final()

    def _desenhar_treeview(self):

        vbox_treeview = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        vbox_treeview.get_style_context().add_class(class_name='card')

        scrolledwindow = Gtk.ScrolledWindow.new()
        scrolledwindow.set_propagate_natural_height(True)
        vbox_treeview.append(child=scrolledwindow)

        self._tree_store = Gtk.TreeStore(GObject.TYPE_INT, GObject.TYPE_STRING, GObject.TYPE_STRING)

        treeview = Gtk.TreeView.new()
        treeview.set_model(model=self._tree_store)
        treeview.connect('row_activated', self.on_row_activated)
        # tree_view.connect('cursor_changed', self.on_cursor_changed)
        treeview.set_activate_on_single_click(True)
        treeview.set_vexpand(expand=True)

        treeview.set_margin_start(margin=10)
        treeview.set_margin_end(margin=10)
        treeview.set_margin_top(margin=10)
        treeview.set_margin_bottom(margin=10)
        treeview.set_grid_lines(Gtk.TreeViewGridLines.HORIZONTAL)

        scrolledwindow.set_child(child=treeview)

        self._desenha_colunas(treeview=treeview)
        self._inserir_dados_treeview(tree_store=self._tree_store, list_dic_registros=self._list_dic_registros)

        return vbox_treeview

    def _desenha_colunas(self, treeview):

        cols = ('ID',
                self._model_unidade_medida.get_title("a01_sigla"),
                self._model_unidade_medida.get_title("a01_descricao")
                )

        for column_index, title in enumerate(cols):
            # Criando um rederizador do tipo texto.
            cell_render = Gtk.CellRendererText.new()

            if column_index == self._COL_A01_SIGLA:
                cell_render.set_property('weight', Pango.Weight.BOLD)

            # Criando a coluna.
            tree_view_column = Gtk.TreeViewColumn(
                title=title,
                cell_renderer=cell_render,
                text=column_index
            )

            # tornando a coluna invisivel
            if column_index == self._COL_A01_ID:
                tree_view_column.set_visible(visible=False)

            # Definindo que a coluna pode ordenar o conteúdo.
            tree_view_column.set_sort_column_id(sort_column_id=column_index)
            # Adicionando a coluna no `Gtk.TreeView()`.
            treeview.append_column(column=tree_view_column)

    def _inserir_dados_treeview(self, list_dic_registros, tree_store):
        treestore = tree_store
        treestore.clear()
        for registro in list_dic_registros:
            treestore.append(None, [registro['a01_id'], registro['a01_sigla'], registro['a01_descricao']])

    def _criar_treeview(self, list_dic_registros):
        self._gr.meu_logger.info("inicio da montagem")

        vbox_treeview = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        vbox_treeview.get_style_context().add_class(class_name='card')

        scrolledwindow = Gtk.ScrolledWindow.new()
        scrolledwindow.set_propagate_natural_height(True)

        vbox_treeview.append(child=scrolledwindow)
        # tree_store = Gtk.TreeStore.set_column_types([GObject.TYPE_INT, GObject.TYPE_STRING, GObject.TYPE_STRING])
        tree_store = Gtk.TreeStore.new(types=[GObject.TYPE_INT, GObject.TYPE_STRING, GObject.TYPE_STRING])

        # tree_store = Gtk.TreeStore(types=[GObject.TYPE_INT, GObject.TYPE_STRING, GObject.TYPE_STRING])
        tree_store.clear()

        for registro in list_dic_registros:
            tree_store.append(None, [registro['a01_id'], registro['a01_sigla'], registro['a01_descricao']])

        # tree_store.clear()

        try:
            treeview = Gtk.TreeView.new()

            # treeview.set_model()
            treeview.set_model(model=tree_store)
            # treeview = Gtk.TreeView.new_with_model(model=tree_store)

            # treeview = Gtk.TreeView.new_with_model(model=tree_store)
        except Exception as e:
            self._gr.meu_logger.error(f"problema no treeview {e}")

        # tree_view.set_model(model=list_store)
        treeview.connect('row_activated', self.on_row_activated)
        # tree_view.connect('cursor_changed', self.on_cursor_changed)
        treeview.set_activate_on_single_click(True)
        treeview.set_vexpand(expand=True)

        treeview.set_margin_start(margin=10)
        treeview.set_margin_end(margin=10)
        treeview.set_margin_top(margin=10)
        treeview.set_margin_bottom(margin=10)
        treeview.set_grid_lines(Gtk.TreeViewGridLines.HORIZONTAL)

        scrolledwindow.set_child(child=treeview)

        cols = ('ID',
                self._model_unidade_medida.get_title("a01_sigla"),
                self._model_unidade_medida.get_title("a01_descricao")
                )

        for column_index, title in enumerate(cols):
            # Criando um rederizador do tipo texto.
            cell_render = Gtk.CellRendererText.new()

            if column_index == self._COL_A01_SIGLA:
                cell_render.set_property('weight', Pango.Weight.BOLD)

            # Criando a coluna.
            tree_view_column = Gtk.TreeViewColumn(
                title=title,
                cell_renderer=cell_render,
                text=column_index
            )

            # tornando a coluna invisivel
            if column_index == self._COL_A01_ID:
                tree_view_column.set_visible(visible=False)

            # Definindo que a coluna pode ordenar o conteúdo.
            tree_view_column.set_sort_column_id(sort_column_id=column_index)
            # Adicionando a coluna no `Gtk.TreeView()`.
            treeview.append_column(column=tree_view_column)

        return vbox_treeview

    def _criar_listview(self, list_dic_registros):
        self._gr.meu_logger.info("inicio da montagem")

        vbox_listview = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        vbox_listview.get_style_context().add_class(class_name='card')

        # tree_view = Gtk.TreeView.new()
        scrolledwindow = Gtk.ScrolledWindow.new()
        scrolledwindow.set_propagate_natural_height(True)
        vbox_listview.append(child=scrolledwindow)
        # list_store = Gtk.ListStore()
        # list_store.clear()
        list_store = Gtk.ListStore.new(types=[GObject.TYPE_INT, GObject.TYPE_STRING, GObject.TYPE_STRING])
        # if list_store:
        #     list_store.clear()
        # list_store.clear()

        self._gr.meu_logger.info(f"dados a serem colocados no treeview: {list_dic_registros}")
        # list_store.append(None)
        # tree_view = Gtk.TreeView.new()
        # tree_view.set_model()

        for registro in list_dic_registros:
            list_store.append([registro['a01_id'], registro['a01_sigla'], registro['a01_descricao']])

        # tree_view.set_model(model=list_store)
        # tree_view.new_with_model(model=list_store)
        tree_view = Gtk.TreeView.new_with_model(model=list_store)

        # tree_view.new()
        # list_store.clear()

        # tree_view.set_model(model=list_store)

        # if tree_view:
        #     tree_view = Gtk.TreeView.new()
        # tree_view = Gtk.TreeView.new_with_model(model=list_store)

        # tree_view = Gtk.TreeView.new_with_model(model=list_store)
        # tree_view.set_model(model=list_store)

        # tree_view.set_model(model=list_store)
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

        cols = ('ID',
                self._model_unidade_medida.get_title("a01_sigla"),
                self._model_unidade_medida.get_title("a01_descricao")
                )

        for column_index, title in enumerate(cols):
            # Criando um rederizador do tipo texto.
            cell_render = Gtk.CellRendererText.new()

            if column_index == self._COL_A01_SIGLA:
                cell_render.set_property('weight', Pango.Weight.BOLD)

            # Criando a coluna.
            tree_view_column = Gtk.TreeViewColumn(
                title=title,
                cell_renderer=cell_render,
                text=column_index,

            )
            # tree_view_column.clear()

            # tornando a coluna invisivel
            if column_index == self._COL_A01_ID:
                tree_view_column.set_visible(visible=False)

            # Definindo que a coluna pode ordenar o conteúdo.
            tree_view_column.set_sort_column_id(sort_column_id=column_index)
            # Adicionando a coluna no `Gtk.TreeView()`.

            tree_view.append_column(column=tree_view_column)

        return vbox_listview

    def _inserir_dados_na_tela(self, dic_model_unida_medida):

        self._e_a01_sigla.set_text(dic_model_unida_medida.a01_sigla)
        self._e_a01_descricao.set_text(dic_model_unida_medida.a01_descricao)

    def on_row_activated(self, path, column, user_data):
        (model, node) = path.get_selection().get_selected()
        if not node:
            return
        selected = int(model.get_value(node, self._COL_A01_ID))
        self._gr.meu_logger.info(f"id selecionado:{selected}")

        try:
            self.registro = self._engine_unidade_medida.select_one(id=selected)
        except Exception as e:
            self._gr.meu_logger.error(f"{e}")
            print(f'{e}')
            DialogMessageError(parent=self._pai,
                               titulo="SQL",
                               titulo_mensagem="Problemas na execução do select_one()",
                               mensagem=f"mensagem de erro:\n{e}")
            return
        else:
            self._model_unidade_medida = from_dict(ModelUnidadeMedida, self.registro)
            self._inserir_dados_na_tela(dic_model_unida_medida=self._model_unidade_medida)

        self._gr.meu_logger.info(f"registro do id selecionado:{self._model_unidade_medida}")

    # def on_cursor_changed(self,widget):
    #     campo = ""
    #     selection = widget.get_selection()
    #     modelX, iterX = selection.get_selected()
    #     if not iterX:
    #         return False
    #     campo = modelX.get_value(iterX,1)
    #     print(campo)
    # self._e_entry.grab_focus()


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
