#!/usr/bin/env python

import os

import simpress.commands

simpress.base_dir = os.path.abspath(os.path.dirname(__file__))

simpress.settings = {
    # put your configs
    'title': 'Simpress',
}

simpress.commands.execute()
