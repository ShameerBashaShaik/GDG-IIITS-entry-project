import random
import webbrowser
import hashlib
import subprocess
import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

print("""
╔════════════════════════════════════╗
║ GDG Cyber Guardians: Mission Start ║
╚════════════════════════════════════╝
ShadowNet stole AI secrets from GDG IIIT Sri City! As a rookie hacker, 
infiltrate their fortress. Crack the MD5 hash to breach the outer firewall.
""")



with open("wordlist.txt", "r") as f:
    words = [line.strip() for line in f if line.strip()]
chosenword=random.choice(words)

file='html1.html'
md5_hash = hashlib.md5(chosenword.encode()).hexdigest()

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>littleCTF</title>
    <link rel="stylesheet" href="all.css">

</head>
<body>
    <div class="container">
     <h1 id="welcome">Hmm, Good Approach</h1>
     <!-- Retro Cyber Hash Code for Level 1 is {md5_hash}-->
    </div>
    </body>
</html>
"""

with open("correct.html", "w") as f:
    f.write(html_content)

subprocess.run(["explorer.exe", "html1.html"])

print("\nEnter the answer to level up yourself: ")
response = input()

if response != chosenword:
    print("❌ Oops, it is not the one. Try again.")
    sys.exit()
else:
    print("""
    ╔════════════════════════════════════╗
    ║ GDG Cyber Guardians: Progress 20%  ║
    ╚════════════════════════════════════╝
    [██--------] Outer firewall breached! 
    """)
    print("✅ Great! Go ahead to the next level.")




print("\n\n")
print("""
╔════════════════════════════════════╗
║ GDG Cyber Guardians: Infiltration  ║
╚════════════════════════════════════╝
You're in ShadowNet's network! A SHA-256 hash guards the cipher vault. 
Solve it to unlock the next layer.
""")

chosenword1=random.choice(words)
sha256_hash = hashlib.sha256(chosenword1.encode()).hexdigest()
print("\nSimilarly solve the following hash to get a cipher text\n:"+sha256_hash)

response=input()
if response != chosenword1:
    print("❌ Oops, it is not the one. Try again.")
    sys.exit()
else:
    print("""
    ╔════════════════════════════════════╗
    ║ GDG Cyber Guardians: Progress 40%  ║
    ╚════════════════════════════════════╝
    [████------] Cipher vault unlocked!
    """)
    
    print("\n✅ Great! Take this.")




print("\n\n")
print("""
╔════════════════════════════════════╗
║ GDG Cyber Guardians: Vault Access  ║
╚════════════════════════════════════╝
The vault holds an AES-encrypted file with AI secrets. 
Use the first password as the key to decrypt it. Go deep to find some special tool if you need, run the hint.
""")

with open("lines.txt", "r", encoding='utf-8') as f:
    lines = [line.strip() for line in f if line.strip()]
    
    
message = random.choice(lines)
key = chosenword.ljust(16)[:16].encode()
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(pad(message.encode(), 16))
print(f"🔐 Ciphertext (hex): {ciphertext.hex()}\n")
print("\nWhat does it say:  ")
response=input()

if response != message:
    print("❌ Oops, it is not the one. Try again.")
    sys.exit()
else:
    print("""
    ╔════════════════════════════════════╗
    ║ GDG Cyber Guardians: Progress 60%  ║
    ╚════════════════════════════════════╝
    [██████----] AI secrets decrypted!
    """)
    print("\n✅ Great! Go Ahead, look inside to find a logo.\n")




print("\n\n")
print("""
╔════════════════════════════════════╗
║ GDG Cyber Guardians: Key Recovery  ║
╚════════════════════════════════════╝
The decrypted file hints at a logo hiding an RSA exponent. 
Find it to unlock the final challenge! The image is hidden so does data in it.
""")
response=input("\nFound anything inside it, like e:")
if response != "65537":
    print("\n❌ Oops, it is not the one. Try again.\n")
    sys.exit()
else:
    print("""
    ╔════════════════════════════════════╗
    ║ GDG Cyber Guardians: Progress 80%  ║
    ╚════════════════════════════════════╝
    [████████--] RSA key secured!
    """)
    print("\n✅ Great! Go Ahead, you have an rsa ahead\n")
file_path = os.path.join("deep", "secret.txt")
if os.path.exists(file_path):
    os.remove(file_path)





print("\n\n")
print("""
╔════════════════════════════════════╗
║ GDG Cyber Guardians: Final Mission ║
╚════════════════════════════════════╝
One last RSA-encrypted message holds the flag. 
Decrypt it to save the AI and join the Guardians!
""")

p = 10007
q = 10009
n = p * q
phi = (p - 1) * (q - 1)
e = 65537
d = pow(e, -1, phi)


message = "Ilovecyber"
m = int.from_bytes(message.encode(), 'big')

c = pow(m, e, n)

print("Encrypted:", c)

response=input()
if response!=message:
    print("\nOops it is not the one needed\n")
    sys.exit
else :
    print("\nYohooo you have captured the flag. Did great!!!\n")


print("""
╔════════════════════════════════════╗
║ GDG Cyber Guardians: Progress 100% ║
╚════════════════════════════════════╝
[██████████] Mission complete! Flag captured!
""")
