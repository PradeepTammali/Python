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
dec_pass = encrypt_password(enc_pass)
print dec_pass
