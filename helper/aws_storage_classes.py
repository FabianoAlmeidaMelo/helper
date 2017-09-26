from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

# ???https://stackoverflow.com/questions/31357353/using-cloudfront-with-django-s3boto

# class MediaStorage(S3Boto3Storage):
#     location = 'media'


# class StaticStorage(S3Boto3Storage):
#     location = 'staticfile'


class StaticStorage(S3BotoStorage):
	"""uploads to 'mybucket/staticfile/', serves from 'cloudfront.net/staticfile/'"""
    location = settings.STATICFILES_LOCATION

    def __init__(self, *args, **kwargs):
        kwargs['custom_domain'] = settings.AWS_S3_CUSTON_DOMAIN
        super(StaticStorage, self).__init__(*args, **kwargs)

class MediaStorage(S3BotoStorage):
	"""uploads to 'mybucket/media/', serves from 'cloudfront.net/media/'"""
    location = settings.MEDIAFILES_LOCATION

    def __init__(self, *args, **kwargs):
        kwargs['custom_domain'] = settings.AWS_S3_CUSTON_DOMAIN
        super(MediaStorage, self).__init__(*args, **kwargs)
