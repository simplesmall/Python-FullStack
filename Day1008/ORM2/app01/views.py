from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
import json
from app01.models import Book,Publish,Author,AuthorDetail,Emp


##################### 图书管理系统 视图函数 ##################

from django import forms
from app01.models import Publish,Author
from app01.form import BookModelForm



def book_view(request):
    book_list=Book.objects.all()
    return render(request,"book_view.html",{"book_list":book_list})




def book_add(request):

    if request.method=="GET":
        form=BookModelForm()
        return render(request,"book_add.html",{"form":form})
    else:

        form=BookModelForm(request.POST)
        if form.is_valid():
            # authors=form.cleaned_data.pop("authors")
            # book = Book.objects.create(**form.cleaned_data)
            # book.authors.add(*authors)
            obj=form.save() # create
            return redirect("/books/")
        else:

            return render(request, "book_add.html", {"form": form})






def book_edit(request,edit_book_id):
    edit_book = Book.objects.filter(pk=edit_book_id).first()
    if request.method=="GET":

        form=BookModelForm(instance=edit_book)
        return render(request,"book_edit.html",{"form":form})

    else:
        form=BookModelForm(request.POST,instance=edit_book)
        if form.is_valid():
            form.save() # update操作 ;  edit_book.update(**cleandata)
            return redirect("/books/")
        else:
            return render(request, "book_edit.html", {"form": form})







def book_del(request,del_book_id):

    Book.objects.filter(pk=del_book_id).delete()

    return redirect("/books/")
    #return HttpResponse("OK")




def book_ajax_del(request,del_book_id):
    response = {"state": True}
    try:
        Book.objects.filter(pk=del_book_id).delete()
    except Exception as e:
        response = {"state": False}

    return HttpResponse(json.dumps(response))
