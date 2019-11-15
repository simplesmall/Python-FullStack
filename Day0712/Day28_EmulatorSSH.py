import subprocess

res = subprocess.Popen("dir",
                       shell=True,
                       stderr=subprocess.PIPE,
                       stdout=subprocess.PIPE)

print(res.stdout.read().decode('gbk'))

import  struct

res = struct.pack("i",12321213)

print(res)
print(len(res))

obj = struct.unpack("i",res)
print(obj[0])
