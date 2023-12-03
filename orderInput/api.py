from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.http import HttpResponse

import re


def new_item_row(request):
    return render(request, "partials/new_item_row.html")


@require_POST
def submit_order(request):
    # last_name = request.POST.get("last-name")
    phone_number = request.POST.get("phone-number")
    print(phone_number)
    if not re.match(r"^\(\d{3}\) \d{3}-\d{4}$", phone_number):
        return HttpResponse("Invalid phone number format", status=400)
    print(phone_number)
    # if customer := Customer.objects.filter(
    #     last_name=last_name, phone_number=phone_number
    # ):
    #     customer = customer[0]
    # else:
    #     customer = Customer.objects.create(last_name=last_name, phone_number=phone_number)
    return render(request, "input.html")


def clear_order(request):
    return render(request, "input.html")
