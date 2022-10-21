import gi

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Gio, GLib


class Win(Gtk.ApplicationWindow):
    def __init__(self, a):
        Gtk.ApplicationWindow.__init__(self, application=a)
        btn = Gtk.Button(label='このアプリについて')
        btn.connect('clicked', self.on_button_clicked)
        self.set_child(btn)
        self.present()

    def on_button_clicked(self, button):
        about = Gtk.AboutDialog(
            transient_for=self,
            modal=True,
            # logo = ***, # アイコン
            program_name='OM SYSTEM E-M5',
            version='3.0.0',
            comments='OLYMPUS のカメラ事業は OM SYSTEM に変わりました',
            website='http://localhost/',
            website_label='localhost',  # 指定しなければ「ホームページ」と表示
            copyright='Copyright(C) 2022 sasakima-nao',
            # 以下ライセンスボタン、指定しなければボタンは出ない
            license='GPL',
            # 以下クレジットボタン、指定しなければボタンは出ない、配列に注意
            authors=['sasakima-nao'],  # 開発担当
            artists=['sasakima-nao'],  # アートワーク担当
            documenters=['sasakima-nao'],  # ドキュメント担当
            translator_credits='sasakima-nao'  # 翻訳担当、ここは str
        )
        about.show()


def app_activate(a):
    w = Win(a)
    w.set_default_size(600, 500)  # モーダル化が判るようにリサイズ
    w.present()


app = Gtk.Application()
app.connect('activate', app_activate)
app.run()