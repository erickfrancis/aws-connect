class AwsConnect:
    def __init__(self):
        import gtk
        import appindicator
        import os

        self.gtk = gtk

        self.menu = self.gtk.Menu()

        self.indicator = appindicator.Indicator('wallch_indicator',
                                                '%s/resources/aws.png' % os.path.dirname(os.path.abspath(__file__)),
                                                appindicator.CATEGORY_APPLICATION_STATUS)
        self.indicator.set_status(appindicator.STATUS_ACTIVE)

    def get_indicator(self):
        return self.indicator

    def get_menu(self):
        return self.menu

    def add_item_menu(self, item):
        self.get_menu().append(item)

    def add_menu_quit(self):
        menu_item = self.gtk.MenuItem('Quit')
        menu_item.connect('activate', self.gtk.main_quit)

        self.add_item_menu(menu_item)

        return menu_item

    def add_menu_manage_accounts(self):
        menu_item = self.gtk.MenuItem('Manage accounts')
        menu_item.connect('activate', self.on_menu_item_manage_accounts)

        self.add_item_menu(menu_item)

        return menu_item

    def on_menu_item_manage_accounts(self, widget, event=None):
        from gui.manage_account import ManageAccount

        manage_account = ManageAccount()
        manage_account.get_window_main().show_all()

aws_connect = AwsConnect()

menu = aws_connect.get_menu()

indicator = aws_connect.get_indicator().set_menu(menu)

aws_connect.add_menu_manage_accounts()
aws_connect.add_menu_quit()

menu.show_all()

aws_connect.gtk.mainloop()
