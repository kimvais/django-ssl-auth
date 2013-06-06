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
 _server certificate is valid_. If it is not.

### This module

1. run setup.py (sudo python setup.py install)
2. edit your `settings.py`
    2. add `"django_ssl_auth.SSLClientAuthMiddleware"` to your `MIDDLEWARE_CLASSES`
    3. add `"django_ssl_auth.SSLClientAuthBackend"` to your `AUTHENTICATION_BACKENDS`
    4. add a function to map DN to username `USERNAME_FN = lambda x: x'`

#### Configuration 
If your client certificates Distinguished names to not map 1:1,
you need to define a USERNAME_FN in your settings.py to extract the username
 from the DN, the above example assumes 1:1 mapping.

## TODO

Active directory integration.

## How to get help

Please do ask your questions on http://stackoverflow.com/
I am active there, and more likely to answer you publicly.
Also, you can try catching Kimvais on #django@freenode

