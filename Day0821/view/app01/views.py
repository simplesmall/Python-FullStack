from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def indextest(request):
    print(request.method)
    print(request.path)
    print(request.POST)
    print(request.GET)
    print(request.get_full_path)
    return  HttpResponse("INDEX")

def index(request):
    fruit = "Apple"
    food="意大利面"
    lst=['12','qwe','中国']
    return render(request,"index.html",{"name":fruit,"eat":food,"list":lst})

def redirect(request):
    return redirect("redirect.html")