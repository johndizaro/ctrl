import gi

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk


class AssistantWin(Gtk.Assistant):
    def __init__(self, a):
        '''
            4 ページあるサンプル
        '''
        Gtk.Assistant.__init__(self, application=a)
        self.connect('cancel', self.on_close)
        self.connect('close', self.on_close)
        self.connect('apply', self.on_apply)
        # Pages
        for title in ['最初に', 'コンテンツ', '進展状況', '完了']:
            vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
            self.append_page(vbox)
            self.set_page_title(vbox, title)
        # 最初に
        label0 = Gtk.Label(label='導入ページ - 進んでください')
        page = self.get_nth_page(0)
        page.append(label0)
        self.set_page_type(page, Gtk.AssistantPageType.INTRO)
        self.set_page_complete(page, True)
        # コンテンツ
        label1 = Gtk.Label(label='コンテンツページ - チェックすると次に進めます\n完了を間違えて押さないで')
        check = Gtk.CheckButton(label='カメラの画質はセンサーサイズではない')
        check.connect('toggled', self.on_checkbutton_toggled)
        page = self.get_nth_page(1)
        page.append(label1)
        page.append(check)
        self.set_page_type(page, Gtk.AssistantPageType.CONTENT)
        # 進展状況
        label2 = Gtk.Label(label='進度ページ - 本当ですか？')
        # r1 = Gtk.RadioButton(label='いいえ', active=True)) # GTK3
        # r2 = Gtk.RadioButton(label='はい', group=r1)
        r1 = Gtk.CheckButton(label='いいえ', active=True)
        r2 = Gtk.CheckButton(label='はい', group=r1)
        r2.connect('toggled', self.on_radiobutton_toggled)
        page = self.get_nth_page(2)
        page.append(label2)
        page.append(r1)
        page.append(r2)
        self.set_page_type(page, Gtk.AssistantPageType.CONTENT)
        self.set_page_complete(page, True)
        # 完了
        self.last_label = Gtk.Label(label='そうですか...')
        page = self.get_nth_page(3)
        page.append(self.last_label)
        self.set_page_type(page, Gtk.AssistantPageType.SUMMARY)
        self.set_page_complete(page, True)

    def on_close(self, assistant):
        '''
            delete-event もココにくる
        '''
        app.quit()

    def on_apply(self, assistant):
        '''
            コンプリート(CONFIRM)でココにくる
            close シグナルも発生するので main_quit 処理は不要
        '''
        print('やっぱりマイクロフォーサーズが最高！')

    def on_checkbutton_toggled(self, widget):
        '''
            次に進むボタンの ON/OFF
        '''
        self.set_page_complete(self.get_nth_page(1), widget.get_active())

    def on_radiobutton_toggled(self, widget):
        '''
            CONFIRM, SUMMARY の振り分け
        '''
        if widget.get_active():
            self.last_label.set_text('適用してください')
            self.set_page_type(self.get_nth_page(3), Gtk.AssistantPageType.CONFIRM)
        else:
            self.last_label.set_text('そうですか...')
            self.set_page_type(self.get_nth_page(3), Gtk.AssistantPageType.SUMMARY)


def app_activate(a):
    # GtkWindow ベースなのでウインドウとして使える
    w = AssistantWin(a)
    w.present()


app = Gtk.Application()
app.connect('activate', app_activate)
app.run()