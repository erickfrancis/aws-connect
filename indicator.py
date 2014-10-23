import appindicator
import pynotify
import os

import gtk


indicator = appindicator.Indicator('wallch_indicator', '%s/resources/aws.png' % os.path.dirname(os.path.abspath(__file__)),
                           appindicator.CATEGORY_APPLICATION_STATUS)
indicator.set_status(appindicator.STATUS_ACTIVE)
m = gtk.Menu()
ci = gtk.MenuItem('Check')
qi = gtk.MenuItem('Quit')

m.append(ci)
m.append(qi)

indicator.set_menu(m)
ci.show()
qi.show()


def checkStatus(item):

    pynotify.init('wallch_indicator')
    n = pynotify.Notification('<b>AWS Connect</b>',
                              'subscribers: %s   views: %s' % ('erc', 'vew'),
                              'notification-message-im')
    n.show()


ci.connect('activate', checkStatus)


def quit(item):
    gtk.main_quit()


qi.connect('activate', quit)

gtk.main()
