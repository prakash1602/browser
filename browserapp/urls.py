from django.conf.urls import url
from django.contrib import admin
from browserapp.views import index,details,makeentry

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',index),
    url(r'^browserapp/info/(\d+)/$',details,),
    url(r'^makeentry/',makeentry, name='makeentry')
]
