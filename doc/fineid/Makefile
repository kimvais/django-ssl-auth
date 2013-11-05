all: clean ca

ca:
	wget http://vrk.fineid.fi/certs/vrkrootc.crt
	wget http://vrk.fineid.fi/certs/vrkcqc.crt
	openssl x509 -inform der -outform pem -in vrkcqc.crt >> vrkca.crt
	openssl x509 -inform der -outform pem -in vrkrootc.crt >> vrkca.crt

clean:
	rm *.crt || true
