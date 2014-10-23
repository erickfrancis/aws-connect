class AccountManager:
    # def on_addAccount(self, widget):
    #     form = self.accountForm().factoryForm()
    #     form.show_all()
    #
    #     label = self.gtk.Label()
    #     label.set_text('OLA')
    #
    #     self.tabs.append_page(form, label)
    #     self.tabs.next_page()
    #
    #     widget.parent
    #
    #     widget.get_parent_window().destroy()

    # def on_cancelCreateAccount(self, widget):
    #     widget.get_parent_window().destroy()

    def on_createAccount(self, widget, event=None):
        messagedialog = self.gtk.MessageDialog(parent=None, flags=0, type=self.gtk.MESSAGE_QUESTION,
                                               buttons=self.gtk.BUTTONS_OK_CANCEL,
                                               message_format="Name")

        action_area = messagedialog.get_content_area()

        self.entry = self.gtk.Entry()
        action_area.pack_start(self.entry)

        messagedialog.show_all()
        response = messagedialog.run()
        messagedialog.destroy()

        if response == gtk.RESPONSE_OK:
            form = self.accountForm().factoryForm()
            form.show_all()

            label = self.gtk.Label()
            label.set_text(self.entry.get_text())

            self.tabs.append_page(form, label)
            self.tabs.next_page()

        # dialog = self.gtk.Dialog(title='Create Account')
        #
        # accountName_label = self.gtk.Label()
        # accountName_label.set_text('Name')
        #
        # accountName_value = self.gtk.Entry()
        # accountName_value.set_name('account_name')
        #
        # buttonCreate = self.gtk.Button("ADD")
        # buttonCreate.connect("clicked", self.on_addAccount)
        #
        # buttonCancel = self.gtk.Button("Cancel")
        # buttonCancel.connect("clicked", self.on_cancelCreateAccount)
        #
        # dialog.action_area.pack_start(buttonCreate)
        # dialog.action_area.pack_start(buttonCancel)
        #
        # dialog.vbox.add(accountName_label)
        # dialog.vbox.add(accountName_value)
        #
        # dialog.show_all()

    def __init__(self):
        import pygtk

        pygtk.require('2.0')
        import gtk

        self.gtk = gtk

        from lib.gui.account_form import AccountForm

        self.accountForm = AccountForm

        self.tabs = self.gtk.Notebook()
        self.tabs.set_tab_pos(gtk.POS_TOP)
        self.tabs.set_scrollable(True)

        self.buttonCreate = self.gtk.Button('Create account')
        self.buttonCreate.connect("clicked", self.on_createAccount)

        self.container = self.gtk.VBox()

        self.container.add(self.buttonCreate)
        self.container.add(self.tabs)

    def getContainer(self):
        return self.container


import pygtk

pygtk.require('2.0')
import gtk


def delete(widget, event=None):
    gtk.main_quit()
    return False


accountManager = AccountManager()

windowMain = gtk.Window(gtk.WINDOW_TOPLEVEL)
windowMain.set_position(gtk.WIN_POS_CENTER)
windowMain.set_border_width(10)

windowMain.connect("delete_event", delete)

windowMain.add(accountManager.getContainer())

windowMain.show_all()
gtk.main()