from django.shortcuts import render
from .utils.input_utils import get_categories


def input(request):
    return render(request, "input.html", {"categories": get_categories()})
