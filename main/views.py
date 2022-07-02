from typing import Dict
from unicodedata import name
from django import forms
from django.forms import ChoiceField
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.template import loader, RequestContext, Template
from django.template.loader import render_to_string
from django.urls import resolve, reverse

from .models import Type, Links
from django.http import HttpResponseRedirect


class some_method:
    @staticmethod
    def sort_key(e):
        return e.name


class to_html:
    @staticmethod
    def index(req):
        ctx = dict()
        ctx["title"] = "Trang chủ"
        ctx["type"] = list(Type.objects.all())
        ctx["link"] = list(Links.objects.all())
        ctx["link"].sort(key=some_method.sort_key)

        for i in ctx["type"]:
            i.dem = sum(p.idType.id == i.id for p in ctx["link"])
            i.save()


        return render(req, "main/link/index.html", ctx)

    @staticmethod
    def tk(req):
        ctx = dict()
        ctx["title"] = "Trang chủ"
        ctx["type"] = Type.objects.all()


        ctx["link"] = list(Links.objects.all())
        que = "SELECT * FROM main_links where name like '%{}%' or url like '%{}%'".format(req.POST["tk"], req.POST["tk"])
        print(que)
        # ctx["link"].sort(key=some_method.sort_key)
        # print("SELECT * FROM main_links WHERE {} IN name OR {} IN url".format(req.POST["tk"], req.POST["tk"]))
        if (req.method == "POST"):
            ctx["link"] = list(Links.objects.raw(que))

        ctx["link"].sort(key=some_method.sort_key)
        for i in ctx["type"]:
            i.dem = sum(p.idType.id == i.id for p in ctx["link"])
            # i.save()

            # pass
        return render(req, "main/link/index.html", ctx)


class xldl:
    @staticmethod
    def add_link(req):
        # print(req)
        if req.method == "POST":
            print(req.POST)
            moi = Links(idType=Type.objects.get(id=req.POST["loai"]),
                        name=req.POST["name"],
                        url=req.POST["url"]
                        )
            if "id" in req.POST.keys():
                moi.id = req.POST["id"]
            moi.save()
        return redirect('index')

    @staticmethod
    def dem(req, id):
        it = Links.objects.get(id=id)
        it.dem += 1
        it.save()
        print(it)
        return HttpResponse("ok")

    @staticmethod
    def del_link(req, id):
        it = Links.objects.get(id=id)
        it.delete()
        print(it)
        return redirect('index')

    @staticmethod
    def add_type(req):
        if req.method == "POST":
            moi = Type(name=req.POST["name"])
            if "id" in req.POST.keys():
                moi.id = req.POST["id"]
                print(moi.id)
            moi.save()
        return redirect('index')

    @staticmethod
    def del_type(req, id):
        it = Type.objects.get(id=id)
        it.delete()
        print(id)
        return HttpResponse("ok")
