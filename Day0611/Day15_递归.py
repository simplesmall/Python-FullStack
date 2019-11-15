import  os
def func(filepath,n):
    files = os.listdir(filepath)
    for file in files:
        file_p = os.path.join(filepath,file)
        if os.path.isdir(file_p):
            print("\t"*n,file)
            func(file_p,n+1)
        else:
            print("\t"*n,file)
    pass
func("d:/FullStackD",0)
