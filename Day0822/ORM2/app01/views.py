from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from app01.models import Book, Publish, Author, AuthorDetail,Emp


def index(request):
    return HttpResponse("OKK")

def addrecord(request):
    '''
    添加记录
    '''

    pub_obj = Publish.objects.filter(name="南京出版社").first()

    # 插入的书籍本身也是一个对象,该对象也是可以赋值给一个变量进而进行下一步操作的
    book=Book.objects.create(
        title="Python",
        price=122,
        pub_date="2017-12-23",
        # 一对多的实现方法  第一种方法 直接在"一"里面指定对应字段以及对应字段的值
        # publish_id=1
        # 方法二 以对象的形式来实现
        publish=pub_obj
    )

    # 多对多的绑定方式
    # 方式一
    alex=Author.objects.filter(name="alex").first()
    egon=Author.objects.filter(name="egon").first()
    # 先将要插入记录的记录 查出来并赋值给一个变量,其实是一个对象类型,然后再插入到有 对应关系的表中
    book.authors.add(alex,egon)
    # 也可以直接在这里添加字段,括号里面的1,2分别就是author 表中的记录的关键字ID,这样使用的缺点就是不知道所使用的ID到底是什么意思
    # 方式二
    # book.authors.add(1,2)
    # 方式三
    # book.authors.add(*[1,2])

    return HttpResponse("添加成功")

def delrecord(request):
    book = Book.objects.filter(nid=4).first()
    # 解除定向绑定
    alex = Author.objects.filter(name="alex").first()
    egon = Author.objects.filter(name="egon").first()
    # book.authors.remove(alex)
    book.authors.set(1)
    return HttpResponse("删除成功")

def  query(request):
    ########################## 基于对象的跨表查询 #############################
    '''
    正向查询
    反向查询
      book.publish
    Book  -----  Publish

    反向查询表名小写_set.all() : pub_obj.book_set.all()

    '''
    # 1查询这本书出版社的名字和邮箱
    # book=Book.objects.filter(title="JAVA").first()
    # pub_obj=Publish.objects.filter(nid=book.publish_id).first()
    # print(pub_obj.name)
    # print(pub_obj.email)
    # return HttpResponse("查询成功")
    # book=Book.objects.filter(title="JAVA").first()
    # print(book.publish) # 与book这本书关联的传射对象
    # print(book.publish.name)
    # print(book.publish.email)
    # return HttpResponse("再次成功返回")


    # 2.查询某个出版社出版的所有书籍的名称
    # pub_obj = Publish.objects.get(name="南京出版社")
    # print(pub_obj.book_set.all().values_list("title"))
    # return  HttpResponse("查询倒是成功了,但是并没有返回任何东西")

    ################多对多######################
    '''
    正向查询
        book.authgor.all()
    BOOK ----------------------Author
    
    反向查询
       按表名小写_set.all()
    '''
    # 查询某本书是由哪些作者参与编写的
    book = Book.objects.filter(nid=4).first()
    ret=book.authors.all().values("name")
    print(ret)

    # 查询某个作者参与编写过的书籍
    author=Author.objects.filter(name="egon").first()
    print(author.book_set.all())


    ################ 一对一 #######
    #  正向查询按字段  alex.ad.tel
    # 查询alex 手机号
    alex = Author.objects.filter(name="alex").first()
    print(alex.ad.tel)

    #  反向查询按表明小写  ad.author
    # 查询手机号为112的作者的name
    ad = AuthorDetail.objects.filter(tel=112).first()
    print(ad.author.name)

    return HttpResponse("返回一些东西啦")

def book_view(request):
    book_list = Book.objects.all()
    return render(request,"book_view.html",{"book_list":book_list})

def book_add(request):
    if request.method=="GET":
        publish_list=Publish.objects.all()
        author_list=Author.objects.all()
        return  render(request,"book_add.html",{"publish_list":publish_list,"author_list":author_list})
    else:
        title=request.POST.get("title")
        price=request.POST.get("price")
        pub_date=request.POST.get("pub_date")
        publish_id=request.POST.get("publish_id")
        authors=request.POST.getlist("authors")
        print(request.POST)
        print(authors)

        book=Book.objects.create(title=title,price=price,pub_date=pub_date,publish_id=publish_id)
        book.authors.add(*authors)
        return redirect("/books/")


def book_edit(request,edit_book_id):
    edit_book = Book.objects.filter(pk=edit_book_id).first()

    if request.method=="GET":
        publish_list = Publish.objects.all()
        author_list = Author.objects.all()
        return render(request,"book_edit.html",{"edit_book":edit_book,"publish_list":publish_list,"author_list":author_list})
    else:
        title = request.POST.get("title")
        price = request.POST.get("price")
        pub_date = request.POST.get("pub_date")
        publish_id = request.POST.get("publish_id")
        authors = request.POST.getlist("authors")
        print(request.POST)
        print(authors)

        Book.objects.filter(pk=edit_book_id).update(title=title,price=price,pub_date=pub_date,publish_id=publish_id)
        edit_book.authors.set(authors)

        return redirect("/books/")

