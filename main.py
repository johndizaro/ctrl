import sys

from menu_principal import MenuPrincipal

class Ctrl:
    def __init__(self):
        self.pode_entrar = False
        # self.cf = ConfigSistema()
        # exit(0)

        app = MenuPrincipal()
        app.run(sys.argv)

if __name__ == '__main__':
    Ctrl()

