
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes



clave = bytes.fromhex('e2cff885901a5449e9c448ba5b948a8c4ee377152b3f1acfa0148fb3a426db72')
iv = bytes.fromhex('00000000000000000000000000000000')


#Descifrado

try:
    texto_cifrado_bytes = b64decode('zcFJxR1fzaBj+gVWFRAah1N2wv+G2P01ifrKejICaGpQkPnZMiexn3WXlGYX5WnNgpZs3h0N4jLXi2xlV02D1g==')
    cipher = AES.new(clave, AES.MODE_CBC, iv)
    
    mensaje_des_bytes = cipher.decrypt(texto_cifrado_bytes)
   
    print(mensaje_des_bytes.hex())
    print("El texto en claro es: ", mensaje_des_bytes.decode("utf-8"))
    print("*********")
    
except (ValueError, KeyError) as error:
    print('Problemas para descifrar....')
    print("El motivo del error es: ", error) 