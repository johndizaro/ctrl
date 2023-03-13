import gi

gi.require_version(namespace='Gtk', version='4.0')

from gi.repository import Gtk


class LabelDropdown():
    def __init__(self, **kwargs):

        self.lst_dic_registros = []
        self._lst_data = []
        self.campo_para_incluir = None
        self.campo_chave = None
        self._selected_value = None
        # self.selected_id = 0


        self.margin_top = 10
        self.margin_end = 10
        self.margin_bottom = 10
        self.margin_start = 10
        self.title = "title"
        self.tooltip_text = "tooltip_text"



        for key, value in kwargs.items():
            setattr(self, key, value)


    def __setattr__(self, key, value):

        match key:
            case 'margin_top':
                self._validade_margin(key, value)
            case 'margin_end':
                self._validade_margin(key, value)
            case 'margin_bottom':
                self._validade_margin(key, value)
            case 'margin_start':
                self._validade_margin(key, value)
            case 'title':
                self._validade_title(key, value)
            case 'tooltip_text':
                self._validade_tooltip_text(key, value)
            case '_selected_value':
                self._inicializa_selected_value(key, value)
            case '_lst_data':
                self._inicializa_lst_data(key, value)
            case 'campo_para_incluir':
                self._validade_campo_para_incluir(key, value)
            case 'campo_chave':
                self._validade_campo_chave(key, value)
            case 'lst_dic_registros':
                self._validade_lst_dic_registros(key, value)
            case _:
                raise ValueError(f"key:{key} value:{value} Erro:{NotImplementedError}")

    def return_selected_data(self, field_name):

        if self._selected_value == None:
            return

        for registro in self.lst_dic_registros:
            if registro[self.campo_para_incluir] == self._selected_value:
                return registro[field_name]

    def _inicializa_selected_value(self, key, value):
        self.__dict__[key] = value

    def _inicializa_lst_data(self,key, value):
        if not (type(value) is list):
            raise ValueError(f"key:{key} value:{value} Erro: Deverá ser uma lista")
        else:
            self.__dict__[key] = value



    def _validade_lst_dic_registros(self, key, value):

        if not (type(value) is list):
            raise ValueError(f"key:{key} value:{value} Erro: Deverá ser uma lista")
        # if value == []:
        #     return
        # else:
        self.__dict__[key] = value

        self._lst_data = []
        for registro in value:
            self._lst_data.append(registro[self.campo_para_incluir])

    def _validade_title(self, key, value):
        if len(str(value)) > 0:
            self.__dict__[key] = value

    def _validade_tooltip_text(self, key, value):
        if len(str(value)) > 0:
            self.__dict__[key] = value

    def _validade_campo_para_incluir(self, key, value):
        if value == None:
            return
        if not (type(value) is str):
            raise ValueError(f"key:{key} value:{value} deverá ser uma string")
        if value == '':
            raise ValueError(f"key:{key} value:{value} deverá ser fornecido")
        else:
            self.__dict__[key] = value

    def _validade_campo_chave(self, key, value):
        if value == None:
            return
        if not (type(value) is str):
            raise ValueError(f"key:{key} value:{value} deverá ser uma string")
        if value == '':
            raise ValueError(f"key:{key} value:{value} deverá ser fornecido")

        self.__dict__[key] = value

    def _validade_margin(self, key, value):
        if not str(value).isnumeric():
            raise ValueError(f"key:{key} value:{value} Erro:{AttributeError}")
        if value >= 0:
            self.__dict__[key] = value
        else:
            self.__dict__[key] = 0

    def _validate_select_data(self, key, value):
        if len(str(value)) > 0:
            self.__dict__[key] = value

    def _validate_select_id(self, key, value):
        if value > 0:
            self.__dict__[key] = value

    # @selected_value.setter
    # def selected_value(self, value):
    #     self._selected_value = value

    @property
    def label_dropdown(self):
        vbox_dropdown = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        vbox_dropdown.set_margin_top(margin=self.margin_top)
        vbox_dropdown.set_margin_end(margin=self.margin_end)
        vbox_dropdown.set_margin_bottom(margin=self.margin_bottom)
        vbox_dropdown.set_margin_start(margin=self.margin_start)
        vbox_dropdown.set_tooltip_text(self.tooltip_text)

        l_label = Gtk.Label(label=self.title,
                            xalign=0,
                            yalign=0)
        vbox_dropdown.append(child=l_label)

        dropdown_text = Gtk.DropDown.new_from_strings(self._lst_data)
        # dropdown_text.set_hexpand(expand=True)
        # dropdown_text.compute_expand(Gtk.Orientation.HORIZONTAL)
        dropdown_text.connect("notify::selected-item", self._on_selected_item_notify, self._lst_data)

        self._selected_value = self._lst_data[dropdown_text.get_selected()]
        # print(self._selected_value)
        # dropdown_text.connect("activate", self._on_activate)

        # dropdown_text.set_selected(position=self.default_row)

        # dropdown_text.set_enable_search(True)
        vbox_dropdown.append(child=dropdown_text)

        return vbox_dropdown

    def _on_selected_item_notify(self, dropdown, user_data, lista):
        # self.selected_Text = dropdown.get_selected()
        self._selected_value = lista[dropdown.get_selected()]

        # for registro in self.lst_dic_registros:
        #     if registro['um_descricao'] == self._selected_value:
        #         print(registro['um_id'])


        # print(self._selected_value)
        # print(self.selected_row)

# a = LabelDropdown(margin_top=10, margin_end=20)
# x = a.label_dropdown()
#
# print(f"a.margin_top:{a.__dict__}")
