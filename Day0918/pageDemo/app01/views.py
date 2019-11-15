from django.shortcuts import render
from django.http import  HttpResponse

from app01.models import  Book
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
def index(request):
    # for i in  range(100):
    #     Book.objects.create(title="title_%d"%i,price=i*i)
    # book_list1=[]
    # for i in range(1,101):
    #     book=Book(title="title_%d"%i,price=i*i)
    #     book_list1.append(book)
    # Book.objects.bulk_create(book_list1)

    # print(paginator.count)
    # print(paginator.num_pages)
    # print(paginator.page_range)
    #
    # page=paginator.page(5)
    # for i in page:
    #     print(i)
    #
    # print(page.has_next())
    # print(page.has_previous())
    #
    # print(page.next_page_number())
    # print(page.previous_page_number())
    print(request.GET)
    import copy
    params=copy.deepcopy(request.GET)
    params["xxx"]=123
    print(params.urlencode())
    book_list = Book.objects.all()
    paginator = Paginator(book_list, 10)
    try:
        current_page_num=request.GET.get("page",1)
        current_page=paginator.page(current_page_num)
    except EmptyPage  as e:
        current_page_num=1
        current_page=paginator.page(1)

    return  render(request,"index.html",{"current_page":current_page,"paginator":paginator,"current_page_num":int(current_page_num)})