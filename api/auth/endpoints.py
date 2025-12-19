from .api import (
    custom_login,
    custom_register,
    custom_logout,
    profile,
    change_password,
    activate,
    deactivate,
    test_email_send,
)

# urlpatterns = [
#     # path("login/", custom_login, name="login"),
#     # path("register/", custom_register, name="register"),
#     # path("logout/", custom_logout, name="logout"),
#     # path("profile/", profile, name="profile"),
#     # path("change_password/", change_password, name="change_password"),
#     # path("activate/", activate, name="activate"),
#     # path("deactivate/", deactivate, name="deactivate"),
# ]

from django.urls import path
from .generic_accounts_api import (
    LoginView,
    LogoutView,
    RegisterView, 
    ProfileView,
    DeactivateAccountView,
    ChangePasswordView,
    # ActivateAccountView,
)

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("deactivate/", DeactivateAccountView.as_view(), name="deactivate"),
    path("change_password/", ChangePasswordView.as_view(), name="change_password"),
    # path("activate/", ActivateView.as_view(), name="activate"),
    path("send-test-email/", test_email_send, name="send-test-email")
]
