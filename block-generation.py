from _datetime import datetime
import hashlib
import random

def blockchain():
    blockid = input("Enter the blockid = ")
    timestamp = datetime.now()
    date_time = timestamp.strftime("%m/%d/%Y, %H:%M:%S")
    print("Date Time :: ",timestamp)
    data = input("Enter the data = ")
    nonce = random.randint(1,500)
    print("nonce = ",nonce)
    previous_hash=000
    print("previous block hash =" ,previous_hash)
    text = blockid + str(date_time+data) + str(nonce) + str(previous_hash)
    text1 = hashlib.md5(text.encode('utf-8')).hexdigest()
    print("new hash = ",text1)

blockchain()