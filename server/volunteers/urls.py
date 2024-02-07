from volunteers.views import *
from django.urls import path

app_name = "volunteers"

urlpatterns = [
    path("", home_page, name="home_page"),
    path('admin_user_login/', admin_user_login, name='admin_user_login'),
    path('admin_user_signup/', admin_user_signup, name='admin_user_signup'),
    path('admin_user_logout/', admin_user_logout, name='admin_user_logout'),
    path('anonymous_user_login/', anonymous_user_login, name='anonymous_user_login'),
    path('anonymous_user_signup/', anonymous_user_signup, name='anonymous_user_signup'),
    path('anonymous_user_logout/', anonymous_user_logout, name='anonymous_user_logout'),
    path('validate/', validate, name='validate'),
    path('anonymous_user_list/', anonymous_user_list, name='anonymous_user_list'),

]