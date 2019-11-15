import  re
ret = re.findall(r"\d+","1-2*(60+(-40.35/5)-(-4*3))")
print(ret)
ret = re.findall(r"\d+\.\d+|\d+","1-2*(60+(-40.35/5)-(-4*3))")
print(ret)
#精准的渠道整数,去掉小数

ret = re.findall(r"\d+\.\d+|(\d+)","1-2*(60+(-40.35/5)-(-4*3))")
print(ret)
ret.remove("")
#取到整数
print(ret)

