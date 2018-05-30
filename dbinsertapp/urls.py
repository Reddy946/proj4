from django.conf.urls import url
from . import views
app_name='dbinsertapp'
urlpatterns = [
url(r'^$',views.input, name='input'),
url(r'^insert$',views.insert,name='insert'),
]
