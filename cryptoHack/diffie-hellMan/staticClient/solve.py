{"p": "0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff", "g": "0x260ce7a3c7940e68f896383d9d1025412a64a59b37494d9fa34dd4391a4448b6ad5b6f4dc6356113ff66766e2d279dfc041b38eb89e9a821a3ee5c7bd7a7c63f0ef3d8e6269b2734cbd17d5a2bc5ee3198937c1be1679a2bc948de5e39fae7a14235fe0ac2cad7a316c7f74c0048089b368565c150f788111f4908b8692b8c6039cb568db4393aa0ab7c6338ca6dfa26ead0bad168e22d6b5104a707fa17f0650516ac3884f84943ecc0cfd56d67d8024baa7deb087bb52d2378d89b4252a74f", "A": "0x1"}


{"B": "0x8d79b69390f639501d81bdce911ec9defb0e93d421c02958c8c8dd4e245e61ae861ef9d32aa85dfec628d4046c403199297d6e17f0c9555137b5e8555eb941e8dcfd2fe5e68eecffeb66c6b0de91eb8cf2fd0c0f3f47e0c89779276fa7138e138793020c6b8f834be20a16237900c108f23f872a5f693ca3f93c3fd5a853dfd69518eb4bab9ac2a004d3a11fb21307149e8f2e1d8e1d7c85d604aa0bee335eade60f191f74ee165cd4baa067b96385aa89cbc7722e7426522381fc94ebfa8ef0"}
B = 0xd1b8266f3efdaa1f8619aa264043cbdc31ce691df7c2cc212f8a5bbe7d56d704e4f6bdf8ab60a19734579bb656ce6d8a7eeaf777d4e437c543eca4e867d1c3999c70d7322e9dbb5ae5a90302205c1b4ae797f2031e10830c718527bd68c308c07050c59d956b21f6ed0063a16cc1474c18a54ada81c9b0deaa359c828498558a86c6f3b842ec9e554bfe073a007e31694d8963a8c53f1631294f044c8d566dd5d2334642a9b139b2b19c8a31e939238466324686561a3a078b182895d19df2e0
import json
from pwn import *
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad

def is_pkcs7_padded(message):
  padding = message[-message[-1]:]
  return all(padding[i] == len(padding) for i in range(0, len(padding)))



def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext


shared_secret = B

iv = "2977d786b0e7c6255d4cb406bbeac7eb"

ciphertext = "4c73a7a2b1524b33f7a069692fccbdb06ce91f12c8a283a31432d5cc18099824"

print(decrypt_flag(shared_secret, iv, ciphertext))
