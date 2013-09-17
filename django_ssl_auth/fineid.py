#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2013 SSH Communication Security Corporation.
# All rights reserved.
# This software is protected by international copyright laws.
#

def _dictify_dn(dn):
    return dict(x.split('=') for x in dn.split('/') if '=' in x)


def user_dict_from_dn(dn):
    d = _dictify_dn(dn)
    ret = dict()
    ret['username'] = d['serialNumber']
    ret['last_name'] = d['SN'].title()
    ret['first_name'] = d['GN'].title()
    ret['email'] = ''
    return ret
