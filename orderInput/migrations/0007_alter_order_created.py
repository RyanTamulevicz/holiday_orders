# Generated by Django 4.2.7 on 2023-12-10 17:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orderInput", "0006_alter_item_order"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 12, 10, 17, 19, 26, 432660, tzinfo=datetime.timezone.utc
                ),
                verbose_name="date created",
            ),
        ),
    ]