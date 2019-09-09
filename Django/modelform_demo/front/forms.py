from django import forms
from .models import Book, User


class AddBookForm(forms.ModelForm):
    # 对某个字段进行深度验证
    def clean_page(self):
        page = self.cleaned_data.get('page')
        if page > 100:
            raise forms.ValidationError("价格不能大于100!")
        return page

    class Meta:
        model = Book
        # 绑定左右字段
        fields = "__all__"
        # 绑定两个字段
        # fields = ['title', 'page']
        # 不包括此字段
        # exclude = ['price']
        error_messages = {
            'page': {
                'required': '请传入page参数',
                'invalid': '请输入一个可用的page参数'

            },
            'title': {
                'max_length': 'title不能超过100个字符'
            },
            'price': {
                'max_value': '图书价格不能超过100元'
            }
        }


# 注册表单
class RegisterForm(forms.ModelForm):
    pwd1 = forms.CharField(max_length=16, min_length=6)
    pwd2 = forms.CharField(max_length=16, min_length=6)

    def clean(self):
        cleaned_data = super().clean()
        pwd1 = cleaned_data.get("pwd1")
        pwd2 = cleaned_data.get("pwd2")
        if pwd1 != pwd2:
            raise forms.ValidationError("两次输入密码不一致")
        else:
            return cleaned_data

    class Meta:
        model = User
        exclude = ['password']
