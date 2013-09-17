# How to use the Finnish e-ID (FINeID) cards in Django on OS X

## Client side:

Instructions in Finnish (Ohjeita suomeksi):
* http://hopeinenomena.net/viewtopic.php?f=44&t=71540

1. Install the official card reader software http://www.fineid.fi/
1. Install OpenSC http://dl.dropbox.com/u/7089298/OpenSC/OpenSC-0.12.2-10.8.dmg
1. Install libtool (sudo port install libtool)
1. Create a critical symlink: sudo ln -s /opt/local/lib/libltdl.7.dylib /usr/lib
1. `pkcs15-tool -D` should now show something like:
    Using reader with a card: ACS ACR38U-CCID 00 00
    PKCS#15 Card [HENKILOKORTTI]:
        Version        : 1
        Serial number  : 12345678901234567890
        Manufacturer ID: VRK-FINEID
        Language       : fi
        Flags          : Login required
        ...
1. Reboot (Fastest way to get KeyChain access to pick up the new keychain
        "HENKILOKORTTI")
1. Going to URL https://vrk.fineid.fi/ should now prompt for Certificate and
PIN code in both Safari and Google Chrome

## Server side:

1. set up your django app with `django_ssl_auth` as specified in the top-level
README.md
1. Download the CA certificates from the Finnish Population Register Centre
(`make` in this directory, or manually):
    1. wget http://vrk.fineid.fi/certs/vrkrootc.crt
    1. wget http://vrk.fineid.fi/certs/vrkcqc.crt
    1. openssl x509 -inform der -outform pem -in vrkcqc.crt >> vrkca.crt
    1. openssl x509 -inform der -outform pem -in vrkrootc.crt >> vrkca.crt
1. Set-up your nginx (see `nginx.conf`)
1. Run the `testapp`
    1. `export DJANGO_SETTINGS_MODULE=ssltest.settings`
    1. `gunicorn ssltest.wsgi`
    1. navigate to `https://localhost/fi` and you should see your name and SATU
    in a not-at-all-formatted view.

Further information about the Finnish Gov.t CAs

http://fineid.fi/default.aspx?docid=2237&site=9&id=332
