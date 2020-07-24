# -*- coding: utf-8 -*-
from baidupcsapi import PCS

pcs = PCS('username','password')
print(pcs.quota().content)
print(pcs.list_files('/').content)