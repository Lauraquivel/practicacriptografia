from Crypto.Cipher import ChaCha20_Poly1305
from base64 import b64decode, b64encode
from Crypto.Random import get_random_bytes
import json

textoPlano = bytes('“Este curso es de lo mejor que podemos encontrar en el mercado"', 'UTF-8')
clave = bytes.fromhex('FF9DF30474898787A45605CCB9B936D33B780D03CABC81719D52383480DC3120')
nonce_mensaje = get_random_bytes(12)

#Cifrado
datos_asociados = bytes('Datos no cifrados sólo autenticados', 'utf-8')
cipher = ChaCha20_Poly1305.new(key=clave, nonce=nonce_mensaje)
texto_cifrado_bytes = cipher.encrypt(textoPlano)
cipher.update(datos_asociados)
texto_cifrado, tag = cipher.encrypt_and_digest(textoPlano)
print('Mensaje cifrado en HEX = ', texto_cifrado_bytes.hex() )
print('Mensaje cifrado en B64 = ', b64encode(texto_cifrado_bytes).decode())
texto_cifrado_hex = texto_cifrado_bytes.hex()


#Descifrado
decipher = ChaCha20_Poly1305.new(key=clave, nonce=nonce_mensaje)
plaintext_bytes = decipher.decrypt(bytes.fromhex(texto_cifrado_hex))
print('Mensaje en claro = ',plaintext_bytes.decode('utf-8'))

