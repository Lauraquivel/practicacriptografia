import jwt

#Ticket de autenticacion que lo aporta el servidor de autenticación.
encoded_jwt = jwt.encode({"usuario": "Don Miguel Feroz", "rol": "isNormal"}, "“Con KeepCoding aprendemos", algorithm="HS256")

print(encoded_jwt)

#Verificación del propio servidor de autenticación (o delegado) es correcto
decode_jwt = jwt.decode(encoded_jwt,"“Con KeepCoding aprendemos", algorithms="HS256")

print(decode_jwt)

