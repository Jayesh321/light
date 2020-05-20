from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


app_name = 'accounts'

urlpatterns = [
    url(r'signup/', views.SignUpView.as_view(template_name = 'accounts/signup.html'), name= 'signup_url'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name = 'accounts/login.html'), name= 'login_url'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name = 'accounts/logout.html'), name= 'logout_url'),
]
