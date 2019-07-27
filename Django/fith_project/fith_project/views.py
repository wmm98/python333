from django.shortcuts import render


# if标签使用解析
def index(request):
    # context = {
    #     'age': 18
    # }

    context = {
        'hero': [
            '鲁班一号',
            '项羽',
            '程咬金'
        ],

        'person': {
            'username': 'zhiliao',
            'age': 18,
            'height': 180
        },

        'book': [
            {
                'name': '水浒传',
                'author': '施耐庵',
                'price': 190
            },

            {
                'name': '挪威的森林',
                'author': '村上',
                'price': 110
            },

            {
                'name': '英国病人',
                'author': '迈克尔',
                'price': 146
            },

            {
                'name': '飘',
                'author': '不知道',
                'price': 100
            }

        ],

        'comments': [
        ]

    }
    return render(request, 'index.html', context=context)