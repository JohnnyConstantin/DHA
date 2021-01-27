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


message = "This is a test message"
j_public = 197
j_private = 199
b_public = 151
b_private = 157
John = DH_Endpoint(j_public, b_public, j_private)
Bob = DH_Endpoint(j_public, b_public, b_private)

j_partial = John.generate_partial_key()
print(j_partial)

b_partial = Bob.generate_partial_key()
print(b_partial)

j_full = John.generate_full_key(b_partial)
b_full = Bob.generate_full_key(j_partial)

b_encrypted = Bob.encrypt_message(message)
print(b_encrypted)

message = John.decrypt_message(b_encrypted)
print(message)

