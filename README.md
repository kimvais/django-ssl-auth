django-ssl-client-auth
======================

SSL authentication backend &amp; middleware for Django for authenticating users with SSL client certificates

## License

MIT license, see LICENSE.txt for full text.

## Setup

### SSL

Set up nginx and create SSL certificates for your server and set up the paths
to server private key, server certificate and CA certificate used to sign
the client certificates. Example configuration file is in samples/nginx.conf

If you are on OS X, I suggest OS X KeyChain access for doing this for
testing, as it will automatically make your client certificates available in
all both Google chrome & Safari. Instructions can be found e.g.
http://www.dummies.com/how-to/content/how-to-become-a-certificate-authority-using-lion-s.html

On other platforms, there are many tutorials on how to do this with OpenSSL
e.g. http://pages.cs.wisc.edu/~zmiller/ca-howto/

Restart your ngninx (sudo nginx -s restart), make sure your green unicorn is
 running and check that your https:// url loads your application and the
 _server certificate is valid_.

### This module

1. run setup.py (sudo python setup.py install) or install the latest release usning `pip install django_ssl_auth `
2. edit your `settings.py`
    1. add `"django_ssl_auth.SSLClientAuthMiddleware"` to your `MIDDLEWARE_CLASSES`
    2. add `"django_ssl_auth.SSLClientAuthBackend"` to your `AUTHENTICATION_BACKENDS`

#### Configuration 
There are two things you need to do in `settings.py`

1. Define a function that can return a dictionary with fields that
are required by your user model, e.g. `USER_DATA_FN = 'django_ssl_auth.fineid.user_dict_from_dn` is a sample implementation that takes the required fields from the DN of a Finnish government issued ID smart card for the `contrib.auth.models.User`.
2. To automatically create `User`s for all valid certificate holders, set `AUTOCREATE_VALID_SSL_USERS = True`. Auto-created users will be set to inactive by default, consider using the [`User.is_active`](https://docs.djangoproject.com/en/1.9/ref/contrib/auth/#django.contrib.auth.models.User.is_active) field in your [`LOGIN_DIRECT_URL`](https://docs.djangoproject.com/en/1.9/ref/settings/#login-redirect-url) view to notifying the user of their status.

For details, see `testapp/ssltest/settings.py`

#### Smart Card support

For (Finnish) instructions see `doc/fineid/FINEID.md`


## TODO

* Active directory integration.

## How to get help

Please do ask your questions on http://stackoverflow.com/
I am active there, and more likely to answer you publicly.
Also, you can try catching Kimvais on #django@freenode

