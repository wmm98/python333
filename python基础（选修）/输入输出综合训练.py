"""
张三 1.85 105.5 108
李四 1.62 62.5 70
王五 1.73 76.3 74
"""

total_info = []
for i in range(3):
    info = input().split()
    total_info.append(info)
# print(total_info)

print('{0}        {1}      {2}      {3}'.format("姓名", "身高", "体重", "腰围"))
for i in total_info:
    print('{0:<10}{1:<10}{2:<10}{3:<10}'.format(i[0], i[1], i[2], i[3], chr(12288)))


# tplt = "{0:{3}^10}\t{1:{3}^10}\t{2:^10\t{3:^10}}"
# print(tplt.format("姓名", "身高", "体重", "腰围", chr(12288)))
# for i in range(total_info):
#     u = total_info[i]
#     print(tplt.format(u[0], u[1], u[2], u[3], chr(12288)))

# name = "欧阳娜娜"
# height1 = 1.6
# weight1 = 49
# name2 = "汪涵"
# height2 = 1.75
# weight2 = 75
#
# print('{0:{3}<10}{1:<10}{2:<10}'.format(name, height1, weight1, chr(12288)))
# print('{0:{3}<10}{1:<10}{2:<10}'.format(name2, height2, weight2, chr(12288)))

