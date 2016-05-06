# -*- coding: utf-8 -*-
import os

langs = ['it','en','pool',
         'devit','deven', 'devpool',
         'localit','localen','localpool']

#reading lang
lang = os.environ.get('PYWIKIBOT_LANG')

#cheking langs
if not lang in langs:
    print("Lang not supported. Please choose one of:")
    print ('Production: it,en,pool')
    print ('Testing: devit,deven,devpool')
    print ('Local: localit,localen,localpool')
    exit(1)

#reading params
PASSWORD = os.environ.get('PASSWORD')
MODE = os.environ.get('MODE')

#creating config
f = open('user-config.py','w')
f.write('# -*- coding: utf-8 -*-\n')
f.write("mylang='"+ lang+"'\n")
f.write("family='wikitolearn'\n")
f.write("console_encoding = 'utf-8'\n")
f.write('password_file = "./passwordFile.txt"\n')
f.write('usernames = {}\n')
f.write('usernames[family] = {}\n')
f.write('usernames[family][mylang] = u"WikiToBot"\n')
f.close()

#creating password_file
p = open('passwordFile.txt','w')
p.write('("WikiToBot", "'+ PASSWORD +'")\n')
p.close()

import check

#star process
check.main(MODE)
