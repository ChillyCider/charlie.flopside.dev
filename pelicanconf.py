#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
from dotenv import load_dotenv

load_dotenv()

AUTHOR = 'Charlie Murphy'
SITENAME = "Charlie's Blog"
SITETITLE = 'Charlie Murphy'
SITESUBTITLE = 'Programmer'
SITEDESCRIPTION = "Charlie Murphy's random thoughts"
BIO = 'Professional coder, AI enthusiast, hobbyist RPG-er.'
SITEURL = ''
PROFILE_IMAGE = SITEURL + '/images/profile.jpg'
PATH = 'content'
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'
TYPOGRIFY = True

STATIC_PATHS = ['images', 'tools']
ARTICLE_EXCLUDES = ['tools']

if os.getenv('THEME') is not None:
    THEME = os.getenv('THEME')
COPYRIGHT_NAME = 'Charlie Murphy'
COPYRIGHT_YEAR = '2019'
BROWSER_COLOR = '#553'
USE_BOOTSTRAP = True

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL + '/'
FEED_ALL_ATOM = 'feeds/all.atom.xml'

# Blogroll
LINKS = (('Flopside.dev Network', 'https://flopside.dev/'),
         ('Another person: Gawrsh', 'https://gawrsh.flopside.dev/'),)

# Social widget
SOCIAL = (('envelope-open', 'mailto:charliemsmurphy@gmail.com'),
          ('facebook', 'https://www.facebook.com/profile.php?id=100033898026850'),
          ('github-alt', 'https://github.com/ChillyCider/'),
          ('linkedin', 'https://www.linkedin.com/in/charlie-murphy-794b97163'),
          ('rss', FEED_DOMAIN + FEED_ALL_ATOM),)
SOCIAL_ICONS = {
    'github-alt': { 'icon':    'github-alt', 'is_brand':  True },
    'facebook':   { 'icon':    'facebook-f', 'is_brand':  True },
    'linkedin':   { 'icon':      'linkedin', 'is_brand':  True },
    'rss':        { 'icon':           'rss', 'is_brand': False },
    'envelope-open': { 'icon': 'envelope-open', 'is_brand': False },
}

DEFAULT_PAGINATION = 6

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True