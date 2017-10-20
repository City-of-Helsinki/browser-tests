## Install
```
pyenv virtualenv browsertests
pyenv local browsertests
pip install -r requirements.txt
```

## Config
Setup .env or your regular env:

```
SAUCELABS_USERNAME
SAUCELABS_ACCESS_KEY
HELSINKI_ADFS_USER
HELSINKI_ADFS_PASSWORD
FACEBOOK_USER
FACEBOOK_PASSWORD
```

(HELSINKI_ADFS parameters are not currently used)

and optionally change defaults for

```
BROWSER
HEADLESS
TIMEOUT
SERVICEMAP_URL
VARAAMO_URL
```

If SAUCELABS_USERNAME and ACCESS_KEY are set,
BROWSER can be `ie11` for Internet Explorer 11 on Windows 10,
`ie10` for Internet Explorer 10 on Windows 7,
or anything else from Chrome on OS X.

Otherwise browser is always local Chrome.

## Run

```
pytest
```
