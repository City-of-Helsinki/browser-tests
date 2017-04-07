from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

SERVICEMAP_URL = os.environ.get('SERVICEMAP_URL', 'http://localhost:9001')
BROWSER = os.environ.get('BROWSER', 'Chrome')
TIMEOUT = os.environ.get('TIMEOUT', 1)
