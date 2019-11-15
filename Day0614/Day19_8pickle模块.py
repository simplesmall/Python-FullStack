import pickle
dic = {(1,2,3):{'a','b'},1:'abc'}
ret = pickle.dumps(dic)
print(ret)
#dumps 序列化的结果只能是字节
print(pickle.loads(ret))