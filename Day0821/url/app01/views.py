from django.shortcuts import render, HttpResponse


# Create your views here.

def year_article(request, year):
    return HttpResponse(year)


def year_article_two(request, month, year):
    # return HttpResponse("Year:%s  month %s" % (year, month))
    return HttpResponse("Year:${yeay} month ${month}")

def index(request):
    return HttpResponse("INDEX")
