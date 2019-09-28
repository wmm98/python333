from django import forms
from django.contrib.auth import get_user_model


class LoginForm(forms.ModelForm):
    # 登录表单，由于数据库中该字段是唯一的而且已经存在了，登录的时候会冲突，需要另起字段
    telephone = forms.CharField(max_length=11, required=True)
    remember = forms.ImageField(required=False)

    class Meta:
        model = get_user_model()
        fields = ['password']