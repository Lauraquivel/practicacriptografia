from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
import os


my_path = os.path.abspath(os.getcwd())
path_file_publ = my_path + "/clave-rsa-oaep-publ.pem"

#Clave publica del servidor (es decir el destino del mensaje)
key_publ = RSA.importKey(open(path_file_publ).read())


#Cifrado --> Voy a compartir una clave de cifrado simétrica con un servidor. Yo soy una aplicación de móvil. 
msg = bytes.fromhex("e2cff885901a5449e9c448ba5b948a8c4ee377152b3f1acfa0148fb3a426db72")

encryptor = PKCS1_OAEP.new(key_publ, SHA256)
encrypted = encryptor.encrypt(msg)

#print("Cifrado:", binascii.hexlify(encrypted))
print("Cifrado:", encrypted.hex())
print("--------------------------------------------------")
