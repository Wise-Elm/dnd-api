from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from items.models import Weapon


def say_hello(request):
    try:
        weapon = Weapon.objects.get(pk=30)
    except ObjectDoesNotExist:
        pass

    return render(request, 'hello.html', {'name': 'Graham'})
