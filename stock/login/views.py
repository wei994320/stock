from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from login.models import Info, Focus
import time


# Create your views here.
# def index(request):
#     return HttpResponse('OK')


# 必须要返回一个响应，响应的是HttpResponse的实例对象
def index(request):
    # 参数1：当前请求
    # 参数2：模板文件
    # 获取数据
    stock_data = Info.objects.all()
    paginator = Paginator(stock_data, 10)
    # 获取页面请求中的页码
    page = request.GET.get('page', 1)

    page_skus = paginator.page(page)
    context = {
        'stock_data': page_skus,
        'page': page
    }

    return render(request, 'index.html', context)

    # return HttpResponse('index')


def center(request):
    # 参数1：当前请求
    # 参数2：模板文件
    return render(request, 'center.html')
    # return HttpResponse('index')


def edit(request):
    url = request.GET.get('id')
    stock_data = Info.objects.get(id=url)
    context = {
        'edit': stock_data
    }
    # print(context)
    return render(request, 'edit.html', context)


def form1(request):
    id1 = request.POST.get("id")
    code = request.POST.get('code')
    short = request.POST.get('short')
    chg = request.POST.get('chg')
    turnover = request.POST.get('turnover')
    price = request.POST.get('price')
    highs = request.POST.get('highs')
    time1 = request.POST.get("time")

    array = time.strptime(time1, u"%Y年%m月%d日")
    publishTime = time.strftime("%Y-%m-%d", array)
    data = {
        "code": code,
        "short": short,
        "chg": chg,
        "turnover": turnover,
        "price": price,
        "highs": highs,
        "time": publishTime,
    }

    Info.objects.filter(id=id1).update(**data)
    return redirect("/index.html/")
