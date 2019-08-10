from django import forms


class MessageBoardForm(forms.Form):
    title = forms.CharField(max_length=100, min_length=2, label='标题', error_messages={"min_length": "最少不能少于1个字符"})
    content = forms.CharField(widget=forms.Textarea, label='内容', error_messages={"required": "必须要传content字段"})
    email = forms.EmailField(label="邮箱", error_messages={"required": "必须要传eamil字段!"})
    # required=False 可填可不填
    reply = forms.BooleanField(required=False, label='是否回复')


# class MessageBoardForm(forms.Form):
#     title = forms.CharField(max_length=3, label='标题', min_length=2, error_messages={"min_length": '标题字符段不符合要求！'})
#     content = forms.CharField(widget=forms.Textarea, label='内容')
#     email = forms.EmailField(label='邮箱')
#     reply = forms.BooleanField(required=False, label='回复')
