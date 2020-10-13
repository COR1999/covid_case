from django.conf import Settings
from storages.backends.s3boto3 import S3Boto3Storage



class StaticStorage(S3Boto3Storage):
    location = Settings.STATICFILES_LOCATION

class MediaStorage(S3Boto3Storage):
    location = Settings.MEDIAFILES_LOCATION