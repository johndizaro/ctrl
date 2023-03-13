import gi

gi.require_version(namespace='Gtk', version='4.0')

from gi.repository import Gtk,Pango


class LabelEntry2():
    def __init__(self, **kwargs):
        # self.text = "john"
        self.margin_top = 0
        self.l_label = Gtk.Label.new()
        # self.x = Pango.Layout.get_attributes(self.l_label.get_layout())

        print(f"x:{self.x}")
        self.e_entry = Gtk.Entry()
        self.vbox = Gtk.Box()


        # pango_layout_get_attribute(gtk_label_get_layout(self))
        self.x = Pango.Layout.get_attributes(self.l_label.get_layout())
        print(f"x:{self.x}")

        for key, value in kwargs.items():
            if (hasattr(LabelEntry2(), key)):
                # setattr(LabelEntry2(),key,value)
                print(f'LabelEntry2() key:{key} value:{value}  ok')
                self.__dict__[key] = value
                # continue
            elif (hasattr(self.l_label,key)):
                # self.__dict__[key] = value
                # setattr(self.l_label, key, value)

                print(f'self.Gtk.l_label key:{key} value:{value}  ok')
                # print(f'self.l_label.get_text():{self.l_label.get_text()}')
                # self.l_label.set_label(value)
            elif (hasattr(self.e_entry,key)):
                print(f'self.Gtk.e_entry key:{key} value:{value}  ok')
                self.__dict__[key] = value
            else:
                self.__dict__[key] = value
                print(f'PROBLEM key:{key} value:{value}')


a = LabelEntry2(set_label="aaa",text='bbb',  margin_top=10, set_max_length=20)

print(f"var(a):{vars(a)}")
print(f"a.l_label.get_text():{a.l_label.get_text()}")
print(f"a.margin_top:{a.margin_top}")
print(f"a.text:{a.text}")
# print(f"a.margin_top:{a.margin_top}")
