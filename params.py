#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import argparse


class Params:

    def __init__(self, input_params, description=''):
        self.description = description
        self.input_params = input_params
        self.parser = argparse.ArgumentParser(
            description=self.description
        )
        self.parser.add_argument('-c', '--configfile', default='sortstores.conf')
        self.namespace = vars(self.parser.parse_args(self.input_params))

    def get_param(self, param):
        return self.namespace[param]
