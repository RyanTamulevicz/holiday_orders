from orderInput.models import Customer, Item, Category, Order

from django.db import transaction


def create_get_customer_and_order(request):
    information = create_request_dict(request)
    customer, order = customer_and_order_creation(information)

    input_items_to_db(information, order)

    return customer, order


def create_request_dict(request):
    last_name = request.POST.get("last-name")
    phone_number = request.POST.get("phone-number")

    category = request.POST.getlist("category[]")
    item_names = request.POST.getlist("item_name[]")
    quantities = request.POST.getlist("quantity[]")
    page_numbers = request.POST.getlist("page_number[]")
    line_numbers = request.POST.getlist("line_number[]")
    return {
        "last_name": last_name,
        "category": category,
        "phone_number": phone_number,
        "item_names": item_names,
        "quantities": quantities,
        "page_numbers": page_numbers,
        "line_numbers": line_numbers,
    }


def customer_and_order_creation(information):
    with transaction.atomic():
        try:
            customer, created_customer = Customer.objects.get_or_create(
                last_name=information["last_name"],
                phone_number=information["phone_number"],
            )

            order, created_order = Order.objects.get_or_create(
                customer=customer, status="Pending"
            )

            if created_customer or created_order:
                customer.save()
                order.save()

        except Exception:
            raise
    return customer, order


def input_items_to_db(information, order):
    with transaction.atomic():
        try:
            for i in range(len(information["category"])):
                category, created_category = Category.objects.get_or_create(
                    category_name=information["category"][i]
                )

                item, created_item = Item.objects.get_or_create(
                    category=category,
                    item_name=information["item_names"][i],
                    page_number=information["page_numbers"][i],
                    line_number=information["line_numbers"][i],
                    order=order,
                )

                if created_category or created_item:
                    category.save()
                    item.save()
        except Exception:
            raise
