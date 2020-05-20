from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


app_name = 'accounts'

urlpatterns = [
    url(r'signup/', views.SignUpView.as_view(template_name = 'accounts/signup.html'), name= 'signup_url'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name = 'accounts/login.html'), name= 'login_url'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name = 'accounts/logout.html'), name= 'logout_url'),
    url(r'^password_change/$', auth_views.PasswordChangeView.as_view(template_name = 'accounts/password_change.html'), name= 'password_change_url'),
    url(r'^password_change/done/$', auth_views.PasswordChangeDoneView.as_view(template_name = 'accounts/password_change_done.html'), name= 'password_change_done_url'),

]
