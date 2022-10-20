from xml.etree.ElementInclude import include
from django.urls import path
from .views import SignupView, GetCSRFToken, CheckAuthenticated, LoginView, LogoutnView

urlpatterns = [
    path(
        'authenticated/',
        CheckAuthenticated.as_view(),
        name="check-authenticated"
    ),
    path('register/', SignupView.as_view(), name="accounts-register"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutnView.as_view(), name="logout"),
    path('csrf_cookie/', GetCSRFToken.as_view(), name="csrf-cookie"),
]
