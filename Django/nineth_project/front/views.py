from django.shortcuts import render


# 静态文件加载
# 1.首先确保 django.contrib.staticfiles已经添加到 settings.INSTALLED_APPS中
#
# 2.在settings.py中设置了STATIC_URL
#
# 3.在已经安装的app下创建一个文件夹叫做static,然后在这个static文件下创建一个当前app的名字的文件夹，再把静态文件放到这个文件夹下
#     例如你的app叫做book,有一个静态文件叫做zhiliao.jpg, 那么路径为 book/static/book/zhiliao.jpg.
#     (为什么在app下创建一个static文件夹，还需要在static下创建一个同app名字的文件夹呢？原因是如果直接把静态文件放在static文件夹下
#      ，那么在模板加载静态文件的时候就是使用zhilioa.jpg,如果多个app之间用同名的静态文件，这时候就可能会产生混淆，而在staic下加了一个
#      同名app文件夹，在模板中加载的时候就是使用app/zhiliao.jpg, 这样就可以避免产生混淆)
#
# 4. 如果有一些静态文件是不和任何app挂钩的， 那么可以在settings.py中添加STATIC_DIRS,以后DTL就会在这个列表的路径中查找静态文件，比如可以
#     设置为
#
#     STATIC_DIRS = {
#         os.path.join(BASE_DIR, "static")
#     }
#
# 5.在模板中使用load标签加载static标签。比如要加载在项目的static文件夹下的style.css的文件。那么实例代码如下
#     {% load static %}
#     <link rel="stylesheet"  href="{% static 'style.css' %}">

# 6.如果不想每次在模板中加载静态文件都使用load标签加载static标签，那么可以在settings.py中的TEMPLATES/OPTIONS添加
#     'builtins':['django.templatetags.static'],这样以后在模板中就可以直接使用static标签，而不用手动的load了

# 7.如果没有在settings.INSTALL_APP中添加django.contrib.staticfiles.那么我们就需要手动的将请求静态文件中的url与静态文件的路径进行映射了，
#     实列代码如下
#     from django.conf import settings
#     from django.conf.urls.static import static
#
#     urlpatterns = [
#         # 其他的url映射
#
#     ] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

def index(request):
    return render(request, 'index.html')
