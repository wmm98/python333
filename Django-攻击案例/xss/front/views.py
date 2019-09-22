from django.shortcuts import render, reverse, redirect
from .models import Comment
from django.views.decorators.http import require_http_methods
from django.template.defaultfilters import escape
import bleach
from bleach.sanitizer import ALLOWED_ATTRIBUTES, ALLOWED_TAGS


def index(request):
    context = {
        'comments': Comment.objects.all()
    }
    return render(request, 'index.html', context=context)


# 输入的案例
"""
<script>window.onload = function () {
    var imgTag = document.createElement("img");
imgTag.setAttribute('src', 'http://img.haote.com/upload/news/image/20170605/20170605144101_12960.jpg');
document.body.appendChild(imgTag)
}</script>
"""



"""
如果不需要显示一些富文本，那么在渲染用户提交的数据的时候，直接进行转义就可以了。在Django的模板中默认就是转义的。
也可以把数据在存储到数据库之前，就转义再存储进去，这样以后在渲染的时候，即使不转义也不会有安全问题，示例代码如下：
"""

# 添加评论
@require_http_methods(['POST'])
def add_comment(request):
    content = request.POST.get('content')
    # 经过转义之后的content, 模板中打开safe也没关系
    content = escape(content)
    Comment.objects.create(content=content)
    return redirect('index')

# 添加评论
@require_http_methods(['POST'])
def add_comment1(request):
    content = request.POST.get('content')
    # tags：表示允许哪些标签。
    # attributes：表示标签中允许哪些属性。
    # ALLOWED_TAGS：这个变量是bleach默认定义的一些标签。如果不符合要求，可以对其进行增加或者删除。
    # ALLOWED_ATTRIBUTES：这个变量是bleach默认定义的一些属性。如果不符合要求，可以对其进行增加或者删除。

    # 增加标签，不会修改原本的结构（用append就会修改其本身）
    tags = ALLOWED_TAGS + ['img']
    print(tags)
    # ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code', 'em', 'i', 'li', 'ol', 'strong', 'ul', 'img']
    # 增加允许的标签
    attributes = {**ALLOWED_ATTRIBUTES, 'img': ['src']}
    print(attributes)
    # {'a': ['href', 'title'], 'abbr': ['title'], 'acronym': ['title'], 'img': ['src']}
    cleaned_data = bleach.clean(content, tags=tags, attributes=attributes)
    Comment.objects.create(content=cleaned_data)
    return redirect('index')


# 默认内置的一些标签
"""
ALLOWED_TAGS = [
    'a',
    'abbr',
    'acronym',
    'b',
    'blockquote',
    'code',
    'em',
    'i',
    'li',
    'ol',
    'strong',
    'ul',
]
"""

# 内置默认属性
"""
ALLOWED_ATTRIBUTES = {
    'a': ['href', 'title'],
    'abbr': ['title'],
    'acronym': ['title'],
}

"""



