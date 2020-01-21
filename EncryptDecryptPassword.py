from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def generate_keys():
    #Generate a public/ private key pair using 4096 bits key length (512 bytes)
    new_key = RSA.generate(4096, e=65537)
    #The private key in PEM format
    private_key = new_key.exportKey("PEM")
    #The public key in PEM Format
    public_key = new_key.publickey().exportKey("PEM")
    print private_key
    fd = open("private_key.pem", "wb")
    fd.write(private_key)
    fd.close()
    print public_key
    fd = open("public_key.pem", "wb")
    fd.write(public_key)
    fd.close()

def encrypt_password(password):
    # Encrypting the password with public key
    with open("public_key.pem") as fd:
        public_key = fd.read()
    rsa_key = RSA.importKey(public_key)
    rsa_key = PKCS1_OAEP.new(rsa_key)

    # Encrypting the password
    return base64.b64encode(rsa_key.encrypt(password))


def decrypt_password(password):
    # Encrypting the password with public key
    with open("private_key.pem") as fd:
        private_key = fd.read()
    rsa_key = RSA.importKey(private_key)
    rsa_key = PKCS1_OAEP.new(rsa_key)

    # Encrypting the password
    return rsakey.decrypt(base64.b64decode(password))

#generate_keys()
#enc_pass = encrypt_password("ThisIsPassword")
#print enc_pass
dec_pass = encrypt_password("ZbQ3tQyXH4ancbk5ewNGeq9PN2Laqg2SLYy3TG7QF5Inz3UBgOpJAQsflSid+Hp1ektvlc1DK3qS3k6BMzxOsX3n/ZjL32/FHKZ50ctnT3LHr6LkF/PNbhbwc20rrG/ZfcTbcLU4oXyp+TlJXBlBm0n0bAhpK20RwqVVMe38K5HVhEdkq2sOMkL1qb1q0Usy2/KQEGtNL7dqBXP5o7Tw0pmASZIP9SNNm8UepjscweMz7AkHLIEd+fBdxeVoQjPcMU3IXYP/+rSkwKMRoAE7GY8xPd88zWKMDrsWwuOxDtwvNo+5RPzdENbBrdNLepNfsqRuUSopzvnwN7xJAJpkFofDd81vCiggsN0FR6zQV7+2vqkg5eYnIc+/oWT2R1PIZkJzA6n4Szeqby/NlVNFxzgg12lFIyBN/gclaulEiGfXhBFzdDjZljJWoTZk3uvulaR09O/odfj3A/hlpwHaxnr9cCHk4X9byfSvxNWiLDxZHN031DfabESgp4OMzfQXZozSHWvHJpIlzCobI+HC7r9LIbtIdsLSggrWh/mKNDQ291WD1/Io9+qtQEaK6RHUmxRDoWFc97KVcFyl1QUc49JIfUbohQIuYtVNIkpGB7zfeRzgJSfFezrL7vn3gLtrq8rcdqn6M39ymG7uWOpmEMODINc74yX65mUEOCuzaNI=")
print dec_pass
