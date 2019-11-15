from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def order(request):
    order_list = ['Card1','Card2','Card3',]
    return render(request,"order.html",{"order_list":order_list})

def shopping(request):
    shopping_list=["T-Shirt","Tooth-Brush","加爵牌小铁锤"]
    return  render(request,"shopping.html",{"shopping_list":shopping_list})