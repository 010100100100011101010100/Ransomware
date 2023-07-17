import os
from cryptography.fernet import Fernet as i
files=[]
for f in os.listdir():
    if f=="one" or f=="thisisit" or f=="sec":
        continue
    if os.path.isfile(f):
        files.append(f)
for file in files:
    with open(file,"rb") as f:
        contents=f.read()
    con=i(key).decrypt(contents)
    with open(file,"wb") as c:
        c.write(con)

        

