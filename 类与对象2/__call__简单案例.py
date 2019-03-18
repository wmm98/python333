class bi:
    def __init__(self, type_bi):
        self.type = type_bi

    def __call__(self, color):
        print("这是一支%s, 它的颜色是 %s" % (self.type, color))


b = bi("钢笔")
b("红色")
b("黑色")

# 这是一支钢笔, 它的颜色是 红色
# 这是一支钢笔, 它的颜色是 黑色

b = bi("蜡笔")
b("蓝色")
b("灰色")

# 这是一支蜡笔, 它的颜色是 蓝色
# 这是一支蜡笔, 它的颜色是 灰色
