from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

NONCE_SIZE = 12  # Define the nonce size for AES GCM

def aes_gcm_decrypt(ciphertext, key, nonce):
    aesgcm = AESGCM(key)
    plaintext = aesgcm.decrypt(nonce, ciphertext, None)
    return plaintext

def decrypt_file(input_file, output_file, key, nonce):
    with open(input_file, 'rb') as f_in:
        encrypted_data = f_in.read()
        nonce = encrypted_data[:NONCE_SIZE]  # Extract nonce from the encrypted data
        ciphertext = encrypted_data[NONCE_SIZE:]  # Rest is ciphertext
    
    plaintext = aes_gcm_decrypt(ciphertext, key, nonce)
    
    with open(output_file, 'wb') as f_out:
        f_out.write(plaintext)

def main():
    key = b'\x00' * 32  # Hardcoded key (replace with your actual key)
    input_directory = "chunkenc/"
    output_directory = "chunkdec/"

    os.makedirs(output_directory, exist_ok=True)

    # Decrypt each file separately
    for file_name in os.listdir(input_directory):
        input_file = os.path.join(input_directory, file_name)
        output_file = os.path.join(output_directory, file_name[:-13] + "_decrypted.txt")  # Change the file extension
        
        decrypt_file(input_file, output_file, key, None)
        print(f"Decryption completed for {file_name}.")

if __name__ == "__main__":
    main()
