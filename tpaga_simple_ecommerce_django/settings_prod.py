import os

ALLOWED_HOSTS = [
    # Allowed domains for env
    "localhost",
    "tpaga.contraslash.com",
]

# Database configuration
DATABASE_NAME = os.environ.get("DATABASE_DATABASE", "")
DATABASE_USERNAME = os.environ.get("DATABASE_USERNAME", "")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD", "")
DATABASE_HOST = os.environ.get("DATABASE_HOST", "")
DATABASE_PORT = os.environ.get("DATABASE_PORT", "3306")


DATABASES = {
    'default': {
        #
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DATABASE_NAME,
        'USER': DATABASE_USERNAME,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': DATABASE_HOST,
        'PORT': DATABASE_PORT
    }
}


# Static files configuration
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME', "")
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', "")
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', "")
AWS_MEDIA_S3_REGION_NAME = os.environ.get('AWS_MEDIA_S3_REGION_NAME', "")
AWS_S3_CUSTOM_DOMAIN = '{}.s3.amazonaws.com'.format(AWS_STORAGE_BUCKET_NAME)


STATICFILES_LOCATION = 'tpaga/static'
STATICFILES_STORAGE = 'tpaga_simple_ecommerce_django.storages.StaticStorage'
STATIC_URL = "https://{}/{}/".format(AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
