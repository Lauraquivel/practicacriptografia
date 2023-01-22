from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256
import binascii 
import os

my_path = os.path.abspath(os.getcwd())
key = my_path + "/clave-rsa-oaep-priv.pem"

key_priv = RSA.importKey(open(key).read())



# Firma del mensaje con PKCS#1 v1.5 esquema de firma (RSASP1)
msg = bytes('El equipo está preparado para seguir con el proceso','utf8')
hash = SHA256.new(msg)
signer = PKCS115_SigScheme(key_priv)
signature = signer.sign(hash)
print("Firma:", binascii.hexlify(signature))
