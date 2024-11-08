from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib


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
        return plaintext.decode('ascii')


shared_secret = 1534027579878599529407245581770033581737409012139150291175054558125761392816482249439755265869871410639945814393096611058050317888277747259758551685684656418449750631734523806665480296095288478273861740761978543630344674992314373869588794915977913927865775525261328765815940781497413694511614398338667526745569294521583971158043085192808133609450610985080930043102002900559512749576021441013326208617708423765357557304629920935068696342850671128478464846284161128


iv = "bbc1d44ac14ddd9431efcc930f354951"

ciphertext = "82229127ceedd03e590e5e2d10c3c1b796487c796cd3725e77060b74eb06a80e"

print(decrypt_flag(shared_secret, iv, ciphertext))
