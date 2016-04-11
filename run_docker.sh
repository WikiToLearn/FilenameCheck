#!/bin/bash
docker run -ti --rm -e PYWIKIBOT_LANG=$1 \
    -e PASSWORD=$2 wikitolearn/filenamecheck:0.1
