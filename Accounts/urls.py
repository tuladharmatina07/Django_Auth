from django.urls import path
from . import views
from django.contrib.auth import views as authview
from django.urls import reverse_lazy
app_name = 'Accounts'
urlpatterns = [
    path('register/', views.registration, name="Register"),
    path('login/', authview.LoginView.as_view(template_name="login.html"), name ="Login"),
    path('logout/', authview.LogoutView.as_view(template_name="logout.html")),
    path('', views.home, name="home"),
    path('change-password/', authview.PasswordChangeView.as_view(success_url=reverse_lazy('account:change_password_done')), name='change_password'),
    path('change-password-done/', authview.PasswordChangeDoneView.as_view(template_name="change-password-done.html"), name ="change_password_done")
]
