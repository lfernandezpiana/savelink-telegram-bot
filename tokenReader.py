#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Lector de nombre de usuario y token
Debe ponerse el token que da el bot master en un archivo txt (Token.txt) para que pueda leerlo
"""

import os

def access_token():
    open_token = open('Token.txt', 'r')
    token = open_token.read()
    return token.rstrip()
