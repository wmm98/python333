import memcache

# 在连接之前一定要切记先启动memcached
mc = memcache.Client(["127.0.0.1:11211"], debug=True)

# 设置数据
# mc.set('username', 'abc', time=120)
# # 获取数据
# print(mc.get('username'))

# 设置多个键值对
# mc.set_multi({"title": "钢铁是怎么练成的", 'content': "你好世界"}, time=120)

# 删除键
# mc.delete("username")

# 已设置了age=20
# 自动增长10, 若不设置delta就自动增长1
# mc.incr('age', delta=10)
# age = mc.get("age")
# print(age)

# 自动减少
mc.decr('age', delta=10)