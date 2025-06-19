import hmac
import hashlib
import base64
import struct
import random

def buat_otp(secret, counter, digits = 6):
    key = base64.b32decode(secret.upper())
    msg = struct.pack(">Q", counter)
    h = hmac.new(key, msg, hashlib.sha1).digest()
    offset = h[-1] & 0x0F
    potong = h[offset:offset+4]
    kode = struct.unpack(">I", potong)[0] & 0x7FFFFFFF
    return str(kode % 10**digits).zfill(digits)

secret = 'MYSECRETKEY23456'

counter = random.randint(0, 100000)

otp = buat_otp(secret, counter)
print("OTP yang dikirim ke pengguna:", otp)
masukan = input("Masukkan OTP: ")

if masukan == otp:
    print("OTP valid!")
else:
    print("OTP salah.")
