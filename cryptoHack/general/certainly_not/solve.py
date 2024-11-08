from Crypto.PublicKey import RSA
import base64

# Load the PEM private key file
with open('convertedfromder.pem', 'r') as file:
    pem_data = file.read()

# Remove header and footer
pem_data = pem_data.replace("-----BEGIN CERTIFICATE-----", "")
pem_data = pem_data.replace("-----END CERTIFICATE-----", "")
pem_data = pem_data.strip()

# Decode the Base64 content
binary_data = base64.b64decode(pem_data)

# Load the RSA key
private_key = RSA.import_key(binary_data)


# Get the modulus (n) and private exponent (d) in decimal
n_decimal = private_key.n
d_decimal = private_key.d

print("Modulus (n) in decimal:", n_decimal)
print(d_decimal)
