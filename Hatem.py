from cryptography.fernet import Fernet

# Generate a random encryption key
key = Fernet.generate_key()

# Create a Fernet cipher with the generated key
cipher = Fernet(key)

# Text to be encrypted
text_to_encrypt = "Hello, this is a secret message."

# Convert the text to bytes
text_bytes = text_to_encrypt.encode("utf-8")

# Encrypt the text
encrypted_text = cipher.encrypt(text_bytes)

print("Original Text: ", text_to_encrypt)
print("Encrypted Text: ", encrypted_text)
# Decrypt the encrypted text
decrypted_text = cipher.decrypt(encrypted_text)

# Convert the decrypted bytes back to a string
decrypted_text_str = decrypted_text.decode("utf-8")

print("Decrypted Text: ", decrypted_text_str)
