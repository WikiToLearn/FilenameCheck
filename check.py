# -*- coding: utf-8 -*-
import pywikibot
import sys
import os
import re
import time

config = __import__("user-config")


def check_filename(page):
    '''This function make the first letter of
    filenames uppercase'''
    newtext = page.text[:]
    changed = False
    r = re.compile(r'\[\[File:\s*(.*?)\]\]')
    for match in re.finditer(r, page.text):
        f = match.group(1)
        if f[0].islower():
            global errors
            errors+=1
            print("         #Fixing: "+ f)
            f = f[0].upper()+f[1:]
            newtext = newtext.replace(match.group(0),'[[File:'+f+']]')
            changed = True
    if changed:
        page.text = newtext
        page.save(minor=True, botflag=True)

def move_page(site,page, title):
    letter = title[5]
    if letter.islower():
        global errors
        errors+=1
        new_title ='File:'+letter.upper()+ title[6:]
        #moving the page
        new_page = pywikibot.Page(site,new_title)
        if site.page_exists(new_page):
            #deleting the page
            print("        #Duplicate image: "+ title)
            #I'm not able to delete them
            #page.delete(prompt=False, reason='duplicated file', mark=True)
        else:
            print("        #Moving image: "+ title)
            try:
                page.move(new_title,reason='Wrong filename capitalization')
            except Exception as e:
                print('ERROR: '+str(e))




def main(MODE):
    print("Connecting to " + config.mylang + \
          " domain for the " + config.family + " family")
    site = pywikibot.Site()
    site.login()

    BASE_SITE = site.family.langs[config.mylang]
    print("Base URL: " + BASE_SITE)

    checkedPages = 0
    global errors
    errors = 0

    if MODE == 'a':
        print("Checking all pages")
        for page in site.allpages(step=20):
            page_title = page.title()
            print("    @page: " + page_title + "")
            page = pywikibot.Page(site, page_title)
            check_filename(page)
            checkedPages+=1
    elif MODE == 'b':
        print("Checking all images")
        for page in site.allimages(step=20):
            page_title = page.title()
            print("    @image: " + page_title + "")
            move_page(site,page, page_title)
            checkedPages+=1

    print("Checked " + str(checkedPages) + " pages")
    print("Fixed "+ str(errors) + " pages")
