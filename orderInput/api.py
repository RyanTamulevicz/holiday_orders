from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.http import HttpResponse, JsonResponse

import re


def new_item_row(request):
    return render(request, "partials/new_item_row.html")


@require_POST
def submit_order(request):
    last_name = request.POST.get("last-name")
    phone_number = request.POST.get("phone-number")

    item_names = request.POST.getlist("item_name[]")
    quantities = request.POST.getlist("quantity[]")
    page_numbers = request.POST.getlist("page_number[]")
    line_numbers = request.POST.getlist("line_number[]")
    print(last_name, phone_number, item_names, quantities, page_numbers, line_numbers)

    if not re.match(r"^\(\d{3}\) \d{3}-\d{4}$", phone_number):
        return HttpResponse("Invalid phone number format", status=400)

    # if customer := Customer.objects.filter(
    #     last_name=last_name, phone_number=phone_number
    # ):
    #     customer = customer[0]
    # else:
    #     customer = Customer.objects.create(last_name=last_name, phone_number=phone_number)
    return render(request, "input.html")


def clear_order(request):
    return render(request, "input.html")


def auto_complete_phone(request):
    partial_number = request.GET.get("phone-number", "")
    print(partial_number)
    # Implement logic to search for matching phone numbers
    # For example, using a database query
    matching_numbers = [
        "(123) 456-7890",
        "(234) 567-8901",
        ...,
    ]  # Replace with actual search logic

    return JsonResponse({"suggestions": matching_numbers})
