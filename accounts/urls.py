from django.conf.urls import url
from django.contrib.auth import views as auth_view
from . import views


app_name = 'accounts'

urlpatterns = [
    url(r'signup/$', views.SignupView.as_view(template_name = 'accounts/signup.html'), name= 'signup_url'),
]
