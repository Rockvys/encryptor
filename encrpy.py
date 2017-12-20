import os
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

 hello = 'encrypt'
print hello

def encrypt(key,filename):
    chunksize = 64*1024
    outputFile = "(encrypted)" + filename
    filesize = str(os.path.getsize(filename)).zfill(16)
    IV = Random.new().read(16)
    encryptor - AES.new(key, AES.MOSE_CBC, IV)

     
