#!/bin/bash

poetry export -f requirements.txt --without-hashes --output requirements.txt
poetry build
pex $(pwd)/dist/fb_scraper-*-py3-none-any.whl -r requirements.txt -o fb_scraper.exe -m fb_scraper.main:main
