from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

SERVICES = {
    'servicemap': {
        'URL': os.environ.get('SERVICEMAP_URL', 'https://palvelukartta.hel.fi')
    },
    'varaamo': {
        'URL': os.environ.get('VARAAMO_URL', 'https://varaamo.hel.fi')
    }
}

BROWSER = os.environ.get('BROWSER', 'Chrome')
HEADLESS = os.environ.get('HEADLESS', 'true').lower() in ['1', 'true', 'yes']
TIMEOUT = int(os.environ.get('TIMEOUT', 10))
HELSINKI_ADFS_USER = os.environ.get('HELSINKI_ADFS_USER', '')
HELSINKI_ADFS_PASSWORD = os.environ.get('HELSINKI_ADFS_PASSWORD', '')
FACEBOOK_USER = os.environ.get('FACEBOOK_USER', '')
FACEBOOK_PASSWORD = os.environ.get('FACEBOOK_PASSWORD', '')
