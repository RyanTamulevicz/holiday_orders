from orderInput.models import Customer, Item, Order
from django.db import transaction


def create_get_customer_and_order(request):
    information = create_request_dict(request)
    print(information)
    # customer, order = customer_and_order_creation(information)

    # input_items_to_db(information, order)

    # return customer, order


def create_request_dict(request):
    # Existing fields
    last_name = request.POST.get("last-name")
    phone_number = request.POST.get("phone-number")

    # Dynamic fields
    categories = request.POST.getlist("category[]")
    grades = request.POST.getlist("grade[]", [])  # Optional field
    types = request.POST.getlist("type[]", [])  # Optional field
    item_names = request.POST.getlist("item-name", [])

    # Processing each category with its corresponding grade and type
    items = []
    for i, category in enumerate(categories):
        grade = grades[i] if i < len(grades) else None
        type = types[i] if i < len(types) else None
        item_name = item_names[i] if i < len(item_names) else None
        items.append(
            {
                "category": category,
                "grade": grade,
                "type": type,
                "item_name": item_name,
            }
        )

    return {"last_name": last_name, "phone_number": phone_number, "items": items}


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
            items = Item.objects.filter(order=order)
            items.delete()

            for i in range(len(information["category"])):
                item = Item.objects.create(
                    category=information["category"][i],
                    item_name=information["item_names"][i],
                    quantity=information["quantities"][i],
                    page_number=information["page_numbers"][i],
                    line_number=information["line_numbers"][i],
                    order=order,
                    grade="default",  # Replace with your default grade
                    type="default",  # Replace with your default type
                )

                item.save()

        except Exception:
            raise


def return_full_order(customer):
    order = customer.order
    return Item.objects.filter(order=order)


def get_categories():
    return Item.CATEGORY_CHOICES
