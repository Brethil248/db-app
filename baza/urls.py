from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]

# ok, więc ?P<pk>\d+ oznacza ze do pk zostanie wpisane z url'a liczba
# ktora bedzie po /post/. Np jesli /post/1234/ to pk==1234
# pk -> primary key
