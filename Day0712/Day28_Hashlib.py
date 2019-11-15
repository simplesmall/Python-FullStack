import  hashlib

md5 = hashlib.md5()
md5.update(b"Hello")
md5.update(b"world")


print(md5.hexdigest())
print(len(md5.hexdigest()))

# helloworld  a165968b0a8084a041aed89bf40d581f
# hello  8b1a9953c4611296a827abf8c47804d7

md5 = hashlib.md5()
with open("Day28_EmulatorSSH.py","rb") as f:
    # md5.update(f.read())
#     d41d8cd98f00b204e9800998ecf8427e
    for line in f:
        md5.update(line)
        998
#    dca9fa6c95d741c73e23371c87b2e

print(md5.hexdigest())