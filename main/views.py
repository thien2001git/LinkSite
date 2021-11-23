from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader, RequestContext, Template
from django.template.loader import render_to_string
from django.urls import resolve, reverse

from .models import Type, Links
from .forms import AddType, AddLink
from django.http import HttpResponseRedirect

nav = render_to_string('main/layout.html')


def tr(request):
    ty = Type.objects.all()
    return render(request, 'main/Type/rd.html', {'ty': ty, 'nav': nav})


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

    return render(request, 'main/Type/u.html', {'form': form, 'li': t1, 'tt': tt, 'nav': nav})


def tc(request):
    form = AddType()
    if request.method == 'POST':
        form = AddType(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('../../type/r')
    return render(request, 'main/Type/c.html', {'form': form, 'tt': 0, 'nav': nav})


def td(request, _id):
    rm = Type.objects.get(id=_id)
    rm.delete()
    return HttpResponseRedirect('../../type/r')


def ls(request):
    if request.method == 'POST':
        ty = Type.objects.all()
        li = Links.objects.raw(
            "SELECT * FROM main_links where name like '%{}%' or url like '%{}%'".format(request.POST['ss'],
                                                                                        request.POST['ss']))
        re = RequestContext(request, {'ty': ty, 'li': li, 'nav': nav})

        return render(request, 'main/Link/s.html', {'ty': ty, 'li': li, 'nav': nav})
    else:
        return render(request, 'main/Link/s.html', {'ty': None, 'li': None, 'nav': nav})


def lr(request):
    ty = Type.objects.all()
    li = Links.objects.all()
    # print("{} {}".format())
    return render(request, 'main/Link/r.html', {'ty': ty, 'li': li, 'nav': nav})


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

    return render(request, 'main/Link/u.html', {'form': form, 'li': t1, 'tt': tt, 'nav': nav})


def lc(request):
    form = AddLink()
    if request.method == 'POST':
        form = AddLink(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('../../link/r')
    return render(request, 'main/Link/c.html', {'form': form, 'tt': 0, 'nav': nav})


def ld(request, _id):
    rm = Links.objects.get(id=_id)
    rm.delete()
    return HttpResponseRedirect('../../link/r')
