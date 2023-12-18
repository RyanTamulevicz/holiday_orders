from django.db import models
from django.utils import timezone


class Customer(models.Model):
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)


class Order(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, null=False)
    created = models.DateTimeField("date created", default=timezone.now())
    status = models.CharField(max_length=200)


class Item(models.Model):
    CATEGORY_CHOICES = [
        ("tenderloin", "Tenderloin"),
        ("rib_roast", "Rib Roast"),
        ("steaks", "Steaks"),
        ("lamb", "Lamb"),
        ("ham", "Ham"),
        ("misc", "Miscellaneous"),
    ]

    TYPE_CHOICES = [
        ("amish", "Amish"),
        ("berkshire", "Berkshire"),
        ("bone_in_quantity", "Bone-in Quantity"),
        ("bone_less_quantity", "Bone-less Quantity"),
        ("racks", "Racks"),
        ("loins", "Loins"),
        ("rib_chops", "Rib Chops"),
        ("legs", "Legs"),
        ("whole_in_the_bag", "Whole in the Bag"),
        ("whole_trimmed_and_tied", "Whole Trimmed and Tied"),
        ("center_cut", "Center Cut"),
    ]

    GRADE_CHOICES = [
        ("choice", "Choice"),
        ("prime", "Prime"),
        ("american", "American"),
        ("australian", "Australian"),
        ("new_zealand", "New Zealand"),
    ]

    category = models.CharField(
        max_length=200, choices=CATEGORY_CHOICES, default="default"
    )
    item_name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)
    page_number = models.IntegerField(default=0)
    line_number = models.IntegerField(default=0)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    grade = models.CharField(max_length=50, choices=GRADE_CHOICES, default="default")
    item_type = models.CharField(max_length=50, choices=TYPE_CHOICES, default="default")

    def __str__(self):
        return self.item_name

    @staticmethod
    def available_grade_choices(category):
        if category == "tenderloin":
            return [
                ("choice", "Choice"),
                ("prime", "Prime"),
                ("american", "American"),
                ("australian", "Australian"),
            ]
        if category == "rib_roast":
            return [
                ("choice", "Choice"),
                ("prime", "Prime"),
                ("american", "American"),
                ("australian", "Australian"),
            ]
        elif category == "lamb":
            return [("american", "American"), ("new_zealand", "New Zealand")]
        else:
            return []

    @staticmethod
    def available_type_choices(category):
        if category == "ham":
            return [("amish", "Amish"), ("berkshire", "Berkshire")]
        elif category == "lamb":
            return [
                ("racks", "Racks"),
                ("loins", "Loins"),
                ("rib_chops", "Rib Chops"),
                ("legs", "Legs"),
            ]
        elif category == "rib_roast":
            return [
                ("bone_in_quantity", "Bone-in Quantity"),
                ("bone_less_quantity", "Bone-less Quantity"),
            ]
        elif category == "tenderloin":
            return [
                ("whole_in_the_bag", "Whole in the Bag"),
                ("whole_trimmed_and_tied", "Whole Trimmed and Tied"),
                ("center_cut", "Center Cut"),
            ]
        else:
            return []
