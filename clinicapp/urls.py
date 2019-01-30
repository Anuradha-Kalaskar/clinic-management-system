from django.conf.urls import url
from clinicapp import views

app_name = 'clinicapp'

urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login')
]
