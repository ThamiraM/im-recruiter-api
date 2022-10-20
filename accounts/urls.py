from xml.etree.ElementInclude import include
from django.urls import path
from .views import SignupView, GetCSRFToken

urlpatterns = [
    path('register/', SignupView.as_view(), name="accounts-register"),
    path('csrf_cookie/', GetCSRFToken.as_view(), name="csrf-cookie"),
]
