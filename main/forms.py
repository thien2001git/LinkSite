from django import forms
from .models import Type, Links


class Search(forms.Form):
    ss = forms.CharField(label='Tìm kiếm')


class AddType(forms.Form):
    n1 = forms.CharField(label="Tên")

    def save(self):
        li = Type.objects.all()
        t = Type(name=self.cleaned_data['n1'])

        t.save()

    def save1(self, _id, _name):
        t = Type.objects.get(id=_id)
        t.name = _name
        # print(t)
        t.save()

    @staticmethod
    def lt():
        li = Type.objects.all()
        ll = []
        for i in li:
            ll.append((i.id, i.name))
        return ll


# def ty():


class AddLink(forms.Form):
    # type = forms.CharField(label="Loại")
    type = forms.ChoiceField(label="Loại", widget=forms.RadioSelect, choices=AddType.lt())
    name = forms.CharField(label="Tên")
    url = forms.CharField(label="Url")

    def ret(self):
        return type

    def save(self):
        li = Type.objects.all()
        _id = Type()
        for i in li:
            if i.id == int(self.cleaned_data['type']):
                _id = i
        # print(self.cleaned_data['type'])
        t = Links(idType=_id, name=self.cleaned_data['name'], url=self.cleaned_data['url'])
        t.save()

    def save1(self, _id, _name, _type, _url):
        li = Type.objects.all()
        for i in li:
            if i.name == _type:
                _id = i.id
        t = Links.objects.get(id=_id)
        t.name = _name
        t.idType = Type.objects.get(id=_type)
        t.url = _url
        # print(t)
        t.save()
