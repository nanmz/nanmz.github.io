#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Pmin'
SITENAME = 'Pmin'
SITEURL = '//localhost:8000'
SITESUBTITLE = '人生苦短,我TMd又懒'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'
DATE_FORMATS = {
        'zh_CN': '%Y-%m-%d %H:%M:%S',
}
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

DEFAULT_LANG = 'zh-CN'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github', '#'),
          ('twitter', '#'),
          ('facebook', '#'),)


DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = "./theme/Pmin"
OUTPUT_PATH = '28sui.github.io'
ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

STATIC_SAVE_AS= 'posts/{path}'
STATIC_PATHS = [
    'images',
    'extra/favicon.ico',
    'extra/CNAME'
]
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': '../favicon.ico'},
    'extra/CNAME': {'path': '../CNAME'}
}

MAIN_MENU = False
MENUITEMS = (('分 类', '/categories.html'),
    ('存  档', '/archives.html'),
            ('关  于', '/about.html'),)

DUOSHUO = '28sui'
PYGMENTS_STYLE = 'default'
