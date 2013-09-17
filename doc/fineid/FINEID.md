# Suomalaisen henkilÃ¶kortin kÃ¤yttÃ¶ Django SSL -kirjautumiseen

Ohjeita:
* http://hopeinenomena.net/viewtopic.php?f=44&t=71540

1. Asenna viralliset softat http://www.fineid.fi/
1. Asenna OpenSC http://dl.dropbox.com/u/7089298/OpenSC/OpenSC-0.12.2-10.8.dmg
1. Asenna libtool (sudo port install libtool)
1. sudo ln -s /opt/local/lib/libltdl.7.dylib /usr/lib
1. pkcs15-tool -D piÃ¤isi tulostaa jotain seuraavankaltaista:
    Using reader with a card: ACS ACR38U-CCID 00 00
    PKCS#15 Card [HENKILOKORTTI]:
        Version        : 1
        Serial number  : 12345678901234567890
        Manufacturer ID: VRK-FINEID
        Language       : fi
        Flags          : Login required
        ...
1. Rebootski.
1. https://vrk.fineid.fi/ pitÃ¤isi kysyÃ¤ varmennetta kortiltasi...


Laita nginx.conf:n ssl_client_certificate  osoittaamaan tiedostoon jossa on "VRK Gov. CA for Citizen Qualified Certificates" PEM-muodossa (Oikealla hiirennapilla "Save as" mPollux DigiSign -asiakasohjelmassa ja sen jÃ¤lkeen "openssl x509 -inform der -outform -pem vrk-intermediate.ca.cer vrk-i-ca.pem"

Lataa Väestörekisterikeskuksen juurivarmenne ja Valtion
kansalaisvarmenteet (ks. Makefile)

1. wget http://vrk.fineid.fi/certs/vrkrootc.crt
1. wget http://vrk.fineid.fi/certs/vrkcqc.crt
1. openssl x509 -inform der -outform pem -in vrkcqc.crt >> vrkca.crt
1. openssl x509 -inform der -outform pem -in vrkrootc.crt >> vrkca.crt

http://fineid.fi/default.aspx?docid=2237&site=9&id=332
