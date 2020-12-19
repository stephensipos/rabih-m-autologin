# -*- coding: utf-8 -*-
"""Loads the package configuration

Attributes:
    config: ConfigParser instance
"""

import configparser

config = configparser.ConfigParser()

config.read("autologin.ini")

