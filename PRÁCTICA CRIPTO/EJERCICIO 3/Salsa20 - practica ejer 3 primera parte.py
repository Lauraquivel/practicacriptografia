from Crypto.Cipher import ChaCha20
from base64 import b64decode, b64encode

textoPlano = bytes('“Este curso es de lo mejor que podemos encontrar en el mercado"', 'UTF-8')
clave = bytes.fromhex('FF9DF30474898787A45605CCB9B936D33B780D03CABC81719D52383480DC3120')
nonce_mensaje = bytes.fromhex('f5871c9ff7f99c926102dd92')
print('nonce  = ', nonce_mensaje.hex())

#Cifrado
cipher = ChaCha20.new(key=clave, nonce=nonce_mensaje)
texto_cifrado_bytes = cipher.encrypt(textoPlano)
print('Mensaje cifrado en HEX = ', texto_cifrado_bytes.hex() )
print('Mensaje cifrado en B64 = ', b64encode(texto_cifrado_bytes).decode())
texto_cifrado_hex = texto_cifrado_bytes.hex()


#Descifrado
decipher = ChaCha20.new(key=clave, nonce=nonce_mensaje)
plaintext_bytes = decipher.decrypt(bytes.fromhex(texto_cifrado_hex))
print('Mensaje en claro = ',plaintext_bytes.decode('utf-8'))

