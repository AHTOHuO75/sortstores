#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
from pprint import pprint


class Stores:

    def __init__(self, storespath, domain):
        self.stack_ = {}
        self.move_ = []
        self.storespath = storespath
        self.stores = [self.storespath + "/" + x + "/" + x for x in os.listdir(self.storespath) if
                       os.path.isdir(self.storespath + "/" + x + "/" + x) == True]
        self.stores[
            self.stores.index(self.storespath + "/store00/store00")] = self.storespath + "/store00/store00/" + domain
        self.stores.sort()
        self.fill_stores_sizes()
        self.fill_mbox_sizes()
        self.fill_difs()
        self.fill_stack()
        self.fill_move()

    def get_size(self, dir_):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(dir_):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
        return total_size

    def get_minuses(self):
        result = [item for item in sorted(self.difs.items(), key=lambda x: x[1], reverse=True) if item[1] < 0]
        return result

    def fill_stores_sizes(self):
        self.store_sizes = {}
        for store in self.stores:
            self.store_sizes[store] = self.get_size(store)
        return self.store_sizes

    def fill_mbox_sizes(self):
        self.mbox_sizes = {}
        for store in self.stores:
            tmp = {}
            for mbox in os.listdir(store):
                if os.path.isdir(store + "/" + mbox) and (mbox != 'LISTS' and mbox != "PBXApps" and mbox != "Settings"  and mbox != "WebSkins") and (mbox.find('.macnt') != -1 or mbox.find('.mslc') != -1):
                    tmp[store + "/" + mbox] = self.get_size(store + "/" + mbox)
            self.mbox_sizes[store] = tmp
        return self.mbox_sizes

    def fill_difs(self):
        self.difs = self.store_sizes
        dif_ = sum(self.difs.values()) / len(self.difs.values())
        for store in self.difs:
            self.difs[store] = self.difs[store] - dif_
        return self.difs

    def fill_stack(self):
        struct = self.mbox_sizes
        for store in sorted(self.difs.items(), key=lambda x: x[1], reverse=True):
            if store[1] > 0:
                diff = store[1]
                mboxes = sorted(struct[store[0]].items(), key=lambda x: x[1], reverse=True)
                for mbox, size_ in mboxes:
                    if size_ > diff:
                        continue
                    self.stack_[mbox] = size_
                    diff -= size_
        return self.stack_

    def fill_move(self):
        tmp = sorted(self.stack_.items(), key=lambda x: x[1], reverse=True)
        minuses = self.get_minuses()
        minuses_len = len(self.get_minuses())
        pprint(self.fill_stores_sizes())
        pprint(minuses)
        for i in range(1,len(tmp)+1):
            index = i % minuses_len if i % minuses_len != 0 else minuses_len
            self.move_.append((tmp[i-1][0], minuses[index-1][0]))
        pprint(self.move_)


