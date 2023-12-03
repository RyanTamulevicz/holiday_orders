from django.urls import path

from . import views
from . import api

urlpatterns = [
    path("", views.input, name="input"),
    path("api/new-input-row", api.new_item_row, name="new-input-row"),
    path("api/submit-order", api.submit_order, name="submit-order"),
    path("api/clear-order", api.clear_order, name="clear-order"),
]
