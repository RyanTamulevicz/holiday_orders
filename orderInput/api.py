from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from .models import Customer
from .utils.input_utils import create_get_customer_and_order

import re


def new_item_row(request):
    return render(request, "partials/input/new_item_row.html")


@require_POST
def submit_order(request):
    phone_number = request.POST.get("phone-number")

    if not re.match(r"^\(\d{3}\) \d{3}-\d{4}$", phone_number):
        return HttpResponse("Invalid phone number format", status=400)

    create_get_customer_and_order(request)
    return render(request, "input.html")


def clear_order(request):
    return render(request, "input.html")


@require_POST
def auto_complete_phone(request):
    entered_number = request.POST.get("phone-number", "")

    phone_numbers = Customer.objects.filter(
        phone_number__startswith=entered_number
    ).values_list("phone_number", flat=True)

    phone_numbers_list = list(phone_numbers)

    if entered_number in phone_numbers_list:
        customer = Customer.objects.get(phone_number=entered_number)
        return_full_order(customer)

    return render(
        request,
        "partials/input/auto_complete_phone_input.html",
        {"phone_numbers": phone_numbers_list},
    )


def fetch_phone_number_info(request):
    print(request.GET.get("phone-number"))
    customer = Customer.objects.get(phone_number=request.GET.get("phone-number"))
    print(return_full_order(customer))
    return HttpResponse("success")


def return_full_order(customer):
    order = customer.order
    print(order)

    return
