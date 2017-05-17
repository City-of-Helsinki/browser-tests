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
TIMEOUT = int(os.environ.get('TIMEOUT', 10))
