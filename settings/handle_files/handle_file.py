from Cryptodome.Cipher import AES
from hashlib import sha256
from os import urandom
import tarfile 
import shutil
import sys
import os



class Handle_files:
    def get_encrypt_zip_file(self, path_to_folders:str, out_path:str, password:str):
        for folders in os.listdir(path_to_folders):
            sys.stdout.write(f"\r[+] Encrypting folder: {path_to_folders}/{folders}")
            sys.stdout.flush()

            with tarfile.open(f'{out_path}/{folders}.tar.gz', "w:gz") as tar:
                tar.add(f'{path_to_folders}/{folders}', arcname=os.path.basename(f'{path_to_folders}/{folders}'))

            if not os.path.isdir(f'{out_path}/encrypted'):
                os.makedirs(f'{out_path}/encrypted')

            with open(f'{out_path}/{folders}.tar.gz', 'rb') as in_file_encrypt, \
                open(f'{out_path}/encrypted/{folders}.tar.gz', 'wb') as out_file_encrypt:
                self.encrypt_zip_file(in_file_encrypt, out_file_encrypt, password)

            shutil.move(f'{out_path}/encrypted/{folders}.tar.gz',
            f'{out_path}/{folders}.tar.gz')
            
            if os.path.isdir(f'{out_path}/encrypted'):
                os.rmdir(f'{out_path}/encrypted')

        return sys.stdout.write('\n')         

        
    def get_decrypt_file(self, path_to_folders:str, out_path:str, password:str):  

        for folders in os.listdir(path_to_folders):
            sys.stdout.write(f"\r[+] Decrypting folder: {path_to_folders}{folders}")
            sys.stdout.flush()

            if not os.path.isdir(f'{out_path}/decrypted'):
                os.makedirs(f'{out_path}/decrypted')
          
            with open(f'{path_to_folders}/{folders}', 'rb') as in_file_decrypt, \
            open(f'{out_path}/decrypted/{folders}', 'wb') as out_file_decrypt:
                self.decrypt_zip_file(in_file_decrypt, out_file_decrypt, password)

            shutil.move(f'{out_path}/decrypted/{folders}',
            f'{out_path}/{folders}')

            if os.path.isdir(f'{out_path}/decrypted'):
                os.rmdir(f'{out_path}/decrypted')
                
        return sys.stdout.write('\n')  
        
    def encrypt_zip_file(self, in_file:str, out_file:str, password:str):
        key = sha256(str.encode(password)).digest()
        iv = urandom(12)
        cipher = AES.new(key, AES.MODE_GCM, iv)
        cipher.update(b"aad")
        ciphertext, tag = cipher.encrypt_and_digest(in_file.read())
        [ out_file.write(x) for x in (cipher.nonce, tag, ciphertext) ]


    def decrypt_zip_file(self, in_file:str, out_file:str, password:str):
        key = sha256(str.encode(password)).digest()
        nonce, tag, ciphertext = [ in_file.read(x) for x in (12, 16, -1) ]
        cipher = AES.new(key, AES.MODE_GCM, nonce)
        cipher.update(b"aad")
        plaintext = cipher.decrypt_and_verify(ciphertext, tag)
        out_file.write(plaintext)