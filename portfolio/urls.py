from django.conf.urls import url
from . import views

from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.views import password_change
from django.contrib.auth.views import password_change_done
from django.contrib.auth.views import password_reset
from django.contrib.auth.views import password_reset_done
from django.contrib.auth.views import password_reset_confirm
from django.contrib.auth.views import password_reset_complete

app_name='portfolio'

urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
   # url(r'^notifications/$', views.notifications, name='notifications'),
    #url(r'^signup/$',views.signup,name='signup'),
    url(r'^employee/$', views.employee_list, name='employee_list'),
    url(r'^employee/(?P<pk>\d+)/delete/$', views.employee_delete, name='employee_delete'),
    url(r'^employee/(?P<pk>\d+)/edit/$', views.employee_edit, name='employee_edit'),
    url(r'^employee/create/$', views.employee_new, name='employee_new'),
    url(r'^account_settings_list/$', views.account_settings_list, name='account_settings_list'),
    url(r'^register/$', views.register, name='register'),
    url(r'^account/register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    # previous login view
    # url(r'^login/$', views.user_login, name='login'),

    # login / logout urls
    # login / logout urls
    url(r'^login/$',
        'django.contrib.auth.views.login',
        name='login'),
    url(r'^logout/$',
        'django.contrib.auth.views.logout',
        name='logout'),
    url(r'^logout-then-login/$',
        'django.contrib.auth.views.logout_then_login',
        name='logout_then_login'),

    # change password urls
    url(r'^password-change/$',
        'django.contrib.auth.views.password_change',
        name='password_change'),
    url(r'^password-change/done/$',
        'django.contrib.auth.views.password_change_done',
        name='password_change_done'),
# restore password urls
url(r'^password-reset/$',
    'django.contrib.auth.views.password_reset',
    name='password_reset'),
url(r'^password-reset/done/$',
    'django.contrib.auth.views.password_reset_done',
    name='password_reset_done'),
url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
    'django.contrib.auth.views.password_reset_confirm',
    name='password_reset_confirm'),
url(r'^password-reset/complete/$',
    'django.contrib.auth.views.password_reset_complete',
    name='password_reset_complete'),


]
