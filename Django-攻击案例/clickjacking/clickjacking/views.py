from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


"""
像以上场景1，是没有办法避免的，受伤害的是用户。而像场景2，受伤害的是百度贴吧网站和用户。这种场景是可以避免的，
只要设置百度贴吧不允许使用iframe被加载到其他网页中，就可以避免这种行为了。我们可以通过在响应头中设置X-Frame-Options来设置这种操作。
X-Frame-Options可以设置以下三个值：

DENY：不让任何网页使用iframe加载我这个页面。
SAMEORIGIN：只允许在相同域名（也就是我自己的网站）下使用iframe加载我这个页面。
ALLOW-FROM origin：允许任何网页通过iframe加载我这个网页。
在Django中，使用中间件django.middleware.clickjacking.XFrameOptionsMiddleware可以帮我们堵上这个漏洞，
这个中间件设置了X-Frame-Option为SAMEORIGIN，也就是只有在自己的网站下才可以使用iframe加载这个网页，
这样就可以避免其他别有心机的网页去通过iframe去加载了。
"""