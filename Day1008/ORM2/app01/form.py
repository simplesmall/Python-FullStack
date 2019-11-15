from django import forms
from app01.models import Publish,Author
from django.forms import widgets

class BookForm(forms.Form):
    title=forms.CharField(max_length=32)
    price=forms.IntegerField()
    pub_date=forms.DateField(widget=widgets.TextInput(attrs={"type":"date"}))
    #publish=forms.ChoiceField(choices=[(1,"AAA"),(2,"BBB")])
    publish=forms.ModelChoiceField(queryset=Publish.objects.all())
    authors=forms.ModelMultipleChoiceField(queryset=Author.objects.all())


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for filed in self.fields.values():
            filed.widget.attrs.update({'class': 'form-control'})


from app01.models import Book,Author,Publish
from django.forms import widgets as wid

class BookModelForm(forms.ModelForm):
    class Meta:
        model=Book
        fields="__all__"
        # fields=["title","price","pub_date"]
        # exclude=["title"]
        labels={
            "title":"书籍名称",
            "price":"价格"
        },
        error_messages={
            "title":{"required":"不能为空"}
        },
        widgets={
            "pub_date":wid.TextInput(attrs={"type":"date"})
        }

    def clean_price(self):
        # 定义局部钩子
        pass
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for filed in self.fields.values():
            #filed.error_messages={"required":"不能为空"}
            filed.widget.attrs.update({'class': 'form-control'})