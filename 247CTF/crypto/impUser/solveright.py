import requests

# Step 1: Encrypt flag_user (using the /encrypt endpoint)
encrypt_url = "https://0d444a8a1a1127dc.247ctf.com/encrypt?user=666c"  # 'flag_user' in hex
response = requests.get(encrypt_url)

# Print the encrypted response
encrypted_flag_user = response.text.strip()
print(f"Encrypted flag_user: {encrypted_flag_user}")

# Step 2: Use the encrypted value in /get_flag to retrieve the flag
get_flag_url = f"https://0d444a8a1a1127dc.247ctf.com/get_flag?user={encrypted_flag_user}"
flag_response = requests.get(get_flag_url)

# Print the retrieved flag
print(f"Flag: {flag_response.text}")
