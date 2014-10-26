#!/usr/bin/env python

class AccountForm:

    def __init__(self):
        import pygtk
        pygtk.require('2.0')
        import gtk

        self.gtk = gtk

    def factory_form(self):
        container = self.gtk.VBox()

        """
        AWS Access key
        """
        aws_access_key = self.gtk.HBox()

        aws_access_key_label = self.gtk.Label()
        aws_access_key_label.set_text('AWS Access Key')

        aws_access_key_value = self.gtk.Entry()
        aws_access_key_value.set_max_length(50)
        aws_access_key_value.select_region(0, len(aws_access_key_value.get_text()))

        aws_access_key.add(aws_access_key_label)
        aws_access_key.add(aws_access_key_value)

        container.add(aws_access_key)

        """
        AWS Access secret
        """
        aws_access_secret = self.gtk.HBox()

        aws_access_secret_label = self.gtk.Label()
        aws_access_secret_label.set_text('AWS Access Secret')

        aws_access_secret_value = self.gtk.Entry()
        aws_access_secret_value.set_max_length(50)
        aws_access_secret_value.select_region(0, len(aws_access_secret_value.get_text()))

        aws_access_secret.add(aws_access_secret_label)
        aws_access_secret.add(aws_access_secret_value)

        container.add(aws_access_secret)

        """
        AWS Zone
        """
        aws_zone = self.gtk.HBox()

        aws_zone_label = self.gtk.Label()
        aws_zone_label.set_text('Zone')

        aws_zone_value = self.gtk.combo_box_new_text()
        zones = ('','us','sp')
        for zone in zones:
            aws_zone_value.append_text(zone)

        aws_zone.add(aws_zone_label)
        aws_zone.add(aws_zone_value)

        container.add(aws_zone)

        """
        Default user
        """
        default_user = self.gtk.HBox()

        default_user_label = self.gtk.Label()
        default_user_label.set_text('Default user')

        default_user_value = self.gtk.Entry()
        default_user_value.set_max_length(50)
        default_user_value.select_region(0, len(default_user_value.get_text()))

        default_user.add(default_user_label)
        default_user.add(default_user_value)

        container.add(default_user)

        """
        Default path keys
        """
        default_path_keys = self.gtk.HBox()

        default_path_keys_label = self.gtk.Label()
        default_path_keys_label.set_text('Default path keys')

        default_path_keys_value = self.gtk.Entry()
        default_path_keys_value.set_text('~/.ssh')
        default_path_keys_value.set_max_length(50)
        default_path_keys_value.select_region(0, len(default_path_keys_value.get_text()))

        default_path_keys.add(default_path_keys_label)
        default_path_keys.add(default_path_keys_value)

        container.add(default_path_keys)

        """
        Port default
        """
        default_port = self.gtk.HBox()

        default_port_label = self.gtk.Label()
        default_port_label.set_text('Port default')

        default_port_value = self.gtk.Entry()
        default_port_value.set_text('22')
        default_port_value.set_max_length(5)
        default_port_value.select_region(0, len(default_port_value.get_text()))

        default_port.add(default_port_label)
        default_port.add(default_port_value)

        container.add(default_port)

        return container