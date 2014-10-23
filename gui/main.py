#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

class AccountManager:

    def delete(self, widget, event=None):
        gtk.main_quit()
        return False

    def __init__(self):
        self.gtk = gtk

        self.windowMain = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.windowMain.connect("delete_event", self.delete)
        self.windowMain.set_border_width(10)

        self.initTabs()

    def show(self):
        self.windowMain.show()
        self.gtk.main()
        return 0

    def initTabs(self):
        tab = self.gtk.Notebook()
        tab.set_scrollable()
        tab.set_tab_pos(gtk.POS_TOP)
        tab.show()

if __name__ == "__main__":
    a = AccountManager()
    a.initTabs()
    a.show()
