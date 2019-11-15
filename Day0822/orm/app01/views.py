from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from app01.models import Book
from django.urls import reverse


def addbook(request):
    # 方式一
    # book=Book(title="python",price=23,pub_date="2013-12-24",publish="电子工业出版社")
    # book.save()
    # print(book.nid)

    # 方式二
    # 注意  create 方法返回的是当前的表记录对象
    # book=Book.objects.create(title="Linux", price=123, pub_date="2013-12-24", publish="电子工业出版社")
    # print(book.price)
    # print(book.nid)
    if request.method == "POST":
        print(request.POST)

        # 方法一
        # title = request.POST.get("title")
        # price = request.POST.get("price")
        # pub_date = request.POST.get("pub_date")
        # publish = request.POST.get("publish")
        # book = Book.objects.create(title=title, price=price, pub_date=pub_date, publish=publish)

        # 方法二
        data = request.POST.dict()
        del data["csrfmiddlewaretoken"]
        book = Book.objects.create(**data)

        return redirect(reverse("books"))
    else:
        return render(request, "addbook.html")


def books(request):
    book_list = Book.objects.all()
    return render(request, "books.html", locals())


def delbooks(request, delete_book_id):
    Book.objects.filter(nid=delete_book_id).delete()
    return redirect(reverse("books"))


def editbooks(request, edit_book_id):
    # Book.objects.filter(nid=edit_book_id).update(price=120)

    if request.method == "POST":
        title = request.POST.get("title")
        price = request.POST.get("price")
        pub_date = request.POST.get("pub_date")
        publish = request.POST.get("publish")
        book = Book.objects.filter(nid=edit_book_id).update(title=title, price=price, pub_date=pub_date,
                                                            publish=publish)
        return redirect(reverse("books"))
    else:
        edit_book = Book.objects.filter(nid=edit_book_id)[0]
        return render(request, "editbook.html", {"edit_book": edit_book})


def query(request):
    # all 方法,返回的是 queryset
    # ret=Book.objects.all()   #  由  __str__返回的数据
    # print(ret)  # <QuerySet [<Book: Go>, <Book: JAVA>, <Book: Djando>, <Book: Djando>, <Book: Djando>, <Book: Python全栈开发之入门第0天>]>
    # return HttpResponse("查询成功")

    #  filter() 方法 返回的是一个queryset
    # book=Book.objects.filter(title='JAVA')
    # print(book)   # <QuerySet [<Book: JAVA>]>

    #   get 方法 返回查询到的 model 对象   get方法可以查出有且只有一个对象,超过或者不足一个就报错
    # ret = Book.objects.get(title='JAVA')
    # print(ret.price)   # JAVA

    # first() 与 last()  方法 返回的是model对象 first()相当于查询出queryset之后在里面加[0]

    #排除
    # ret = Book.objects.exclude(price=23)
    # print(ret)   #<QuerySet [<Book: Djando>, <Book: Python全栈开发之入门第0天>]>

    # order by  默认是升序,要降序排列显示的话要在变量前面加"  -  " 号
    # ret = Book.objects.all().order_by("-price")
    # print(ret)

    # ret = Book.objects.filter(price=122).exists()
    # print(ret)

    # ret = Book.objects.all().values("title")
    # print(ret)   # <QuerySet [{'title': 'Go'}, {'title': 'JAVA'}, {'title': 'flutter'}, {'title': 'cocos'}, {'title': 'Django'}, {'title': 'Python全栈开发之入门第0天'}]>

    # ret = Book.objects.all().values_list("title")
    # #  返回的是一个元组
    # print(ret)  #  <QuerySet [('Go',), ('JAVA',), ('flutter',), ('cocos',), ('Django',), ('Python全栈开发之入门第0天',)]>

    # ret= Book.objects.all().values("title")
    #  <QuerySet [{'title': 'Go'}, {'title': 'JAVA'}, {'title': 'flutter'}, {'title': 'cocos'}, {'title': 'Django'}, {'title': 'Python全栈开发之入门第0天'}, {'title': 'flutter'}]>
    # ret= Book.objects.all().values("title").distinct()
    # print(ret)

    book=Book.objects.filter(price__gt=100) #  价格大于200的
    # book=Book.objects.filter(price__gte=100) #  价格大于等于200的

    #  lt  小于  in  在其中   range  从..到..  contains 包含  icontains    startswith   istartswith

    print(book)

    return HttpResponse("查询成功")
