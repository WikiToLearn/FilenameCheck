# -*- coding: utf-8 -*-
import pywikibot
import sys
import os
import re
import time

config = __import__("user-config")


def userPut(page, oldtext, newtext, **kwargs):
    if oldtext == newtext:
        return
    current_page = page
    page.text = newtext
    return page.save(**kwargs)


def check_filename(page):
    '''This function make the first letter of
    filenames uppercase'''
    newtext = page.text[:]
    changed = False
    r = re.compile(r'\[\[File:\s*(.*?)\]\]')
    for match in re.finditer(r, page.text):
        f = match.group(1)
        if not f[0].isupper():
            print("         #Fixing: "+ f)
            f = f[0].upper()+f[1:]
            newtext = newtext.replace(match.group(0),'[[File:'+f+']]')
            changed = True
    if changed:
        userPut(page, page.text, newtext, minor=True, botflag=True)


def main():
    print("Connecting to " + config.mylang + \
          " domain for the " + config.family + " family")
    site = pywikibot.Site()

    BASE_SITE = site.family.langs[config.mylang]
    print("Base URL: " + BASE_SITE)
    print("Checking all pages")
    pages = site.allpages()

    checkedPages = 0
    errors = 0

    for page in pages:
        page_title = page.title()
        print("    @page: " + page_title + "")
        page = pywikibot.Page(site, page_title)
        check_filename(page)
        time.sleep(1)
        checkedPages+=1;

    print("Checked " + str(checkedPages) + " pages")

if __name__ == "__main__":
    main()
