from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    Kwan = {"Fir":'111',"Sec":'222'}
    class Animal():
        def __init__(self,name,age):
            self.name=name
            self.age =age
        def running(self):
            return "Running"
    Alex=Animal("Alex",123)
    Bill = Animal("Bill",567)
    Jush = Animal("Jush",234)
    personList=[Alex,Bill,Jush]
    import datetime
    now=datetime.datetime.now()

    book_list =[]

    sliceTest = "HELLO DJANGO"
    link="<a href='http://www.baidu.com'>BAIDUYIHA</a>"
    return render(request,"index.html",locals())