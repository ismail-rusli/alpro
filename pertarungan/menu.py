class Menu:
    def __init__ (self, daftar_menu):
        self.daftar_menu = daftar_menu

    def print_menu (self):
        print ("========== MENU ==========")
        for menu in self.daftar_menu:
            print (menu)

