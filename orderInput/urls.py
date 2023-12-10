from django.urls import path

from . import views
from . import api

urlpatterns = [
    path("", views.input, name="input"),
    path("api/new-input-row", api.new_item_row, name="new-input-row"),
    path("api/submit-order", api.submit_order, name="submit-order"),
    path("api/clear-order", api.clear_order, name="clear-order"),
    path(
        "api/auto-complete-phone", api.auto_complete_phone, name="auto-complete-phone"
    ),
    path(
        "api/fetch-phone-number-info",
        api.fetch_phone_number_info,
        name="fetch-phone-number-info",
    ),
]
