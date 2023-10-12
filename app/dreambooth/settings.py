# dreambooth_api/settings.py
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
GS_BUCKET_NAME = 'capstone-design-iise'  # GCS 버킷 이름
GS_PROJECT_ID = 'capstone-design-iise-394910'
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

"""
GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
    "/Users/kimseohyun/Downloads/capstone-design-iise-394910-f2bc2438d25f.json"
)"""

