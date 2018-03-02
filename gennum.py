#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import argparse
import csv
#import numpy

parser = argparse.ArgumentParser(description = ""
                                               "Genera archivo .csv con los posibles telefonos de un usuario."
                                               "Automáticamente se genera una agenda con los posibles telefonos del usuario"
                                               "eso permite importarla desde un usuario . Happy Hack!")
parser.add_argument("-e", "--email", help="Email para averiguar su telefono en facebook", required=True)
parser.add_argument("-p", "--prefix", help="insertar prefijo pais", required=True)
parser.add_argument("-o", "--oneinitphone", help="debe ser 6 o 7", required=True)
parser.add_argument("-t", "--twoendphone", help="los ultimos numeros que da facebook", required=True)

args = parser.parse_args()
f = open('test.csv', 'w')

f.write ("\n".join([args.email + "," + str(args.prefix) + str(args.oneinitphone) + '{0:05}'.format(num) + str(args.twoendphone) for num in xrange(0, 999999)]))

f.close()

#---->Working Agenda CSV format...





