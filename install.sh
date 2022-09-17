#!/bin/bash

poetry build
pex -v $(pwd)/dist/fb_scraper-*-py3-none-any.whl -o fb_scraper.exe -m fb_scraper.main:main
