# Settings for deployment

# These settings are UCL-specific.

from os.path import join, dirname, basename
import re
import logging

logging.warning('Started...')

SITE_NAME = 'Praktomat@UCL (2017)'

PRAKTOMAT_PATH = dirname(dirname(dirname(__file__)))
PRAKTOMAT_HOME = dirname(PRAKTOMAT_PATH)
PRAKTOMAT_ID = "GC05_2017"

# The URL where this site is reachable.
BASE_HOST = 'http://praktomat.cs.ucl.ac.uk'
BASE_PATH = '/'

ALLOWED_HOSTS = [ '*' ]

# URL to use when referring to static files.
STATIC_URL = BASE_PATH + 'static/'

STATIC_ROOT = join(dirname(PRAKTOMAT_PATH), "static")

# Absolute path to the directory that shall hold all uploaded files as well as
# files created at runtime.

# Example: "/home/media/media.lawrence.com/"
UPLOAD_ROOT = PRAKTOMAT_HOME + "/PraktomatSupport/"

ADMINS = [
  (('PraktomatUCL', 'praktomat@cs.ucl.ac.uk'))
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.cs.ucl.ac.uk"
EMAIL_PORT = 25

DEFAULT_FROM_EMAIL = "praktomat@cs.ucl.ac.uk"

#DEBUG = False
DEBUG=True

DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME':   PRAKTOMAT_ID,
    }
}

# Private key used to sign uploded solution files in submission confirmation email
PRIVATE_KEY = PRAKTOMAT_HOME + '/certificates/signer.pem'

# Enable Shibboleth:
# SHIB_ENABLED = True
# REGISTRATION_POSSIBLE = False

# Use a dedicated user to test submissions
USEPRAKTOMATTESTER = False

# Use docker to test submission
# USESAFEDOCKER = True

# Various extra files and versions
#CHECKSTYLEALLJAR = '/srv/praktomat/contrib/checkstyle-5.7-all.jar'
#JAVA_BINARY = 'javac-sun-1.7'
#JVM = 'java-sun-1.7'

# Our VM has 4 cores, so lets try to use them
#NUMBER_OF_TASKS_TO_BE_CHECKED_IN_PARALLEL = 6

# Increase the maximal output size.
TEST_MAXLOGSIZE=256

# The timezone is wrongly set by the defaults.
TIME_ZONE='Europe/London'

# Finally load defaults for missing setttings.
import defaults
defaults.load_defaults(globals())

