import os
import argparse
from pickletools import optimize
import sys
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from click import Argument


parser=argparse.ArgumentParser()
parser.add_argument('option')
parser.add_argument('device')
arg=parser.parse_args()
if arg.option=="eject":
    device=open(arg.device,'rb')
    contents=device.read()
    h=SHA256.new(contents)
    with open("./Key_private.out", 'rb') as f: key = f.read()
    rsa = RSA.importKey(key)
    signer = PKCS1_v1_5.new(rsa)
    signature = signer.sign(h)
    with open("/home/faizan/Assignment/1/.signature",'wb') as f: f.write(signature)
elif arg.option=="mount":
    device=open(arg.device,'rb')
    contents=device.read()
    h=SHA256.new(contents)
    with open("/home/faizan/Assignment/1/Key_public.out", 'rb') as f: key = f.read()
    rsa = RSA.importKey(key)
    signer = PKCS1_v1_5.new(rsa)
    with open("/home/faizan/Assignment/1/.signature",'rb') as f: 
        orig_sign=f.read()
        if signer.verify(h,orig_sign):
            print("Integrity passed")
        else:
            print("The integrity is failed")


