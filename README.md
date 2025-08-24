# Cyber Heist Adventure: A Cryptographic CTF Challenge

## Overview

Welcome to **Cyber Heist Adventure**, a terminal-based Capture-The-Flag (CTF) challenge I created for the GDG IIIT Sri City club's Cybersecurity: Cryptographic Puzzle Design project. In this multi-layered puzzle, you play as a cutie-hacker recruited by the *GDG Cyber Guardians* to recover stolen AI secrets from the villainous *ShadowNet*. Each level tests your skills in cryptography and problem-solving, with a thrilling storyline to keep you hooked!

This CTF combines hash cracking, AES decryption, and RSA cryptography, designed to challenge both beginners and seasoned enthusiasts. It’s built to run entirely in the terminal, making it accessible and authentic to real-world cybersecurity challenges.

## Challenge Structure

The CTF consists of five levels, each with increasing difficulty:

- **Level 1: MD5 Hash Crack** - Break an MD5 hash hidden in an HTML file to breach the outer firewall.
- **Level 2: SHA-256 Hash Crack** - Solve a SHA-256 hash to unlock the cipher vault.
- **Level 3: AES Decryption** - Decrypt an AES-encrypted message using a key derived from Level 1.
- **Level 4: RSA Exponent Hunt** - Find the RSA public exponent (65537) hidden in a clue.
- **Level 5: RSA Decryption** - Decrypt the final RSA-encrypted flag to capture the prize.

Each level provides feedback and a progress bar (e.g., `[████------] 40%`) to track your journey.

## Features

- **Cryptographic Techniques**: Implements MD5, SHA-256, AES (ECB mode), and RSA encryption.
- **Story-Driven**: A "Cyber Heist" narrative ties the puzzles together, with ASCII art and thematic progress updates.
- **Progressive Difficulty**: Starts with simple hash cracking and builds to complex RSA decryption.
- **Terminal-Based**: No UI needed, ensuring accessibility and a hacker-like experience.
- **Replayability**: Random word selection from `wordlist.txt` makes each run unique.

## Setup Instructions

### Prerequisites

- Python 3.x
- Required libraries: `pycryptodome` (for AES and RSA)

```bash
pip install pycryptodome
```

- Files: Ensure `wordlist.txt` and `lines.txt` are in the same directory as `first.py`.

### How to Run

1. Clone or download the project files.
2. Ensure `wordlist.txt` (list of words for hash challenges) and `lines.txt` (messages for AES encryption) are present.
3. Run the script in a terminal:

```bash
python3 first.py
```

4. Follow the prompts to solve each level. Use tools like CyberChef, Hashcat, or John the Ripper for hash cracking, and Python or CyberChef for decryption tasks.

## Tools You Might Need

- **Hash Cracking**: CyberChef, John the Ripper, or Hashcat.
- **Decryption**: CyberChef (for AES and RSA) or custom Python scripts.
- **Text Analysis**: `cat`, `grep`, or any text editor to inspect files like `wordlist.txt`.

- Also use two shells, cause each time the python file is run the hashes are modified.
---
## Solution
There is a solution.md file placed in the github repo for some reference.


*Created by Shameer Basha Shaik for GDG IIIT Sri City Club Selection, August 2025*
