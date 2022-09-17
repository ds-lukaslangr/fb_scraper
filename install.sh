#!/bin/bash

poetry build
pex -v /Users/orbittal/projects/fb_scrapper/dist/fb_scraper-0.1.0-py3-none-any.whl -o fb_scraper.exe -m fb_scraper.main:main
