#!/bin/bash
docker run -ti --rm \
    -e PASSWORD=$1 \
    -e PYWIKIBOT_LANG=$2 \
    -e MODE=$3 \
    wikitolearn/filenamecheck:0.1
