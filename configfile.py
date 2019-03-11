#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import socket

try:
    import configparser
except ImportError:
    import ConfigParser as configparser


class ConfigFile:

    def __init__(self, configfile):
        self.configfile = configfile
        if not os.path.exists(self.configfile):
            self.create_config(self.configfile)
        else:
            self.config = configparser.ConfigParser()
            self.config.read(self.configfile)

    def create_config(self, configfile):
        self.config = configparser.ConfigParser()
        self.config.add_section("General")
        self.config.set("General", "# StorePath - путь к хранилищам (по умолчанию /srv)")
        self.config.set("General", "StorePath", "/srv")
        self.config.set("General", "# Domain - домен для обработки (по умолчанию устанавливает домен хоста без oao)")
        self.config.set("General", "# Например, для хоста esrr-cgnfs-01.esrr.oao.rzd домен будет установлен в esrr.rzd")
        domain = socket.gethostname().split(".", 1)[1].split(".").pop(0) + "." + socket.gethostname().split(".", 1)[1].split(".").pop(2)
        self.config.set("General", "Domain", domain)
        with open(configfile, "wb") as config_file:
            self.config.write(config_file)

    def get_option(self, section, setting):
        value = self.config.get(section, setting)
        return value
