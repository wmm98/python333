from django.urls import converters, register_converter


class CategoryConverter:
    regex = r'\w+|(\w+\+\w+)+'

    def to_python(self, value):
        # value: python+django+flask
        # ['python', 'django', 'flask']
        result = value.split("+")
        return result

    def to_url(self, value):
        # value:['python', 'django', 'flask']
        # python+django+flask
        if isinstance(value, list):
            result = "+".join(value)
            return result
        else:
            raise RuntimeError("转换url的时候， 分类参数必须未列表")


register_converter(CategoryConverter, 'cate')
