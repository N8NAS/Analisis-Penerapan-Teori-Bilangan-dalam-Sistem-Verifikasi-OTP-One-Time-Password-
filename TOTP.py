import time
import hmac
import hashlib
import base64
import struct

def buat_totp(secret, interval=30, digits=6):
    key = base64.b32decode(secret.upper())
    counter = int(time.time()) // interval
    counter_bytes = struct.pack(">Q", counter)
    hmac_hash = hmac.new(key, counter_bytes, hashlib.sha1).digest()

    offset = hmac_hash[-1] & 0x0F
    truncated_hash = hmac_hash[offset:offset+4]
    kode = struct.unpack(">I", truncated_hash)[0] & 0x7FFFFFFF
    return str(kode % 10**digits).zfill(digits)

def verifikasi_totp(secret, user_input, interval=30, digits=6):
    current_otp = buat_totp(secret, interval, digits)
    return user_input == current_otp

secret = 'TEORIBILANGAN765'
generated_otp = buat_totp(secret)

print("Kode TOTP saat ini:", generated_otp)
user_input = input("Masukkan kode OTP: ")

if verifikasi_totp(secret, user_input):
    print("OTP benar!")
else:
    print("OTP salah.")
