from .common import *
import os
import pymysql


DEBUG=True

# pymysql이 MySQLdb처럼 동작하도록 셋팅
pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': os.environ['DATABASE_ENGINE'],
        'HOST': os.environ['DATABASE_HOST'],
        'USER': os.environ['DATABASE_USER'],
        'PASSWORD': os.environ['DATABASE_PASSWORD'],
        'NAME': os.environ['DATABASE_NAME'],
        'PORT': os.environ['DATABASE_PORT'],
    }
}

INSTALLED_APPS += ['storages']

# django-storages 앱 의존성 추가
# 기본 static/media 저장소를 django-storages로 변경
STATICFILES_STORAGE = 'mysite.storages.StaticS3Boto3Storage'
DEFAULT_FILE_STORAGE = 'mysite.storages.mediaS3Boto3Storage'

# S3 파일 관리에 필요한 최소 설정
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
AWS_S3_REGION_NAME = os.environ['AWS_S3_REGION_NAME']