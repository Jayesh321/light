from django.conf.urls import url
from django.contrib.auth import views as auth_view
from . import views


app_name = 'accounts'

urlpatterns = [
    url(r'signup/$', views.SignupView.as_view(template_name = 'accounts/signup.html'), name= 'signup_url'),
    url(r'login/$', auth_view.LoginView.as_view(template_name = 'accounts/login.html'), name= 'login_url'),
    url(r'logout/$', auth_view.LogoutView.as_view(template_name = 'accounts/logout.html'), name= 'logout_url'),
]
