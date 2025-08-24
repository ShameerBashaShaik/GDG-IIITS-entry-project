# Solution Guide: Cyber Heist Adventure CTF

This guide outlines the steps to solve the *Retro Cyber Heist Adventure* CTF, designed for the GDG IIIT Sri City club selection. Use tools like CyberChef, Hashcat, or Python to tackle the puzzles. Most importanlty use two shells, cause the hashes are randomised and each time you run a file, a new hash is picked.

## Level 1: MD5 Hash Crack

**Objective**: Breach ShadowNet's outer firewall by cracking an MD5 hash.

- **Approach**:
  1. Run `first.py`, which generates `html1.html` and opens it (on Windows) or prints the MD5 hash.
  2. Inspect `html1.html` (or terminal output) to find the hash in a comment.
  3. Use a hash-cracking tool (e.g., CyberChef, John the Ripper) with `wordlist.txt` to find the matching word.
  4. Input the word to proceed.

- **Tools**: CyberChef ("Hash" operation), Hashcat, John the Ripper
- **Tip**: The answer is a word from `wordlist.txt`. Try a dictionary attack.

## Level 2: SHA-256 Hash Crack

**Objective**: Unlock the cipher vault by solving a SHA-256 hash.

- **Approach**:
  1. The script outputs a SHA-256 hash.
  2. Use a hash-cracking tool with `wordlist.txt` to identify the word that produces the hash.
  3. Input the word to advance.

- **Tools**: CyberChef, Hashcat
- **Tip**: The process is similar to Level 1 but uses SHA-256. Check the same wordlist.

## Level 3: AES Decryption

**Objective**: Decrypt an AES-encrypted message to access ShadowNet's AI secrets.

- **Approach**:
  1. The script provides a ciphertext (hex) encrypted with AES in ECB mode.
  2. Use the word from Level 1 as the key (padded or truncated to 16 bytes).
  3. Decrypt the ciphertext using CyberChef ("AES Decrypt") or a Python script with `pycryptodome`.
  4. Input the decrypted message to proceed.
  5. Or you can use a python tool hidden in the directories.

- **Tools**: CyberChef, Python (`Crypto.Cipher.AES`)
- **Tip**: Ensure the key is exactly 16 bytes. ECB mode doesn’t require an IV.

## Level 4: RSA Exponent Hunt

**Objective**: Find the RSA public exponent hidden in a clue.

- **Approach**:
  1. The script prompts for a value "like e:65537".
  2. The exponent can be directly extracted using steghide.
  3. Input `65537` to move forward.

- **Tools**: steghide
- **Tip**: The exponent is a common RSA value. Look closely at the prompt.

## Level 5: RSA Decryption

**Objective**: Decrypt the final RSA-encrypted flag to capture the prize.

- **Approach**:
  1. The script provides the ciphertext (e.g., `27290802`), with `p=10007`, `q=10009`, `n=p*q=100160063`, and `e=65537`.
  2. Calculate the private key `d` using `phi=(p-1)*(q-1)=100140048` and `d=pow(e, -1, phi)`.
  3. Decrypt the ciphertext: `m=pow(c, d, n)`.
  4. Convert `m` to bytes (`m.to_bytes((m.bit_length() + 7) // 8, 'big')`) and decode to ASCII.
  5. Input the decrypted flag to win.

- **Tools**: CyberChef ("RSA Decrypt"), RsaCtfTool, Python
- **Tip**: Use provided `p` and `q` for faster decryption in tools like CyberChef.

## General Tips

- **Wordlist**: Wordlists can be explicitly mentioned in the cmd, no problem even if it is not mentioned for john the ripper cause it the default one for it.
- **Tools**: CyberChef, John-The Ripper is versatile for hashing and decryption. Python scripts can also solve all levels.
- **Debugging**: If stuck, inspect `wordlist.txt` or `lines.txt` for clues, or retry with a new run for different random words.
- **Narrative**: The story provides context but not direct answers. Focus on the cryptographic tasks.

This CTF balances accessibility and challenge, teaching core cryptography concepts through a fun narrative. Good luck, Cyber Guardians!

*Created by Shameer Basha Shaik for GDG IIIT Sri City Club Selection, August 2025*
