from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("product/<slug:slug>/", views.product_detail, name="product_detail"),
    path("preorder/thanks/<int:pk>/", views.preorder_thanks, name="preorder_thanks"),
    # NEW ↓
    path("refund-policy/", views.refund_policy, name="refund_policy"),
    path("privacy-policy/", views.privacy_policy, name="privacy_policy"),
]