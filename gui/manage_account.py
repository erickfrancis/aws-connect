class ManageAccount:
    def add_account(self, account_name):
        form = self.accountForm().factory_form()
        form.show_all()

        label = self.gtk.Label()
        label.set_text(account_name)

        self.get_tabs().append_page(form, label)

    def on_create_account(self, widget, event=None):
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
        return self.tabs

    def __init__(self):
        import pygtk

        pygtk.require('2.0')
        import gtk

        self.gtk = gtk

        from account_form import AccountForm

        self.accountForm = AccountForm

        self.tabs = self.gtk.Notebook()
        self.tabs.set_tab_pos(gtk.POS_TOP)
        self.tabs.set_scrollable(True)

        self.buttonCreate = self.gtk.Button('Create account')
        self.buttonCreate.connect("clicked", self.on_create_account)

        self.container = self.gtk.VBox()

        self.container.add(self.buttonCreate)
        self.container.add(self.tabs)

    def get_container(self):
        return self.container