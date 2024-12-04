import requests
import binascii

block_size = 16
possbile_char = "abcdefCTF{}1234567890"
extracted_flag = '3234374354467b'

url = 'https://917b63e76a8d14a2.247ctf.com/'


for count in range(33):
    
    padding = 'AA'*(3*block_size - int(len(extracted_flag)/2) -1)

    for i in possbile_char:
        predicted_value = str(binascii.hexlify(bytes(i, 'utf-8')),'ascii')
        r1 = requests.get(url+'/encrypt?plaintext='+padding)
        a = r1.text
        a1 = r1.text[:96]
        r2 = requests.get(url+'/encrypt?plaintext='+padding+extracted_flag+predicted_value)
        b = r2.text
        b1 = r2.text[:96]
        if a1==b1:
            extracted_flag += predicted_value
            break
    print (binascii.unhexlify(extracted_flag).decode("utf-8"))