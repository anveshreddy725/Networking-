import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random
from Crypto.Hash import SHA256

class CryptoRSA:

    PRIVATE_KEY_FILE = "private_key.pem"
    PUBLIC_KEY_FILE = "public_key.pem"

    def __init__(self):
        return
        
    def __save_file(self, contents, file_name):
        f= open(file_name, 'w')
        f.write(contents)
        f.close()

    def __read_file(self, file_name):
        f= open(file_name, 'r')
        contents = f.read()
        f.close()
        return contents

    def __generate_random(self):
        return Random.new().read()

    def generate_keys(self):
        keys = RSA.generate(4096)
        private_key= keys.exportKey("PEM")
        public_key = keys.publickey().exportKey("PEM")
        str_private_key = bytes.decode(private_key)
        str_public_key = bytes.decode(public_key)
        self.__save_file(str_private_key, self.PRIVATE_KEY_FILE)
        self.__save_file(str_public_key, self.PUBLIC_KEY_FILE)
        print(f"Private keys : {str_private_key} ")
        print(f"Public keys : {str_public_key} ")

    def encrypt(self, cleartext, public_keypath=None):
        if (public_keypath == None):
            public_keypath = self.PUBLIC_KEY_FILE

        public_key = RSA.importKey(self.__read_file(public_keypath))
        cipher = PKCS1_OAEP.new(public_key)
        encrypted_data = cipher.encrypt(cleartext.encode("utf8"))
        return base64.b64encode(encrypted_data)

    def decrypt(self, cipher_text, private_keypath=None):
        if private_keypath == None:
            private_keypath = self.PRIVATE_KEY_FILE

        cipher_text = base64.b64decode(cipher_text)
        private_key = RSA.importKey(self.__read_file(private_keypath))
        cipher = PKCS1_OAEP.new(private_key)
        return cipher.decrypt(cipher_text)



#sample text encrypt

print('IFT 510 Anvesh ')
CryptoRSA().generate_keys()
encrypted_data = CryptoRSA().encrypt("hello World")
print(encrypted_data)

#decrypt
decrypted_data = CryptoRSA().decrypt(encrypted_data)
print(decrypted_data)
