import datetime

AWS_ACCESS_KEY_ID = "AKIAIRMGKN5UTHCW2ZAQ"
AWS_SECRET_ACCESS_KEY = "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"


AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = True

DEFAULT_FILE_STORAGE = 'homelessdog.aws.utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'homelessdog.aws.utils.StaticRootS3BotoStorage'
AWS_STORAGE_BUCKET_NAME = '<bucket_name>'
S3DIRECT_REGION = 'sa-east-1'
S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
MEDIA_ROOT = MEDIA_URL
STATIC_URL = S3_URL + 'static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
AWS_S3_HOST = 's3-sa-east-1.amazonaws.com'

two_months = datetime.timedelta(days=61)
date_two_months_later = datetime.date.today() + two_months
expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")

AWS_HEADERS = {
	'Expires': expires,
	'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()), ),
}
