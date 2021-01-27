"""
Written by Konstantin Zubchenko

In order to understand and realize Diffie-Hellman algorithm in DH protocol.

27.01.2021
"""

import random

# The basic class, which providing all the math

class DH_Endpoint():
    def __init__(self, public_key1, public_key2, private_key):
        self.public_key1 = public_key1
        self.public_key2 = public_key2
        self.private_key = private_key
        self.full_key = None

    def generate_partial_key(self):
        partial_key = (self.public_key1 ** self.private_key) % self.public_key2
        return partial_key

    def generate_full_key(self, partial_key_r):
        full_key = (partial_key_r ** self.private_key) % self.public_key2
        self.full_key = full_key
        return full_key

    def encrypt_message(self, message):
        encrypted_message = ""
        key = self.full_key
        for i in message:
            encrypted_message += chr(ord(i) + key)
        return encrypted_message

    def decrypt_message(self, encrypted_message):
        decrypted_message = ""
        key = self.full_key
        for i in encrypted_message:
            decrypted_message += chr(ord(i) - key)
        return decrypted_message


# Sending message
message = "Try to hack me"

# Generating pub/priv keys for client and receiver on their side. Integers
# are much smaller then needed in case of simplifying training
j_public = 197
j_private = random.randint(0, 1000)
b_public = 151
b_private = random.randint(0, 1000)

# Making objects
John = DH_Endpoint(j_public, b_public, j_private)
Bob = DH_Endpoint(j_public, b_public, b_private)

# Generating part keys, that will flow through traffic to both: client and receiver
j_partial = John.generate_partial_key()
print(j_partial)

b_partial = Bob.generate_partial_key()
print(b_partial)

# Generating full keys to encrypt and decrypt messages depending on received part keys
j_full = John.generate_full_key(b_partial)
b_full = Bob.generate_full_key(j_partial)

# Conversation itself
b_encrypted = Bob.encrypt_message(message)
print(b_encrypted)

message = John.decrypt_message(b_encrypted)
print(message)
