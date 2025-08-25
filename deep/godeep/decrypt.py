from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

key = input("Enter key: ").ljust(16)[:16].encode()
print("\nEnter the Cipher Text\n")
your_ciphertext_here=input()
ciphertext = bytes.fromhex(your_ciphertext_here)
cipher = AES.new(key, AES.MODE_ECB)
plaintext = unpad(cipher.decrypt(ciphertext), 16)
print(plaintext.decode())
