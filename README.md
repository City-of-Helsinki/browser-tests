## Install
```
pyenv virtualenv browsertests
pyenv local browsertests
pip install -r requirements.txt
```

## Config
Setup .env or your regular env

```
HELSINKI_ADFS_USER
HELSINKI_ADFS_PASSWORD
FACEBOOK_USER
FACEBOOK_PASSWORD
```

and optionally change defaults for

```
BROWSER
HEADLESS
TIMEOUT
SERVICEMAP_URL
VARAAMO_URL
```

## Run

```
pytest
```
