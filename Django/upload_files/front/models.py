from django.db import models
from django.core import validators


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # 文件上传到files文件夹里面
    # thumbnial = models.FileField(upload_to="save_files")
    # 上传的文件按日期划分

    # 如果想要限制上传的文件的拓展名，那么我们就需要用到表单来进行限制。
    # 我们可以使用普通的Form表单，也可以使用ModelForm，直接从模型中读取字段。示例代码如下

    # 只能上传扩展名为txt文件
    # thumbnial = models.FileField(upload_to="%Y/%m/%d/", validators=[
    #     validators.FileExtensionValidator(['txt'], message="thumbnial必须为txt格式的文件")])

    # 上传图片
    thumbnial = models.ImageField(upload_to="%Y/%m/%d")
