from django.shortcuts import render

from .models import Statistics


def item_list(request):
    items = Statistics.objects.all()
    context = {
        'title': ['月份', '投产验证总变更单', '应用科驳回', '到达应用科次数', '应用科驳回率',
                  '到达次数为总变更单的倍数'],
        'statistics': items,
        'legend': [data.month for data in items],
        'x_axis_data': [data.month for data in items],
        'total_number': [data.total_num for data in items],
        'reject_number': [data.reject for data in items],
        'reject_rating': [data.reject_rating for data in items],
        'reject_times': [data.times for data in items]
    }
    return render(request, "index.html", context)


def item_show(request):
    items = Statistics.objects.all()
    context = {
        'title': 'User Traffic History',
        'legend': [data.month for data in items],
        'x_axis_data': [data.month for data in items],
        'total_number': [data.total_num for data in items],
        'reject_number': [data.reject for data in items],
        'reject_rating': [data.reject_rating for data in items],
        'reject_times': [data.times for data in items]
    }
    return render(request, "my_show.html", context)
