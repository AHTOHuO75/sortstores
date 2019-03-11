#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import pprint

# custom import
import params
import configfile
import stores


def main():
    params_ = params.Params(sys.argv[1:], 'Сортировка ящиков в хранилищах.')
    config_ = configfile.ConfigFile(params_.get_param('configfile'))
    stores_ = stores.Stores(config_.get_option('General', 'StorePath'), config_.get_option('General', 'Domain'))



if __name__ == '__main__':
    main()
