from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Index")

def app01index(request):
    return HttpResponse("App01 index")

def defaultIndex(request):
    return render(request, "html/default_index.html")