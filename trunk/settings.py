# Django settings for diamanda project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    #('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'           # 'postgresql', 'mysql', 'sqlite3' or 'ado_mssql'.
DATABASE_NAME = 'django'             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. All choices can be found here:
# http://www.postgresql.org/docs/current/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
TIME_ZONE = 'Europe/Warsaw'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'en_EN'

SITE_ID = 1

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/home/piotr/diamanda/media/'

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '%xoxs7+14wy5_=an$1z-3y=rz7c$=i5*6q^1^4+i^4q^%50lk='

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'stats.statsMiddleware.statsMiddleware',
    #'banMiddleware.banMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
 'diamandas/myghtyboard/templates',
 'diamandas/wiki/templates',
 'diamandas/userpanel/templates',
 'diamandas/news/templates',
 'diamandas/tasks/templates',
 'diamandas/stats/templates',
)

from sys import path
path.append('diamandas/') # apps folder
path.append('diamandas/cbcplugins/cbcplugins/') # cbc definitions folder

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'wiki',
    'stats',
    'tasks',
    'news',
    'myghtyboard',
    'userpanel',
    'django.contrib.admin',
)

ENGINE='punbb' # engine - see media/themes for list
THEME='oxygen' # theme for current engine - see /media/themes/punbb for punBB based themes

# RSS Settings
SITE_NAME = 'Diamanda Wiki !'
SITE_DESCRIPTION = 'A Diamanda Wiki Script'
SITE_NEWS_LINK = '/' # where links of the RSS feeds should point

# Anonymous perms Settings
ANONYMOUS_CAN_EDIT=True
ANONYMOUS_CAN_ADD=True
ANONYMOUS_CAN_VIEW=True
ANONYMOUS_CAN_SET_CURENT=False

# wiki config
WIKI_USE_PDF = False # 'htmldoc' - uses htmldoc , False - no PDF generation
# if set to nonFalse API KEY "search" will allow also "Search this site with google"
# requires pyGoogle, uses current SITE_ID domain name !!! example.com by default, change it to yours!
WIKI_GOOGLE_SEARCH_API = False

# myghtyboard config
ANONYMOUS_CAN_ADD_TOPIC=True
ANONYMOUS_CAN_ADD_POST=True
FORUMS_USE_CAPTCHA = False # should add topic/post use captcha image

# thumb CBC
SITE_IMAGES_DIR_PATH = '/home/piotr/svn/diamanda/media/images/'
SITE_IMAGES_SRC_PATH = '/site_media/images/'
