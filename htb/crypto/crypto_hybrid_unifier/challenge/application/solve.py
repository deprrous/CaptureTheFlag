from base64 import b64encode as be, b64decode as bd
from Crypto.Util.number import getPrime, long_to_bytes as l2b
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from secrets import randbelow
from hashlib import sha256
import os, json
import base64
import sympy
import hashlib

def establish_session_key( public_key):
    key = pow(public_key, b, p)
    return sha256(str(key).encode()).digest()
    
p = 0x89949c93a2cff302833bd8642e31c3cc146047e23c6752b1c0e6a86e92d4f015f0a37a008c9c7c0c4dcd512bdf5de9cd

g = 2
b = 1234567
client_public_key = pow(g,b,p)
# print("client ",client_public_key)
server_public_key = 0x10397b0940f060a66c23c10238d0f6b7caa7fcdcd0a6f2a31c9ec1a8df63988557224b20ead5ce2a717709248de6b18a

session_key = establish_session_key(server_public_key)
# print("session_key  ",session_key)

encrypted_challenge = "zjar+7XVu/jh2oUocV2LRuswQ4NGO3srTFyMTDG9llE/xxKP1JSoaPtkM4D44zof"
def encrypt_packet( packet):
    iv = os.urandom(16)
    cipher = AES.new(session_key, AES.MODE_CBC, iv)
    encrypted_packet = iv + cipher.encrypt(pad(packet.encode(), 16))
    return be(encrypted_packet)

def decrypt_packet( packet):
    decoded_packet = bd(packet.encode())
    iv = decoded_packet[:16]
    encrypted_packet = decoded_packet[16:]
    cipher = AES.new(session_key, AES.MODE_CBC, iv)

    decrypted_packet = unpad(cipher.decrypt(encrypted_packet), 16)
    packet_data = decrypted_packet

    
    return  packet_data

challenge = decrypt_packet(encrypted_challenge)
hashn = sha256(challenge).hexdigest()
print(hashn)


# print(hash(decrypt_packet(encrypted_challenge)))

# print(encrypt_packet("flag"))

enc_flag = "C5Rd6uURQFuRX5bukzOuf3NbUHV8fllYpQBmyPg8NWlbjyR9zAQSOvNSScUzukFWfHLA8n0uPy0cUEqM/EjVOzMJ2KovZjFkxiCrXgHGs+f/P7mV9LQp5f8p6/h/WxYG6VhwWpoJGF4iYIZomKS61RURDpS0HX4PyI09tZABzfg="
flag = decrypt_packet(enc_flag)
print(flag)