def book_del(request,book_del_id):
    Book.objects.filter(pk=book_del_id).delete()

    return redirect("/books/")

def query2(request):
    '''
    基于双下划线的跨表查询(基于join实现的)
    正向查询按字段,反向查询表名小写加下划线加字段
    :param request:
    :return:
    '''
    #1=1 1查询这本书出版社的名字和邮箱
    ret = Book.objects.filter(title="python").values("publish__name")
    pub=Publish.objects.filter(book__title="JAVA").values("name")
    print(pub)
    # 1=多2.查询某个出版社出版的所有书籍的名称
    bknm=Publish.objects.filter(name="南京出版社").values("book__title")
    Book.objects.filter(publish__name="北京出版社").values("title")
    print(bknm)
    # 1=多 3查询某本书作者的nianl
    auage=Book.objects.filter(title="python").values("authors__age")
    Author.objects.filter(book__title="JAVA").values("age")
    print(auage)
    # 1=多4查询某个作者出版过的书籍
    Book.objects.filter(authors__name="alex").values("title")
    Author.objects.filter(name="egon").values("book__title")

    # i=1 5 查询alex 手机号
    Author.objects.filter(name="alex").values("ad__tel")
    AuthorDetail.objects.filter(author__name="alex").values("tel")
    # 1=1 6 查询手机号为110的作者的名字
    AuthorDetail.objects.filter(tel=110).values("author__name")
    Author.objects.filter(ad__tel=110).values("name")

    ##############################连续跨表##################
    # 查询人民出版社传出版过的所有书籍的名字以及作者的姓名
    res1=Publish.objects.filter(name="南京出版社").values("book__title","book__authors__name")
    res12=Book.objects.filter(publish__name="北京出版社").values("title","authors__name")
    print('RESULT',res1,'\r\n',res12)

    #  手机号以110开头的作者出版过的所有书籍名称以及出版社名称
    # 方式1
    ano1=Author.objects.filter(ad__tel__startswith=110).values("book__title","book__publish__name")
    # print('---------------->')
    # print(ano1)

    # 方式2
    AuthorDetail.objects.filter(tel__startswith=110).values("author__book__title","author__book__publish__name")

    # 方式3
    Book.objects.filter(authors__ad__tel__startswith=110).values("title","publish__name")

    ########################聚合 分组###########################
    from django.db.models import Avg, Max, Sum, Min, Count
    avgPrice = Book.objects.all().aggregate(Avg("price"))
    print(avgPrice)

    #   单表分组查询
    # 查询书籍表每一个出版社id以及对应的书籍个数
    # select app01_book.nid,count(1) from app01_book group by publish_id;
    # key: annotate() 前value哪一个字段就按哪一个字段group by
    ret=Book.objects.values("publish_id").annotate(c=Count(1))
    print(ret)

    # 查询每一个部门的名称以及对应员工的平均工资
    ret=Emp.objects.values("dep").annotate(avg_salary=Avg("sal"))
    print(ret)

    # 查询每一个省份的名称以及对应的员工人数
    ret=Emp.objects.values("addr").annotate(num_person=Count(1))
    print(ret)


    #########跨表分组查询
    #查询每一个出版社的名名称以及对应的书籍平均价格
    # 查询select 语句  select app01_publish.name,count(1) from app01_book inner join app01_publish on app01_book.publish_id = app01_publish.nid
    #                      group by app01_publish.nid
    ret=Publish.objects.values("name").annotate(avg_price=Avg("book__price"))
    print(ret)

    # 查询每一个作者的名字以及出版的书籍的最高价格
    ret=Author.objects.values("nid","name").annotate(max_price=Max("book__price"))
    print(ret)

    # 查询每一个书籍的名称以及对应的作者的个数
    ret = Book.objects.values("pk","title").annotate(total=Count("authors"))
    print(ret)

    # 查询作者数不止一个的书籍名称以及作者个数
    ret=Book.objects.annotate(c=Count("authors")).filter(c__gt=1).values("title","c")
    print(ret)
    '''
        SELECT app01_book.title,COUNT(app01_author.nid) as c FROM app01_book 
        INNER JOIN app01_book_authors on app01_book.nid=app01_book_authors.book_id
        INNER JOIN app01_author on app01_author.nid=app01_book_authors.author_id
        GROUP BY app01_book.nid,app01_book.price,app01_book.publish_id,app01_book.pub_date,app01_book.title
        HAVING c>1
    '''


    from django.db.models import F,Q
    ret=Book.objects.filter(price__gt=100).values("title")
    ret = Book.objects.filter(price=F("ad__pub_date")*2)

    return HttpResponse("__(Join)查询")