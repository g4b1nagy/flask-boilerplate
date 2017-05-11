from authomatic.providers import oauth1, oauth2

# =========================================================================
# Authomatic
# =========================================================================

AUTHOMATIC = {
    'facebook': {
        'class_': oauth2.Facebook,
        'consumer_key': '',
        'consumer_secret': '',
        'scope': ['public_profile', 'email'],
    },
    'google': {
        'class_': oauth2.Google,
        'consumer_key': '',
        'consumer_secret': '',
        'scope': ['profile', 'email'],
    },
    'twitter': {
        'class_': oauth1.Twitter,
        'consumer_key': '',
        'consumer_secret': '',
    },
}

# =========================================================================
# Flask
# =========================================================================

DEBUG = True
# python3 -c "import os;print(os.urandom(32))"
SECRET_KEY = '\xf0\xb6\x19\xb94Uo\x1b\xf9\x8b\x0e\xa1@RK\x11T_\xb9Q\xde\x1d\x80\xfa\xd4t\xcbZN:1@'

# =========================================================================
# SQLAlchemy
# =========================================================================

SQLALCHEMY_DATABASE_URI = 'mysql://username:password@server/db'
SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# =========================================================================
# WTForms
# =========================================================================

WTF_CSRF_ENABLED = True

# =========================================================================
# webassets
# =========================================================================

ASSETS_DEBUG = True
