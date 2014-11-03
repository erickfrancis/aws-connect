class ManageAccount:

    def get_form_account(self):
        from os.path import join

        glade_form_file = join('gui', 'glade-files', 'form_account.glade')
        builder = self.gtk.Builder()
        builder.add_from_file(glade_form_file)
        return builder.get_object('account_form')

    def add_account(self, account_name):
        label = self.gtk.Label()
        label.set_text(account_name)

        self.get_tabs().append_page(self.get_form_account(), label)

    def on_create_account_clicked(self, widget, event=None):
        message_dialog = self.gtk.MessageDialog(parent=None, flags=0, type=self.gtk.MESSAGE_QUESTION,
                                               buttons=self.gtk.BUTTONS_OK_CANCEL,
                                               message_format="Name")

        action_area = message_dialog.get_content_area()

        name_account_entry = self.gtk.Entry()
        action_area.pack_start(name_account_entry)

        message_dialog.show_all()
        response = message_dialog.run()

        if response == self.gtk.RESPONSE_OK:
            self.add_account(name_account_entry.get_text())
            self.get_tabs().next_page()

        message_dialog.destroy()

    def get_tabs(self):
        tabs = self.builder.get_object('account_tabs')
        tabs.show_all()
        return tabs

    def get_window_main(self):
        return self.builder.get_object("manage_accounts")

    @staticmethod
    def get_glade_file():
        from os.path import join
        return join('gui', 'glade-files', 'manage_accounts.glade')

    def __init__(self):
        import pygtk

        pygtk.require('2.0')
        import gtk

        self.gtk = gtk

        self.builder = self.gtk.Builder()
        self.builder.add_from_file(self.get_glade_file())
        self.builder.connect_signals(self)