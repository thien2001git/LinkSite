from typing import Dict
from unicodedata import name
from django import forms
from django.forms import ChoiceField
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader, RequestContext, Template
from django.template.loader import render_to_string
from django.urls import resolve, reverse

from .models import Type, Links
from .forms import AddType, AddLink
from django.http import HttpResponseRedirect
import requests
from bs4 import BeautifulSoup

# nav = render_to_string('main/layout.html')


def img():
    # url = 'http://www.bing.com/HPImageArchive.aspx?format=xml&idx=0&n=1&mkt=en-US'
    # r = requests.get(url, allow_redirects=False)
    # data = str(r.content[:])

    # tree = BeautifulSoup(data)
    # image = tree.findAll("url")
    # stri = "https://www.bing.com/{}".format(str(image[0].get_text()))
    return ""


def tr(request):
    ty = Type.objects.all()
    return render(request, 'main/Type/rd.html', {'ty': ty,  "ba": img()})


def tu(request, tt):
    form = AddType()
    ty = Type.objects.all()
    t1 = Type()
    for i in range(len(ty)):
        if tt == ty[i].id:
            t1 = ty[i]
            break
    if request.method == 'POST':
        print(form)
        n = request.POST['n1']
        form.save1(tt, n)
        return HttpResponseRedirect('../../type/r')

    return render(request, 'main/Type/u.html', {'form': form, 'li': t1, 'tt': tt,  "ba": img()})


def tc(request):
    
    if request.method == 'POST':
        ty = Type(name=request.POST['n1'], dem=0)
        ty.save()
        
        return HttpResponseRedirect('../../type/r')
    return render(request, 'main/Type/c.html', { 'tt': 0,  "ba": img()})


def td(request, _id):
    rm = Type.objects.get(id=_id)
    rm.delete()
    return HttpResponseRedirect('../../type/r')

def dem(request, id):
    l = Links.objects.get(id=id)
    print(l)
    l.dem = l.dem+1
    l.save()

    t = l.idType
    t.dem = t.dem + 1
    t.save()
    return lr(request)

def ls(request):
    # print(request)
    if request.method == 'GET':
        # print(request.GET)
        ty = Type.objects.all()
        li = Links.objects.raw(
            "SELECT * FROM main_links where name like '%{}%' or url like '%{}%'".format(request.GET['ss'],
                                                                                        request.GET['ss']))
        # re = RequestContext(request, {'ty': ty, 'li': li})

        return render(request, 'main/Link/s.html', {'ty': ty, 'li': li,  'val': request.GET['ss']})
    else:
        return render(request, 'main/Link/s.html', {'ty': None, 'li': None})

# lấy tất cả link
def lr(request):
    ty = Type.objects.all()
    li = Links.objects.all()
    # print("{} {}".format())
    # if request.method == "POST":

    return render(request, 'main/Link/r.html', {'ty': ty, 'li': li, 'ba': img()})


def lu(request, tt):
    form = AddLink()
    ty = Type.objects.all()
    t1 = Type()
    for i in range(len(ty)):
        if tt == ty[i].id:
            t1 = ty[i]
            break
    if request.method == 'POST':
        # print(form)
        # n = request.POST['n1']
        _type = request.POST['type']
        _name = request.POST['name']
        _url = request.POST['url']
        form.save1(tt, _name, _type, _url)
        return HttpResponseRedirect('../../link/r')
    t = Links.objects.get(id=tt)
    return render(request, 'main/Link/u.html',
                  {'type': ty, 'id': tt, 'name': t.name, 'nametype': t1.name, "url": t.url, "ba": img()})


def ty():
    li = Type.objects.all()
    ll = []
    for i in li:
        ll.append((i.id, i.name))
    return ll


def lt():
    li = Type.objects.all()
    ll = []
    for i in li:
        ll.append((i.id, i.name))
    return ll


def lc(request):
    # form = AddLink()
    # ChoiceField.validate(form.type, lt())
    ty = list(Type.objects.all())
    cxt = dict()
    cxt = {'ty': ty, 'tt': 0}
   
    ba = img()
    if request.method == 'POST':
        # print(request.POST["loai"])
        if request.POST["nm"] == "" or print(request.POST["u"]) == "":
            cxt["mess"] = "Lỗi bạn đã đế trống trường tên hoặc url"
        else:
            l = Links(idType=Type.objects.filter(id=request.POST["loai"]).first(), name=request.POST["nm"], url=request.POST["u"], dem=0)
            l.save()
            cxt['mess'] = "Thành công"
    return render(request, 'main/Link/c.html', context=cxt)


def ld(request, _id):
    rm = Links.objects.get(id=_id)
    rm.delete()
    return HttpResponseRedirect('../../link/r')

def tk(req):
    ctx = dict()
    li = list(Links.objects.all())

    li.sort(key= lambda x : x.dem, reverse=True)
    # print(li)
    ctx["li"] = li

    return render(req, 'main/ThongKe/tk.html', context=ctx)