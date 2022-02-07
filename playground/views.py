from django.http import HttpRequest
from django.db.models.aggregates import Count, Avg
from django.shortcuts import render

from items.models import Weapon


def say_hello(request):
    count = Weapon.objects.aggregate(Avg('cost'))

    return render(request, 'hello.html', {'name': 'Graham', 'count': count})


# def say_hello(request):
#     weapon = Weapon.objects.select_related('damage_type').all()
#
#     return render(request, 'hello.html', {'name': 'Graham', 'weapons': list(weapon)})


# def say_hello(request):
#     weapon = Weapon.objects.prefetch_related('properties').all()
#
#     return render(request, 'hello.html', {'name': 'Graham', 'weapons': list(weapon)})
