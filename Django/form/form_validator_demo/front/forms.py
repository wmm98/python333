from django import forms
from django.core import validators
from .models import User


class MyForm(forms.Form):
    # email = forms.EmailField(error_messages={"invalid": "请输入正确的邮箱"})
    # 相同用法一样
    # email = forms.CharField(validators=[validators.EmailValidator(message='请输入正确格式的邮箱')])
    # price = forms.FloatField(error_messages={"invalid": "请输入浮点类型"})

    # 以13， 14，15，16，17，18开头的11位数
    # telephone = forms.CharField(validators=[validators.RegexValidator(r'1[345678]\d{9}')])
    telephone = forms.CharField(validators=[validators.RegexValidator("1[345678]\d{9}", message='请输入正确格式的手机号码！')])


"""RegexValidator：如果还需要更加复杂的验证，那么我们可以通过正则表达式的验证器：RegexValidator。比如现在要验证手机号码是否合格，
那么我们可以通过以下代码实现："""


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    telephone = forms.CharField(validators=[validators.RegexValidator(r'1[345678]\d{9}', message='请输入正确手机号码')])
    pwd1 = forms.CharField(max_length=16, min_length=6)
    pwd2 = forms.CharField(max_length=16, min_length=6)

    # 简化表单错误信息的提取
    # 平常返回的错误信息
    """
    {'telephone': [{'message': '请输入正确手机号码', 'code': 'invalid'}], 
    'pwd1': [{'message': 'Ensure this value has at least 6 characters (it has 5).', 'code': 'min_length'}], 
    '__all__': [{'message': '两次输入密码不一致', 'code': ''}]}
    """

    # 该方法是任何表单都可以用，如果在一个项目里面想所有表单都用该方法则可以定义一个类，在类下面复制
    # 该方法然后其他的表单都继承这个类。
    def get_errors(self):
        errors = self.errors.get_json_data()
        new_errors = {}
        for key, message_dicts in errors.items():
            messages = []
            for message_dict in message_dicts:
                message = message_dict['message']
                messages.append(message)
            new_errors[key] = messages
        return new_errors

    # 单一验证某个字段
    def clean_telephone(self):
        telephone = self.cleaned_data.get('telephone')
        telephone1 = User.objects.filter(telephone=telephone)
        if telephone1:
            raise forms.ValidationError(message='%s已经被注册！')
        # 如果验证没问题记得把telephone返回
        return telephone

    # 验证多个字段的时候 
    def clean(self):
        # 如果来到了clean方法，说明之前每一个字段都验证成功了
        cleaned_data = super().clean()
        pwd1 = cleaned_data.get("pwd1")
        pwd2 = cleaned_data.get("pwd2")

        if pwd1 != pwd2:
            raise forms.ValidationError(message='两次输入密码不一致')
        return cleaned_data
