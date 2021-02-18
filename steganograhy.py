import cv2
import string
import os

d={}
c={}

for i in range(225):
    d[chr(i)]=i
    c[i]=chr(i)


def encrypt(text,x):
    kl=0
    tln=len(text)

    n=0
    m=0
    z=0

    length=len(text)

    for i in range(length):
        x[n,m,z]=d[text[i]]^d[key[kl]]
        n=n+1
        m=m+1
        m=(m+1)%3
        kl=(kl+1)%len(key)

    cv2.imwrite("encrypted.jpg",x)
    os.startfile("encrypted.jpg")
    print("steganography successfull")

def decrypt(text,x):
    kl=0
    tln=len(text)

    n=0
    m=0
    z=0
    length=len(text)
    ch=input("Press Enter key to exract hidden data")

    if ch=="":
        keyconform=input("Enter your password : ")
        decrypted_text=""

        if key==keyconform:
            for i in range(length):
                decrypted_text+=c[x[n,m,z]^d[key[kl]]]
                n+=1
                m+=1
                m=(m+1)%3
                kl=(kl+1)%len(key)
            print("Encrypted text : ",decrypted_text)

        else:
            print("Incorrect password")

    else:
        quit()        


    

x=cv2.imread("image.jpg")

i=x.shape[0]
j=x.shape[1]
print(i,j)

key=input("Enter password(for security purpose) : ")
text=input("Enter text to encrypt : ")
encrypt(text,x)
decrypt(text,x)



























    




    

