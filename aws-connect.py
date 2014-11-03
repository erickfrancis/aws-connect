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

    def add_menu_separator(self):
        separator = self.gtk.SeparatorMenuItem()
        return self.add_item_menu(separator)

    def add_menu_accounts(self):
        sadia = self.gtk.MenuItem('sadia')
        self.add_item_menu(sadia)

        zones = self.gtk.Menu()
        sadia.set_submenu(zones)

        sa_east_1 = self.gtk.MenuItem('sa-east-1')
        zones.append(sa_east_1)

        instances = self.gtk.Menu()
        sa_east_1.set_submenu(instances)

        import subprocess

        web_1 = self.gtk.MenuItem('web-1')
        web_1.connect('activate', lambda x: subprocess.Popen(['xterm', '-e', 'vi']))

        web_2 = self.gtk.MenuItem('web-2')
        web_2.connect('activate', lambda x: subprocess.Popen(['xterm', '-e', 'vi']))

        instances.append(web_1)
        instances.append(web_2)


aws_connect = AwsConnect()

menu = aws_connect.get_menu()

indicator = aws_connect.get_indicator().set_menu(menu)

aws_connect.add_menu_accounts()
aws_connect.add_menu_separator()
aws_connect.add_menu_manage_accounts()
aws_connect.add_menu_quit()

menu.show_all()

aws_connect.gtk.mainloop()